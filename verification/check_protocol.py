#!/usr/bin/env python3
"""Finite matrix checks of the thermal constructions and cutoff illustration.

These checks do not simulate the full asymptotic universal extractor. They
construct actual small energy-conserving permutations, trace their outputs,
and compare them with the analytical channel and probability formulas.
"""

from __future__ import annotations

import argparse
import itertools
import json
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np


TOL = 2e-12


def entropy(state: np.ndarray) -> float:
    values = np.linalg.eigvalsh((state + state.conj().T) / 2)
    if values.min() < -TOL:
        raise AssertionError(f"State has negative eigenvalue {values.min()}")
    positive = values[values > 0]
    return float(-np.sum(positive * np.log(positive)))


def gibbs(energies: np.ndarray, beta: float) -> np.ndarray:
    weights = np.exp(-beta * (energies - np.min(energies)))
    return weights / weights.sum()


def divergence_to_gibbs(state: np.ndarray, energies: np.ndarray, beta: float) -> float:
    probabilities = gibbs(energies, beta)
    return float(-entropy(state) - np.dot(np.diag(state).real, np.log(probabilities)))


def tensor(*states: np.ndarray) -> np.ndarray:
    result = np.ones((1, 1), dtype=complex)
    for state in states:
        result = np.kron(result, state)
    return result


def permutation_unitary(basis: list[tuple[int, ...]], transform) -> np.ndarray:
    lookup = {x: i for i, x in enumerate(basis)}
    destinations = [lookup[transform(x)] for x in basis]
    if len(set(destinations)) != len(basis):
        raise AssertionError("Proposed basis map is not bijective")
    result = np.zeros((len(basis), len(basis)), dtype=complex)
    result[destinations, np.arange(len(basis))] = 1
    return result


def unitary_residuals(unitary: np.ndarray, energies: np.ndarray) -> dict[str, float]:
    identity = np.eye(len(energies))
    residuals = {
        "unitarity": float(np.linalg.norm(unitary.conj().T @ unitary - identity)),
        "energy_commutator": float(
            np.linalg.norm(unitary * energies[None, :] - energies[:, None] * unitary)
        ),
    }
    if max(residuals.values()) > TOL:
        raise AssertionError(residuals)
    return residuals


def thermal_cutoff(state: np.ndarray, energies: np.ndarray, beta: float, cutoff: int):
    tail = float(np.trace(state[cutoff:, cutoff:]).real)
    return state[:cutoff, :cutoff] + tail * np.diag(gibbs(energies[:cutoff], beta))


def check_cutoff() -> dict:
    dimension, cutoff, beta = 5, 3, 0.8
    energies = np.array([0.0, 0.7, 1.9, 3.0, 5.5])
    basis = list(itertools.product(range(dimension), range(cutoff)))
    unitary = permutation_unitary(
        basis, lambda x: (x[1], x[0]) if x[0] < cutoff else x
    )
    residuals = unitary_residuals(
        unitary, np.array([energies[i] + energies[j] for i, j in basis])
    )
    rng = np.random.default_rng(20261109)
    vector = rng.normal(size=dimension) + 1j * rng.normal(size=dimension)
    vector /= np.linalg.norm(vector)
    matrix = rng.normal(size=(dimension, dimension)) + 1j * rng.normal(
        size=(dimension, dimension)
    )
    mixed = matrix @ matrix.conj().T
    mixed /= np.trace(mixed)
    high = np.zeros((dimension, dimension), dtype=complex)
    high[-1, -1] = 1
    states = {
        "coherent_pure": np.outer(vector, vector.conj()),
        "mixed": mixed,
        "high_energy": high,
        "gibbs": np.diag(gibbs(energies, beta)),
    }
    bath = np.diag(gibbs(energies[:cutoff], beta))
    results = {}
    for name, state in states.items():
        joint = unitary @ tensor(state, bath) @ unitary.conj().T
        # Trace the original source, retaining the finite Gibbs ancilla.
        reduced = np.einsum("iaib->ab", joint.reshape(dimension, cutoff, dimension, cutoff))
        predicted = thermal_cutoff(state, energies, beta, cutoff)
        channel_error = float(np.linalg.norm(reduced - predicted))
        nested = thermal_cutoff(
            thermal_cutoff(state, energies, beta, 4), energies[:4], beta, cutoff
        )
        nesting_error = float(np.linalg.norm(nested - predicted))
        divergences = [
            divergence_to_gibbs(thermal_cutoff(state, energies, beta, k), energies[:k], beta)
            for k in range(1, dimension + 1)
        ]
        if channel_error > TOL or nesting_error > TOL:
            raise AssertionError((name, channel_error, nesting_error))
        if np.min(np.diff(divergences)) < -TOL:
            raise AssertionError((name, divergences))
        results[name] = {
            "channel_error": channel_error,
            "nesting_error": nesting_error,
            "divergences": divergences,
        }
    gibbs_error = float(np.linalg.norm(thermal_cutoff(states["gibbs"], energies, beta, cutoff) - bath))
    if gibbs_error > TOL:
        raise AssertionError(gibbs_error)
    return {"unitary": residuals, "gibbs_preservation_error": gibbs_error, "states": results}


