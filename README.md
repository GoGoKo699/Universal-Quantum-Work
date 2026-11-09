# Universal Quantum Work

Can one thermodynamic engine extract the full free-energy work rate from every unknown quantum source, without being told its state, energy bound, or population tail?

This repository constructs such an engine for an i.i.d. source with a known discrete Hamiltonian and a finite Gibbs partition function. For every fixed source state with finite relative entropy to equilibrium, one source-independent sequence of exact thermal operations attains

$$
\frac{X_n}{n}\longrightarrow
f(\rho)=\frac{D(\rho\Vert\tau)}{\beta}
\qquad\text{in mean absolute deviation}.
$$

Here $X_n$ is the energy gained by one fixed oscillator battery, initially in its ground state; $n$ counts every supplied specimen, including training specimens. In the harmonic-oscillator case, the theorem covers **every finite-mean-energy state**, including coherent superpositions and slowly decaying population tails. The convergence is for each fixed source; it has no common sample-size guarantee over the whole class.

## The mechanism

The main step is a finite thermal replacement channel. It keeps the low-energy block, including its coherence, and replaces the discarded population by a finite Gibbs state:

$$
\Phi_K(\rho)
=\Pi_K\rho\Pi_K
+\operatorname{Tr}[(I-\Pi_K)\rho]\,\tau_K.
$$

A conditional swap with a Gibbs ancilla implements this channel exactly. It never rejects a specimen, and

$$
D\bigl(\Phi_K(\rho)\Vert\tau_K\bigr)
\uparrow D(\rho\Vert\tau).
$$

Uniform finite-dimensional extraction can therefore be combined with an arbitrarily slow, predetermined increase of the cutoff. A consumed training block controls the work target through projectors that commute with energy. The explicit finite extractor uses an exact position decoder and a finite charging bath, with every auxiliary register Gibbs initialized.

## Results and their precise scope

| Result | Guarantee | Authoritative account |
|---|---|---|
| Full work rate | Work per copy converges in probability and in mean to the free-energy rate, along all batch sizes. The stronger mean-absolute-deviation limit also holds. | [Model and theorem](science/model_theorem.md), [protocol](science/universal_protocol.md) |
| Output uncertainty | At every large batch size, at most two nearby coarse-grid energies carry probability approaching one. The total battery entropy is at most one bit asymptotically, including rare failure outputs. | [Protocol, §§7–8](science/universal_protocol.md#7-two-work-values-and-one-bit-of-output-entropy) |
| Exact energy levels | At least one member of each sufficiently late pair of batch sizes has an individual energy level with population approaching one. This attains the optimal exact-level rate with a limsup over batch size. | [Exact-level criterion](science/model_theorem.md#4-output-criteria) |
| Optimality | No thermal processor can reliably exceed the relative-entropy work rate. | [Converse](science/converse.md) |
| Sharp-output boundary | A canonical exact energy level cannot become certain along every batch size for every source in a continuously varying family. The one-bit entropy upper bound is sharp as a worst-source limsup statement. | [Output boundary](science/output_boundary.md) |
| Necessary pointwise qualification | Even a known mean-energy ceiling gives no uniform finite-sample guarantee over all states satisfying that ceiling. | [Oscillator examples, §4](science/oscillator.md#4-why-an-energy-bound-does-not-give-a-uniform-sample-guarantee) |

The construction uses exact global energy conservation, finite Gibbs ancillas at each batch size, and a battery that always starts at zero energy. It requires no initially pure auxiliary memory, catalyst, external phase reference, or work loan. Bath dimension, bath energy, control complexity, and running time can grow very rapidly. The result establishes an asymptotic capability, with no efficiency claim.

## Read the science

Start with the [scientific overview](science/README.md). For a direct proof route, read:

1. [The model and universal theorem](science/model_theorem.md).
2. [Thermal compression and monotone relative-entropy recovery](science/thermal_cutoff.md).
3. [The uniform finite-dimensional extractor](science/finite_extraction.md).
4. [The complete source-independent protocol](science/universal_protocol.md).
5. [The converse](science/converse.md), [output boundary](science/output_boundary.md), and [oscillator examples](science/oscillator.md).

The [related-work account](references/related_work.md) distinguishes inherited finite-dimensional extraction and statistical rounding methods from the infinite-dimensional thermal construction. The closest comparison is Watanabe and Takagi's [2026 universal work-extraction result](https://pmc.ncbi.nlm.nih.gov/articles/PMC12957447/), whose infinite-dimensional theorem assumes a finite candidate family and a stronger polynomial population-tail condition. The precise comparison includes the output criterion and its order of limits.

## Reproduce the finite checks

```bash
python3 -m pip install -r verification/requirements.txt
python3 verification/check_protocol.py
```

The script constructs small conditional-swap, position-decoding, and battery-charging unitaries; checks energy conservation and their reduced outputs; and reproduces the [coherent-source cutoff figure](science/oscillator.md#2-the-cutoff-preserves-coherence-inside-its-retained-sector). See [verification](verification/README.md) for exact scope, expected results, and the distinction between finite checks and the analytical asymptotic proof.

The [source register](references/source_register.md) records primary versions and theorem locators. The [LLM guide](llms.txt) maps scientific questions to their authoritative files.

## Purpose and contact

This repository serves as a record of the work and a guide for the author’s self-directed learning. For discussion or potential collaboration, please contact Ruge Lin at [gogoko699@gmail.com](mailto:gogoko699@gmail.com).
