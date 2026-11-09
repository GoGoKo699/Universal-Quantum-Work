# Scientific account

The question is whether ignorance of an infinite-dimensional quantum source prevents extraction of its full thermodynamic work rate. The source supplies independent copies of one fixed state. Its Hamiltonian and the bath temperature are known; its state, energy expectation, and population tail are not supplied.

Finite-dimensional universal extraction already gives the relevant thermodynamic capability when the local dimension is fixed. An unbounded source introduces a different problem: a cutoff that succeeds only when every specimen lies below a threshold needs control of the source tail. A fixed cutoff can fail on almost every sufficiently large batch even if its one-copy tail probability is small.

The thermal channel studied here processes each specimen without acceptance or rejection. It retains the selected energy block and replaces the complementary population by a Gibbs contribution. The channel is physically implementable by an exact energy-conserving swap. Its retained relative entropy approaches the original relative entropy from below. This gives a route from the fixed-dimensional uniform theorem to one processor sequence for every source with finite relative entropy.

## 1. Exact statements and proof route

| Page | Question it answers |
|---|---|
| [Model and theorem](model_theorem.md) | What does “one universal engine” mean, which source states are covered, and what counts as successful work? |
| [Thermal compression](thermal_cutoff.md) | How can an unbounded source be converted to a finite system using only a Gibbs ancilla, and why does its free-energy loss vanish? |
| [Finite extraction](finite_extraction.md) | How can a fixed free-energy threshold be distilled uniformly without a pure helper or an initial work loan? |
| [Universal protocol](universal_protocol.md) | How are training, target selection, extraction, and the increasing cutoff combined into a single source-independent thermal operation? |
| [Converse](converse.md) | Why is the achievable rate optimal, including under the exact-energy-level limsup criterion? |
| [Output boundary](output_boundary.md) | Why can work density converge while the most likely individual output level fails to become certain at every batch size? |
| [Oscillator examples](oscillator.md) | What happens to coherent superpositions, unusually slow tails, and attempts to obtain a uniform finite-sample bound? |

The proof has two distinct limiting statements. At a fixed cutoff, error bounds are uniform over every state of that finite system. As the cutoff increases, relative-entropy recovery holds for each fixed original state. The stage schedule uses the first statement to control processing error and the second to recover the desired rate. It does not assume a common rate for the second limit.

## 2. What is stored in the battery

The battery is one fixed oscillator initialized at its ground level. Every batch uses a finite energy alphabet, and its output is diagonal. At most two nearby coarse-grid energies carry all but a vanishing probability. Their separation divided by the number of source copies tends to zero, so both represent the same asymptotic work density.

The total battery entropy is at most $\ln2+o(1)$, including the contribution of rare outputs. A pair of shifted work grids also ensures one sharp exact label in at least one member of each late pair of batch sizes. This is enough for the exact-label criterion with a limsup over batch size.

These statements cannot be replaced by an assertion of a sharp exact label at every large batch size for every unknown source. The [boundary proof](output_boundary.md) establishes that obstruction already for a commuting two-level family. Its residual-set entropy conclusion is a statement about Baire category and subsequences, with no general probability or typical-source interpretation.

## 3. Physical accounting

All source specimens are charged, including the sublinear training block. Training projectors are used directly as energy-commuting controls, so there is no free classical measurement memory. All auxiliary systems start in full Gibbs states. The fixed battery's initial ground state is explicit in the model and in the converse.

The construction allows unrestricted collective control and very large finite Gibbs baths. It is a constructive existence result in that resource model. It does not establish a practicable device, a finite-time extraction law, or efficient bath scaling.

## 4. Attribution and checks

The [related-work account](../references/related_work.md) identifies which components are inherited and compares the actual source and output quantifiers with nearby results. The [source register](../references/source_register.md) gives precise primary locators, and the [bibliography](../references/bibliography.bib) provides structured citations.

The [finite checks](../verification/README.md) verify representative dilation formulas and energy-conserving permutations, including coherent inputs. They complement the proofs; they cannot establish an asymptotic theorem about all infinite-dimensional sources.

Return to the [repository overview](../README.md).