def check_decoder() -> dict:
    # Source qubit, two identical Gibbs bath qubits, and a Gibbs bit J.
    # P is the excited-state projector. The joint basis is (S, A0, A1, J).
    basis = list(itertools.product(range(2), repeat=4))

    def swap_selected(x):
        state = list(x)
        position = 1 + state[3]
        state[0], state[position] = state[position], state[0]
        return tuple(state)

    def decode_unique(x):
        state = list(x)
        accepted = [j for j in range(2) if state[1 + j] == 1]
        if len(accepted) == 1:
            state[3] = (state[3] - accepted[0]) % 2
        return tuple(state)

    swap = permutation_unitary(basis, swap_selected)
    decoder = permutation_unitary(basis, decode_unique)
    energies = np.array([s + a0 + a1 for s, a0, a1, _ in basis], dtype=float)
    unitary = decoder @ swap
    residuals = unitary_residuals(unitary, energies)
    beta = np.log(2.0)
    bath = np.diag(gibbs(np.array([0.0, 1.0]), beta))
    position = np.eye(2) / 2
    sources = {
        "excited": np.diag([0.0, 1.0]),
        "gibbs": bath,
        "coherent": np.array([[0.5, -0.5j], [0.5j, 0.5]]),
    }
    results = {}
    for name, source in sources.items():
        joint = unitary @ tensor(source, bath, bath, position) @ unitary.conj().T
        output = np.einsum("iaib->ab", joint.reshape(8, 2, 8, 2))
        off_diagonal = float(np.linalg.norm(output - np.diag(np.diag(output))))
        if off_diagonal > TOL:
            raise AssertionError((name, off_diagonal))
        results[name] = {
            "ground_population": float(output[0, 0].real),
            "off_diagonal_norm": off_diagonal,
        }
    # Direct classical enumeration gives 5/6, including extra success on the failure branch.
    if abs(results["excited"]["ground_population"] - 5 / 6) > TOL:
        raise AssertionError(results)
    if abs(results["gibbs"]["ground_population"] - 1 / 2) > TOL:
        raise AssertionError(results)
    return {"unitary": residuals, "states": results, "unique_acceptance_lower_bound": 2 / 3}


def check_charging() -> dict:
    # J has M degenerate states; W has the active levels 0 and work;
    # the bath has one ground state and M states at energy work.
    dimension, work, beta = 3, 1.0, np.log(2.0)
    basis = list(itertools.product(range(dimension), range(2), range(dimension + 1)))
    swaps = {}
    for label in range(dimension):
        left, right = (0, 0, label + 1), (label, 1, 0)
        swaps[left], swaps[right] = right, left
    unitary = permutation_unitary(basis, lambda x: swaps.get(x, x))
    energies = np.array([work * (w + int(b > 0)) for _, w, b in basis])
    residuals = unitary_residuals(unitary, energies)
    bath = np.diag(gibbs(np.array([0.0] + [work] * dimension), beta))
    battery = np.diag([1.0, 0.0])
    results = {}
    for ground_probability in [1.0, 0.8, 1 / dimension]:
        position = np.diag(
            [ground_probability] + [(1 - ground_probability) / (dimension - 1)] * (dimension - 1)
        )
        joint = unitary @ tensor(position, battery, bath) @ unitary.conj().T
        diagonal = np.diag(joint).real
        actual = float(sum(diagonal[i] for i, x in enumerate(basis) if x[1] == 1))
        predicted = ground_probability * dimension * np.exp(-beta * work) / (
            1 + dimension * np.exp(-beta * work)
        )
        if abs(actual - predicted) > TOL:
            raise AssertionError((actual, predicted))
        results[str(ground_probability)] = {"actual_success": actual, "formula_success": float(predicted)}
    return {"unitary": residuals, "position_ground_probabilities": results}


