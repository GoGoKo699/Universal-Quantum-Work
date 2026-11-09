# From thermal operations to universal quantum work

An engine receives repeated preparations of one quantum state. It knows the source Hamiltonian and the bath temperature, but receives no description of the state. Its task is to charge a fixed battery using these specimens and thermal ancillas. The same sequence of engines must work for every admissible source.

The selected educational anchor is Matteo Lostaglio, *An introductory review of the resource theory approach to thermodynamics*, **arXiv:1807.11549v2, 7 October 2019**, published in *Reports on Progress in Physics* **82**, 114001 (2019). Use the [versioned PDF](https://arxiv.org/pdf/1807.11549v2), the [versioned HTML](https://arxiv.org/html/1807.11549v2), or the [publication](https://doi.org/10.1088/1361-6633/ab46e5). This bridge develops the particular task studied here; the [30-milestone map](milestones.md) gives its wider conceptual route.

## 1. What the engine receives and stores

The source has known energy levels and Gibbs state $`\tau=e^{-\beta H}/Z_\beta`$, where $`Z_\beta=\operatorname{Tr}e^{-\beta H}<\infty`$. Here $`\beta=1/(k_{\mathrm B}T)`$, and all logarithms are natural. Its unknown state is $`\rho`$. Independent, identically prepared specimens mean that the joint input at block length $`n`$ is $`\rho^{\otimes n}`$.

A thermal operation appends systems in their Gibbs states at the same temperature, applies a unitary preserving total energy, and discards systems. For unbounded Hamiltonians, the project states energy conservation through commutation with the full time evolution. Each engine uses only finitely many finite-dimensional thermal ancillas. Their sizes may increase with $`n`$.

The available work rate is

```math
f(\rho)=\frac{D(\rho\|\tau)}{\beta}.
```

Relative entropy $`D`$ measures distinguishability from the equilibrium state. For finite mean energy, this expression becomes $`\operatorname{Tr}(H\rho)-S(\rho)/\beta+\ln Z_\beta/\beta`$, with $`S(\rho)=-\operatorname{Tr}(\rho\ln\rho)`$. It is free energy above equilibrium, measured in units of energy. The relative-entropy definition also handles admissible states whose energy and entropy are separately infinite. The theorem assumes $`D(\rho\|\tau)<\infty`$, and covers every finite-energy oscillator state.

The battery is one oscillator with energies $`0,\Delta,2\Delta,\ldots`$ and starts in its ground state. Its gap $`\Delta`$ stays fixed across sources and block lengths. Raising it to the pure level $`|k\rangle`$ stores $`k\Delta`$ of energy without increasing entropy. A mixed battery output requires more care.

The [model and theorem](../science/model_theorem.md) specify these assumptions. Arbitrarily large finite baths and global interactions are allowed; there is no efficiency or locality guarantee.

## 2. A complete two-level example

Let the source be a qubit with energies $`0,\Delta`$ and state

```math
\rho_p=(1-p)|0\rangle\langle0|+p|1\rangle\langle1|.
```

Start the oscillator battery at $`|0\rangle`$. Apply the unitary that exchanges the joint states $`|1\rangle_S|0\rangle_W`$ and $`|0\rangle_S|1\rangle_W`$, and leaves every other basis state unchanged. The exchanged states both have total energy $`\Delta`$, so this is an allowed energy-conserving operation without an ancillary bath.

Afterward, the source is in its ground state and the battery is

```math
\omega_p=(1-p)|0\rangle\langle0|+p|1\rangle\langle1|.
```

An energy measurement returns $`\Delta`$ with probability $`p`$ and zero otherwise. Its mean is $`p\Delta`$. Its entropy is the binary entropy $`h(p)=-p\ln p-(1-p)\ln(1-p)`$, with $`0\ln0=0`$. Since the battery started with zero energy and zero entropy, its free-energy change is $`p\Delta-h(p)/\beta`$.

For $`p=1`$, the operation stores exactly $`\Delta`$ in a pure excited state. For $`p=1/2`$ and $`\beta\Delta=\ln2`$, the mean energy is $`\Delta/2`$, but the free-energy change is $`-\Delta/2`$. The operation has consumed some of the initially pure battery's usefulness while increasing its mean energy. The initial ground state is therefore an explicit resource in the model, even though it carries no positive energy.

This calculation explains the asymptotic objective. The desired engine stores energy proportional to $`n`$ while keeping battery entropy bounded. Its entropy contribution divided by $`n`$ then vanishes, so the stored energy rate also measures the battery's free-energy gain per specimen.

## 3. Translating the review's task

The review develops thermal operations in Section I.C and treats a two-level work-storage system in Section II.C.3. The main translations are:

| Object | Review's setting | This project's setting |
|---|---|---|
| Equilibrium state | $`\gamma_S`$ | $`\tau`$ |
| Resource relative to equilibrium | Nonequilibrium free energy | $`f(\rho)=D(\rho\|\tau)/\beta`$ |
| Work storage | A work bit whose excited level has energy $`W`$ | One fixed oscillator; a target is $`W=k\Delta`$ |
| Input description | A specified state transformation | One unknown fixed source, supplied as independent copies |
| Number of source levels | Finite-dimensional default | Countably many levels with a finite partition function |
| Output statement | Deterministic or approximate work transformations | Full-sequence rate, battery entropy, and exact-level subsequences |

The fixed ladder makes the work values of different engines directly comparable. Rounding a target energy down to a multiple of $`\Delta`$ loses less than one gap, which contributes less than $`\Delta/n`$ to the rate.

Unknown input changes the quantifiers. A separate good engine for each state does not supply a single engine that works without knowing the state. The project constructs one sequence depending only on $`H`$, $`\beta`$, $`\Delta`$, and $`n`$. For every fixed admissible $`\rho`$, that sequence approaches $`f(\rho)`$. This is **pointwise universality**. It does not promise one finite sample size that achieves a prescribed accuracy simultaneously for all admissible infinite-dimensional states.

The [oscillator examples](../science/oscillator.md) explain the obstruction to such uniform sample guarantees: a very rare population at a very high energy can materially change free energy while being difficult to observe in a finite sample.

## 4. Learning a work target with thermal resources

At fixed finite dimension, the engine uses a small portion of the specimens to estimate the free energy. It combines total energy with a collective measurement of permutation symmetry. The latter, expressed through Schur sectors, estimates the eigenvalues of the state and hence its entropy. It does not require a classical description of the state's eigenvectors.

These two observables commute, and their joint projectors commute with the training Hamiltonian. This matters physically. An unrestricted measurement followed by a freely initialized classical controller would introduce resources absent from the model.

Instead, the training subsystem itself controls the later operation. For its mutually orthogonal outcome projectors $`P_j`$ and predetermined extraction unitaries $`U_j`$, the controlled unitary has the form $`U=\sum_j P_j\otimes U_j`$. Each branch preserves energy. All branch ancillas are appended in their Gibbs states before this operation, and the training subsystem is discarded afterward. Thus the calculation of a statistical outcome corresponds to an energy-conserving control, without a separately initialized pure record.

The training specimens are counted among the $`n`$ inputs and consumed. Their number grows, but their fraction tends to zero.

The [finite-dimensional engine](../science/finite_extraction.md) supplies the remaining ingredient: a single thermal operation that reliably charges a chosen level whenever the unknown input's free energy exceeds a threshold by a fixed margin. Its error is uniform over states in that finite-dimensional class. The proof uses an energy-commuting test, disjoint thermal blocks, and an explicit conversion from a concentrated register state to battery energy. The [universal protocol](../science/universal_protocol.md) selects conservative thresholds from training bins and accounts for every ancillary state.

## 5. Passing from finite to infinite dimension

A naive truncation could reject every specimen outside a finite energy sector. Requiring all specimens to survive such a test would introduce an additional success condition, with an uncontrolled dependence on the source's tail.

The actual cutoff always produces an output. Let $`\Pi_K`$ project onto the first $`K`$ energy eigenvectors, and let $`\tau_K`$ be the Gibbs state of those levels. The channel is

```math
\Phi_K(\rho)=\Pi_K\rho\Pi_K+
\bigl(1-\operatorname{Tr}(\Pi_K\rho)\bigr)\tau_K.
```

It preserves the low-energy block, including its internal coherence, and replaces the remaining population by $`\tau_K`$. An exact thermal implementation appends a $`K`$-level Gibbs ancilla, swaps it with the source on the low-energy sector, acts as the identity on the high-energy sector, and discards the original source. Equal energies are exchanged in each swapped pair.

Two facts make the cutoff useful. First, it maps the full Gibbs state to $`\tau_K`$, so data processing bounds its output relative entropy by $`D(\rho\|\tau)`$. Second, the output and its Gibbs reference approach $`\rho`$ and $`\tau`$ in trace norm. Lower semicontinuity supplies the reverse limiting bound. Nested cutoffs give the stronger monotone recovery

```math
D(\Phi_K(\rho)\|\tau_K)\ \uparrow\ D(\rho\|\tau).
```

The [cutoff proof](../science/thermal_cutoff.md) establishes these statements without a polynomial tail assumption.

The remaining choice is when to increase $`K`$. For each fixed cutoff, uniform finite-dimensional error bounds determine a sufficiently late block length. A source-independent schedule holds that cutoff long enough, then moves to the next. Every fixed source eventually recovers its own relative entropy. No common speed of tail recovery is required, so this argument does not turn pointwise convergence into a uniform finite-sample bound.

## 6. Coherence and work-locking

Section III.A.2–A.4 of the review explains covariance under time translations and work-locking. Its Eqs. (53)–(54) compare the work output from a source with that from its dephased state. For a collective source, the dephasing must use the **total source Hamiltonian**.

For $`n`$ copies this is $`\mathcal D_{H^{(n)}}`$, where $`H^{(n)}`$ is the sum of the copy Hamiltonians. It differs from applying $`\mathcal D_H`$ independently to every copy. The distinction can already be seen in two qubits. Write $`|+\rangle=(|0\rangle+|1\rangle)/\sqrt2`$. The state $`|+\rangle^{\otimes2}`$ has a coherence between $`|01\rangle`$ and $`|10\rangle`$. Those vectors have the same total energy, so total-energy dephasing preserves that coherence. Independent dephasing removes it.

At fixed source dimension $`d`$, the number of distinct total-energy sectors is at most $`(n+1)^d`$: occupation numbers determine total energy, and each occupation count lies between zero and $`n`$. Pinching into these sectors increases entropy by at most the logarithm of their number. The associated free-energy loss per specimen is therefore at most $`d\ln(n+1)/(\beta n)`$, which vanishes.

This reconciles work-locking with the collective rate $`D(\rho\|\tau)/\beta`$. Coherence between distinct total-energy sectors remains locked; its asymptotic cost per specimen vanishes at fixed dimension. Coherence within a sector remains available. The construction does not supply an external phase reference. Its slowly increasing cutoff lets the fixed-dimensional control of errors be used stage by stage. See the [oscillator discussion](../science/oscillator.md) and [finite extraction proof](../science/finite_extraction.md).

## 7. Which outputs converge?

Let $`X_n`$ be the measured battery energy and $`\omega_n(\rho)`$ its state. The full-sequence guarantees are

```math
\mathbb E_\rho\left|X_n/n-f(\rho)\right|\longrightarrow0,
\qquad
S(\omega_n(\rho))\le\ln2+o(1).
```

The first statement controls both work fluctuations at scale $`n`$ and the mean work rate. The second concerns the unnormalized battery entropy. With probability tending to one, the output belongs to at most two neighboring coarse work bins whose energies differ by $`o(n)`$. These need not be adjacent oscillator levels.

A different question asks whether one exact level receives probability tending to one. The protocol alternates between two grids displaced by half a bin. For each fixed source, at least one member of every sufficiently late pair of block lengths is far enough from a bin boundary to have a single likely target. The favorable member can depend on the source. Both processors were nevertheless fixed in advance.

Consequently, the same construction attains the optimal exact-level rate with the ordered criterion $`\lim_{\varepsilon\downarrow0}\limsup_n W_n^\varepsilon/n`$, where $`W_n^\varepsilon`$ is the largest level energy with population at least $`1-\varepsilon`$, with value zero by convention if there is no such level. This limsup statement does not assert a settling exact label at all block lengths.

The [output-boundary proof](../science/output_boundary.md) explains why that stronger universal demand fails on continuous families with a nowhere locally constant rate. A Baire-category argument also forces a battery-entropy limsup of at least $`\ln2`$ on a residual set in a suitable commuting family. Residual means topologically generic, not necessarily positive measure. The lower bound is neither a statement about every source nor about every block length. The paired construction has entropy liminf zero for every source; a strengthened schedule can even have entropy tending to zero for almost every parameter in that family.

The [converse](../science/converse.md) bounds the achievable rate through relative-entropy monotonicity. It includes the fixed initial resource in the ground-state battery, whose contribution divided by $`n`$ vanishes.

## 8. A focused source-reading map

Section labels below follow the pinned v2 PDF. Its HTML version numbers the same lettered subsections, for example I.C as I.3.

| Selected source location | Purpose here | Local continuation |
|---|---|---|
| I.A–C, printed pp. 4–8 | Resource accounting and thermal operations | [Model](../science/model_theorem.md) |
| II.B–C, pp. 11–20 | State conversion and free-energy constraints | [Finite engine](../science/finite_extraction.md), [converse](../science/converse.md) |
| II.C.3, beginning p. 18 | Work extraction and the work bit | Sections 2–3 above |
| III.A.2–A.4, pp. 23–27 | Covariance, free-energy decomposition, work-locking | Section 6 above |

The review supplies the operational and coherence framework. The local work supplies the thermally implemented cutoff, the uniformly controlled finite engine used in the construction, the source-independent schedule, and the distinct rate, entropy, and exact-label conclusions. Its statistical ingredients and coding methods have established antecedents. The [related-work comparison](../references/related_work.md) separates those inherited ideas from the particular physical construction and limit statements; the [source register](../references/source_register.md) records the primary research dependencies.
