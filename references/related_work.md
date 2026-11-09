# Relation to universal work extraction and canonical estimation

The result considered here is a source-independent sequence of thermal operations for an unknown iid state $\rho$ on a known discrete Hamiltonian with a normalizable Gibbs state $\tau$. For every fixed source with $D(\rho\Vert\tau)<\infty$, the measured work satisfies

$$
\frac{W_n}{n}\longrightarrow
\frac{D(\rho\Vert\tau)}{\beta}
\quad\text{in probability},
\qquad
S(\omega_{W,n})\leq\ln2+o(1).
$$

The battery is one fixed oscillator, initialized in its ground state. The same sequence also attains the exact-level rate in the pointwise $\lim_{\varepsilon\to0}\limsup_n$ convention. The source class includes every finite-mean-energy oscillator state, without a supplied energy ceiling, candidate list, or tail envelope.

This comparison separates that infinite-dimensional result from the finite-dimensional extraction and estimation methods it uses. The source register records versions and precise proof locations. The literature comparison is bounded and current to November 9, 2026.

## 1. Universal thermal work extraction

### The nearest work-extraction result

[Watanabe and Takagi (2026)](https://www.nature.com/articles/s41467-026-69143-3) prove universal finite-dimensional work extraction. Their infinite-dimensional result assumes a known finite source set with diagonal tails $p_i=O(i^{-(2+\varepsilon)})$ for some $\varepsilon>0$, and their discussion leaves continuous infinite-dimensional source families open. Their formal exact-level rate uses $\lim_{\varepsilon\to0}\limsup_n$.

The distinction in the present construction is the deterministic thermal channel

$$
\Phi_K(\rho)=\Pi_K\rho\Pi_K+
\bigl(1-\operatorname{Tr}\Pi_K\rho\bigr)\tau_K,
\qquad
\tau_K=\frac{\Pi_K\tau\Pi_K}{\operatorname{Tr}\Pi_K\tau}.
$$

It replaces an out-of-cutoff specimen by the truncated Gibbs state. Each specimen therefore produces a normalized finite-dimensional output; no whole-block survival event is required. Since the channel is an exact thermal operation and

$$
D(\Phi_K(\rho)\Vert\tau_K)\longrightarrow D(\rho\Vert\tau),
$$

the cutoff can increase slowly enough for a uniform finite-dimensional extractor. This removes the finite source-menu and tail-envelope assumptions. The paired-grid output construction addresses the same limsup exact-level convention while retaining an all-integer random-work rate guarantee.

### The finite-dimensional engine is inherited

[Faist (2026)](https://arxiv.org/abs/2601.20155) establishes universal thermodynamic implementations with a variable work cost. Theorem 1(ii) and Appendix C, Lemma 7, include uniform finite-dimensional extraction and a fixed-threshold construction. Its discussion restricts the analysis to finite dimension and leaves extension of those techniques to infinite dimension unclear.

The present finite-dimensional proof makes the extraction specialization explicit. Its energy and Schur-sector test uses the spectrum estimator of [Keyl and Werner (2001)](https://doi.org/10.1103/PhysRevA.64.052311), the entropy-continuity bound of [Audenaert (2007)](https://doi.org/10.1088/1751-8113/40/28/S18), and [Hoeffding's inequality](https://doi.org/10.1080/01621459.1963.10500830).

The position-decoding architecture is inherited from [Faist, Berta, and Brandão (2021)](https://doi.org/10.1007/s00220-021-04107-w), Section 7.2. In the extraction problem no quantum memory is retained. Tests on separate bath blocks commute, so their unique-acceptance projectors give an exact energy-conserving controlled-shift decoder on a register initially in its full Gibbs state. A separate finite Gibbs bath converts the resulting purity into one excited level of the ground-start oscillator battery.

This specialization supplies an explicit source-uniform error bound and the resource accounting required here. The finite-dimensional work-extraction capability, spectral estimator, concentration tools, and position-decoding principle are established ingredients.

### Black-box uncertainty is not the same universal task

[Watanabe and Takagi (2024)](https://arxiv.org/html/2407.03400v4) consider work extraction from a specified set of possible input states. Their thermal-operation Theorem 8 and Proposition S.17 assume a finite candidate set $S$ and attain the worst-source rate $\inf_{\rho\in S}D(\rho\Vert\tau)/\beta$. Their more general set-valued results use Gibbs-preserving or Gibbs-preserving covariant operations.

That theorem does not directly supply a thermal extractor uniform over an arbitrary compact source class. A finite net alone is insufficient, because product-state approximation errors must be controlled at the block length at which the net-dependent protocol operates. The source-uniform finite-dimensional threshold guarantee is therefore stated separately in the present proof.

Conditional control is also established machinery. The equivalence between incoherent projective conditioning and ordinary thermal operations is proved in the 2024 paper's Proposition S.23 and restated in the 2026 paper as Lemma S.5. It is related to the broader framework of [Narasimhachar and Gour (2017)](https://doi.org/10.1103/PhysRevA.95.012313). Here, the consumed training specimens themselves provide the control subspaces, and their number is included in the input budget.

## 2. Infinite-dimensional thermodynamics

[Ferrari, Lami, Theurer, and Plenio (2023)](https://pmc.ncbi.nlm.nih.gov/articles/PMC9898434/) develop asymptotic transformation bounds for continuous-variable resources. Their Theorem 15 and thermodynamic Corollary 17 give relative-entropy converse bounds. These support the role of free energy as an upper bound, but they do not provide the universal thermal-operation achievability established here. Their thermodynamic setting uses a Gibbs hypothesis at every positive inverse temperature; the present construction only requires normalizability at the working inverse temperature.

The earlier interacting-spin result of [Sagawa and collaborators (2021)](https://arxiv.org/abs/1907.05650) concerns asymptotic reversibility with increasing lattice size. Its finite local systems and work/coherence assistance differ from an arbitrary unknown state on one infinite energy ladder. Likewise, [Biswas and Winter (2026)](https://arxiv.org/abs/2609.09352) develop universal transformations in a work-and-heat framework with finite local dimension and commuting conserved charges. These are substantial thermodynamic antecedents, but neither result supplies the source class and battery guarantee used here.

A simple oscillator example shows that removing the tail condition changes the covered physical inputs. For $j\geq2$, let

$$
p_j=\frac{c}{j^2\ln^2(j+1)}
$$

with normalization constant $c$. Its mean occupation is finite, since $\sum_j[j\ln^2(j+1)]^{-1}<\infty$, but $p_j$ is not $O(j^{-(2+\varepsilon)})$ for any $\varepsilon>0$. The present construction covers this diagonal state and coherent superpositions with the same energy populations.

The convergence remains pointwise in the source. No source-independent finite-block rate, efficient circuit, bounded bath size, or finite-time implementation follows from the slowly increasing cutoff. Projection with replacement, data processing, lower semicontinuity, and diagonal selection are standard mathematical tools. The claim concerns their exact thermal implementation and the resulting source-independent extraction capability.

## 3. Exact labels, global stability, and list estimation

[Dixon, Pavan, Vander Woude, and Vinodchandran (2023)](https://proceedings.neurips.cc/paper_files/paper/2023/file/61d0a96d4a73b626367310b3ad32579d-Paper-Conference.pdf) explicitly show that coin-bias estimation at additive accuracy below half the bias-interval width cannot give one canonical accurate answer with probability greater than $1/2$ uniformly over biases at a common sample size. Their introductory example also explains why two rounded answers suffice. [Chase, Moran, and Yehudayoff (2023)](https://arxiv.org/abs/2304.03757) study the corresponding limitation through global stability and list replicability. These works already contain the connectedness obstruction and the one-versus-two output distinction.

[Plesnik and Violaris (2024)](https://doi.org/10.1088/1367-2630/ad7f7c) give an earlier thermodynamic distinguishability obstruction: one device cannot extract distinct exact deterministic work values from nonorthogonal single-shot inputs. Their Section 4.2 explicitly separates that setting from asymptotic many-copy distinguishability. Here the requirement is approximate canonical concentration along every block length for a continuous family, even though each fixed pair of distinct iid sources becomes distinguishable.

The [output-boundary theorem](../science/output_boundary.md) retains source-dependent convergence thresholds. For each finite block length, the output law is continuous in the source parameter. Baire category then turns pointwise eventual concentration into a common dominant label on some interval, contradicting a nowhere-locally-constant limiting rate. Under rate consistency alone, it gives a residual set on which

$$
\liminf_n\max_w\Pr_\rho(W_n=w)\leq\frac12.
$$

This is a pointwise, full-sequence strengthening of the finite-sample argument. No separate priority claim is made for the basic canonical-output obstruction or for two-list rounding.

For diagonal battery outputs, the resulting entropy statement is

$$
\limsup_n S(\omega_{W,n})\geq\ln2
$$

on that residual set. It is not an almost-everywhere statement and not a lower bound at every source or block length. The paired-grid implementation has $\liminf_n S(\omega_{W,n})=0$ for every source. A predetermined translation of the grids can also give full-sequence entropy convergence to zero at any one chosen reference source.

A separately specified schedule variant strengthens training accuracy enough that entropy tends to zero for Lebesgue-almost-every parameter in the commuting interval. Its residual set with limsup entropy $\ln2$ is consequently null. This measure statement is restricted to that scalar family and the strengthened schedule.

The upper construction quantizes a consistent free-energy estimate into bins wider than its estimation uncertainty. At most two adjacent bins are then likely. This is the one-dimensional list-estimation idea implemented through thermal branches. The additional entropy estimate requires $\eta_n\ln M_n\to0$, where $\eta_n$ is the error probability and $M_n$ is the active output dimension. Vanishing failure probability by itself would not control entropy on a growing battery.

## 4. Variable output size in other quantum tasks

Random output size is established in universal quantum information processing. [Hayashi and Matsumoto (2002)](https://arxiv.org/abs/quant-ph/0202001) construct universal variable-length quantum source codes with asymptotically vanishing error. [Matsumoto and Hayashi (2007)](https://doi.org/10.1103/PhysRevA.75.062338) concentrate unknown pure-state entanglement into an exact maximally entangled state of probabilistic dimension. Their normalized yield reaches the entropy rate without requiring concentration on one exact output dimension.

The mixed-state universal entanglement protocol of [Takagi and collaborators (2026)](https://arxiv.org/html/2609.40215v1) also uses a variable-length formulation with outcome-dependent target size. Its inputs have finite local dimension. The general universal resource-distillation theorem of [Lami, Regula, and Takagi (2026)](https://arxiv.org/html/2605.15174v1) is finite-dimensional and uses broader asymptotically resource-nongenerating operations. These comparisons place variable work within an existing operational pattern; they do not supply infinite-dimensional extraction under exact thermal operations.

## 5. Reliability is a separate comparison

[Zeng (2026)](https://arxiv.org/abs/2607.16702) proves a pointwise reliability limitation for phase-independent Gibbs-preserving extraction on a coherent qubit time-translation orbit. Its sources have the same free energy; the obstruction concerns an exponential failure rate at a fixed work target. The state-aware reliability functions are studied by [Watanabe, Regula, Tomamichel, and Takagi (2026)](https://arxiv.org/abs/2606.06318).

The output boundary here instead uses a commuting family whose optimal work rate varies. It concerns concentration on an exact energy label, without an exponential-error assumption. The infinite-dimensional construction claims no optimal reliability exponent. Broad statements that universality can affect reliability should therefore credit the existing reliability results rather than treating the label obstruction as the origin of that observation.

## 6. Division between imported methods and the present result

| Ingredient | Established basis | Role in this construction |
|---|---|---|
| Free-energy work rate in finite dimension | Brandão and collaborators (2013); universal extensions above | The target rate and finite-dimensional extraction engine are inherited. |
| Uniform finite-dimensional threshold extraction | Faist (2026), using Faist–Berta–Brandão (2021) | The present proof gives an explicit extraction specialization; its uniformity permits a source-independent cutoff schedule. |
| Energy and spectral estimation | Keyl–Werner (2001), Audenaert (2007), Hoeffding (1963) | Supplies a source-independent test and uniform error constants. |
| Position decoding | Faist–Berta–Brandão (2021), Section 7.2 | The no-retained-memory specialization uses commuting unique-acceptance projectors and an exact unitary on the Gibbs register. |
| Incoherent projective conditioning | Watanabe–Takagi (2024, 2026) | Compiles consumed training specimens and branch operations into one thermal operation. |
| Canonical-output obstruction and two-label rounding | Dixon and collaborators (2023); Chase and collaborators (2023) | The Baire proof preserves pointwise asymptotic quantifiers; the physical protocol realizes the rounded branches. |
| Thermal Gibbs-replacement cutoff | Exact implementation proved in the present construction | Removes whole-block postselection and permits universal extraction without a source-tail promise. |
| Fixed battery and controlled output entropy | Explicit construction and boundary proved here | Gives all-integer rate concentration, entropy at most $\ln2+o(1)$, and the exact-level limsup guarantee within one resource model. |

The resulting capability is full-rate work extraction from every unknown finite-energy oscillator source using one source-independent sequence. The constant entropy bound specifies its output more precisely. Neither the elementary rounding rule nor the statistical connectedness argument is presented as an independent thermodynamic discovery.

Full bibliographic metadata and the locations used for these comparisons are in the [source register](source_register.md) and [bibliography](bibliography.bib).