def coherent_curve(destination: Path) -> dict:
    beta, gap = 1.0, 1.0
    ratio = np.exp(-beta * gap)
    limit = gap * ratio / (1 - ratio) - np.log1p(-ratio) / beta
    cutoffs = np.arange(1, 19)
    coherent, dephased = [], []
    for cutoff in cutoffs:
        energies = gap * np.arange(cutoff)
        amplitudes = np.sqrt(1 - ratio) * ratio ** (np.arange(cutoff) / 2)
        tau = np.diag(gibbs(energies, beta))
        state = np.outer(amplitudes, amplitudes) + ratio ** cutoff * tau
        coherent.append(divergence_to_gibbs(state, energies, beta) / beta)
        dephased.append(divergence_to_gibbs(tau, energies, beta) / beta)
    if min(np.diff(coherent)) < -TOL or abs(coherent[-1] - limit) > 2e-6:
        raise AssertionError((coherent, limit))
    destination.mkdir(parents=True, exist_ok=True)
    plt.rcParams.update({"font.size": 11, "axes.spines.top": False,
                         "axes.spines.right": False, "svg.hashsalt": "universal-quantum-work"})
    figure, axis = plt.subplots(figsize=(7.8, 4.5), layout="constrained")
    axis.plot(cutoffs, coherent, "o-", color="#176b82", linewidth=2, markersize=4,
              label="Pure source with thermal populations")
    axis.plot(cutoffs, dephased, "s-", color="#9a4c24", linewidth=1.5, markersize=3,
              label="Dephased source (Gibbs state)")
    axis.axhline(limit, color="#334155", linestyle="--", linewidth=1.2,
                 label=f"Full coherent-source rate: {limit:.5f}")
    axis.set(xlabel="Retained energy levels K", ylabel="Cutoff free energy per copy",
             title="Thermal compression retains usable coherence", ylim=(-0.06, 1.16))
    axis.set_xticks([1, 3, 6, 9, 12, 15, 18])
    axis.grid(axis="y", alpha=0.2)
    axis.legend(loc="center right", frameon=False, fontsize=9)
    figure.savefig(destination / "coherent_cutoff.png", dpi=180)
    svg_path = destination / "coherent_cutoff.svg"
    figure.savefig(svg_path, metadata={"Date": None})
    svg_path.write_text("\n".join(line.rstrip() for line in svg_path.read_text().splitlines()) + "\n")
    plt.close(figure)
    data = {"beta": beta, "gap": gap, "ratio": float(ratio), "limit": float(limit),
            "cutoffs": cutoffs.tolist(), "coherent": coherent, "dephased": dephased}
    (destination / "coherent_cutoff.json").write_text(json.dumps(data, indent=2) + "\n")
    return {"largest_cutoff": int(cutoffs[-1]), "limit": float(limit),
            "last_cutoff_error": float(limit - coherent[-1])}


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, default=Path(__file__).resolve().parent / "results")
    args = parser.parse_args()
    figures = Path(__file__).resolve().parent / "figures"
    report = {"scope": "Finite constructions and a cutoff illustration; not an asymptotic numerical proof.",
              "tolerance": TOL, "cutoff": check_cutoff(), "decoder": check_decoder(),
              "charging": check_charging(), "coherent_curve": coherent_curve(figures)}
    args.output.mkdir(parents=True, exist_ok=True)
    output = args.output / "finite_checks.json"
    output.write_text(json.dumps(report, indent=2) + "\n")
    print(json.dumps({"status": "passed", "report": str(output),
                      "checks": ["conditional swap", "Gibbs preservation", "nested cutoff",
                                 "relative-entropy monotonicity", "commuting position decoder",
                                 "finite-bath charging", "coherent-source cutoff curve"]}, indent=2))


if __name__ == "__main__":
    main()
