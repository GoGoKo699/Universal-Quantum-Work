# Verification and reproduction

The asymptotic claims are analytical. The accompanying script checks the concrete finite thermal dilations on small Hilbert spaces and reproduces the cutoff figure from its exact finite-matrix formula.

## Run

From the repository root, use Python 3.11 or later:

```bash
python3 -m pip install -r verification/requirements.txt
python3 verification/check_protocol.py
```

The pinned environment uses NumPy 2.3.5 and Matplotlib 3.10.8. The script writes `verification/results/finite_checks.json` and regenerates the PNG, SVG, and numerical data in `verification/figures/`. It uses a fixed random seed only to select illustrative pure and mixed input matrices. The thermal operations themselves are deterministic constructions.

## What the checks establish

| Check | Construction and expected result |
|---|---|
| Thermal cutoff | Build the actual conditional-swap unitary on a five-level source and three-level Gibbs ancilla. Trace out the source and compare with the proposed cutoff channel on coherent pure, mixed, Gibbs, and high-energy inputs. |
| Conservation and normalization | Verify bijectivity of each basis map, unitarity, and commutation with the additive finite Hamiltonian. The exact permutation constructions have zero residual in these examples. |
| Gibbs preservation and nesting | Verify that compression maps the source Gibbs state to the normalized truncated Gibbs state and that an intermediate cutoff gives the same final channel. |
| Relative entropy | Compute the retained relative entropy at each finite cutoff and check monotonicity for the four example states. |
| Exact position decoder | Construct the full two-position decoder with a maximally mixed position bit. For an excited source and bath excitation probability one third, the position register's ground population is five sixths, above the unique-acceptance lower bound of two thirds. A Gibbs source leaves the register maximally mixed. |
| Battery charging | Construct the charging permutation with a three-state degenerate register and a bath of degeneracies one and three. At inverse temperature $\ln2$ and unit work gap, a pure register yields charging probability three fifths. Mixed-register cases reproduce equation (F44). |
| Coherence illustration | Generate the compressed state of the pure geometric superposition with thermal populations. Its free-energy curve increases to approximately 1.04065 for unit inverse temperature and gap; the dephased Gibbs source has zero relative entropy at every cutoff. |

Matrix residuals and differences are required to be below $2\times10^{-12}$. The curve check uses a finite-cutoff tolerance appropriate to its nonzero analytical tail. Floating-point values can differ slightly between linear-algebra implementations.

## What requires the proofs

The numerical checks do not simulate the full universal engine. Its ancillary dimension is far too large for these examples to be an implementation study. They do not establish uniform error bounds, convergence for arbitrary infinite-dimensional states, Baire-category statements, or the physical economy of a bath.

The authoritative proofs are:

- [Thermal compression](../science/thermal_cutoff.md), for the exact unbounded-system dilation and relative-entropy recovery.
- [Finite extraction](../science/finite_extraction.md), for state-uniform error bounds and Gibbs-only resource accounting.
- [Universal protocol](../science/universal_protocol.md), for the stage schedule, full-sequence convergence, entropy bound, and paired-grid exact-level criterion.
- [Converse](../science/converse.md) and [output boundary](../science/output_boundary.md), for optimality and the canonical-label obstruction.

The scripts use standard plotting and numerical linear algebra. Every displayed curve is generated from the scientific formulas, without fitted data or illustrative image generation.
