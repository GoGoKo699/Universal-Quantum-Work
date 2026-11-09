# Thirty milestones for universal quantum work extraction

This map develops the scientific question: how can one source-independent sequence of thermal operations extract the full free-energy rate from every fixed independent and identically distributed source of finite relative entropy, when the source has an unbounded Hamiltonian? It also explains why reliable work need not settle at one exact battery level at every block length.

## Anchor and source conventions

The single educational anchor is Matteo Lostaglio, **“An introductory review of the resource theory approach to thermodynamics,” arXiv:1807.11549v2, 7 October 2019**, published in *Reports on Progress in Physics* **82**, 114001 (2019). The [versioned source record][L] identifies the selected text. Section references below follow the PDF's lettering, such as §II.C.3 and §III.A.4. These correspond to §II.3.3 and §III.1.4 in the arXiv HTML rendering.

The review supplies the resource-theoretic setting, population transformations, work storage, and coherence constraints. The canonical [science pages](../science/README.md) supply the finite-sample constructions, unbounded-source analysis, universal schedule, and output boundary. A pointer to the review gives the relevant conceptual foundation; it does not attribute the project's additional proof to the review. Primary research dependencies remain identified in the scientific pages.

Throughout the map, $`H`$ is the source Hamiltonian, $`\beta>0`$ is inverse temperature, $`\tau=e^{-\beta H}/Z_\beta`$ is its Gibbs state, and

```math
f(\rho)=\frac{1}{\beta}D(\rho\Vert\tau)
```

is the proposed work rate. The battery has fixed levels $`k\Delta`$, starts in its ground state, and has output energy $`X_n`$ after consuming $`n`$ source copies. Entropies use natural logarithms, so $`\ln 2`$ is one bit of entropy.

## Allocation and dependency structure

**M01–M14 are background/preliminaries; M15–M30 are narrative/innovation.** The fourteen background milestones connect local state descriptions and allowed physical operations to a complete finite-dimensional extraction engine. Its statistical test, purity transfer, and battery conversion are separate understanding targets because each supplies a different physical or mathematical guarantee. M14 integrates them into the inherited capability used by the construction.

The sixteen narrative milestones start with the obstruction caused by an unbounded source, assemble exact compression and universal control, and then establish the work and entropy guarantees. The final part places those guarantees beside the converse, concrete oscillator sources, and the sharp-output obstruction. M30 integrates the complete statement and its scope. The division follows this proof architecture, rather than a fixed ratio between background and results.

Dependencies identify the earlier milestones needed for a conceptual step. The numbered route respects those dependencies, while the table also exposes useful branches: M25 gives the converse, M26–M27 give physical examples and convergence limits, and M28–M29 explain the output entropy boundary. The records describe understanding targets and source routes; the detailed proofs remain in their canonical pages.

## At a glance

| ID | Phase | Central focus | Dependencies |
|---|---|---|---|
| [M01](#m01-states-populations-and-coherence) | Background | States, populations, and coherence | None |
| [M02](#m02-entropy-as-uncertainty-in-a-quantum-state) | Background | Entropy as uncertainty in a quantum state | M01 |
| [M03](#m03-gibbs-states-and-the-bath-temperature) | Background | Gibbs states and the bath temperature | M01, M02 |
| [M04](#m04-channels-discarded-systems-and-physical-dilations) | Background | Channels, discarded systems, and physical dilations | M01 |
| [M05](#m05-thermal-operations-and-their-resource-restrictions) | Background | Thermal operations and their resource restrictions | M03, M04 |
| [M06](#m06-what-a-battery-must-store) | Background | What a battery must store | M02, M05 |
| [M07](#m07-free-energy-as-distance-from-equilibrium) | Background | Free energy as distance from equilibrium | M02, M03, M06 |
| [M08](#m08-resource-order-and-information-monotones) | Background | Resource order and information monotones | M04, M05, M07 |
| [M09](#m09-coherence-under-energy-preserving-control) | Background | Coherence under energy-preserving control | M01, M05 |
| [M10](#m10-independent-copies-and-uniform-statistical-bounds) | Background | Independent copies and uniform statistical bounds | M04, M07 |
| [M11](#m11-reading-spectra-through-collective-symmetry) | Background | Reading spectra through collective symmetry | M04, M09, M10 |
| [M12](#m12-a-test-for-a-free-energy-threshold) | Background | A test for a free-energy threshold | M07, M10, M11 |
| [M13](#m13-purity-from-the-location-of-a-resource) | Background | Purity from the location of a resource | M05, M12 |
| [M14](#m14-a-complete-finite-dimensional-extraction-engine) | Background | A complete finite-dimensional extraction engine | M06, M12, M13 |
| [M15](#m15-why-an-unbounded-source-changes-the-task) | Narrative | Why an unbounded source changes the task | M10, M14 |
| [M16](#m16-replacing-the-tail-by-a-gibbs-state) | Narrative | Replacing the tail by a Gibbs state | M05, M15 |
| [M17](#m17-recovering-relative-entropy-from-finite-cutoffs) | Narrative | Recovering relative entropy from finite cutoffs | M07, M08, M16 |
| [M18](#m18-learning-one-number-from-consumed-specimens) | Narrative | Learning one number from consumed specimens | M10, M11, M17 |
| [M19](#m19-conservative-work-bins-and-finite-labels) | Narrative | Conservative work bins and finite labels | M12, M14, M18 |
| [M20](#m20-compiling-adaptive-choices-into-one-thermal-operation) | Narrative | Compiling adaptive choices into one thermal operation | M05, M13, M18, M19 |
| [M21](#m21-choosing-one-cutoff-schedule-for-every-source) | Narrative | Choosing one cutoff schedule for every source | M14, M17, M19, M20 |
| [M22](#m22-work-concentration-and-mean-work-at-every-block-length) | Narrative | Work concentration and mean work at every block length | M17, M21 |
| [M23](#m23-two-principal-work-levels-and-one-bit-of-entropy) | Narrative | Two principal work levels and one bit of entropy | M19, M21, M22 |
| [M24](#m24-sharp-outputs-along-paired-grids) | Narrative | Sharp outputs along paired grids | M19, M21, M23 |
| [M25](#m25-why-the-rate-is-optimal) | Narrative | Why the rate is optimal | M07, M08, M22, M24 |
| [M26](#m26-coherent-and-finite-energy-oscillator-sources) | Narrative | Coherent and finite-energy oscillator sources | M09, M17, M22, M25 |
| [M27](#m27-slow-tails-and-the-limit-of-uniform-guarantees) | Narrative | Slow tails and the limit of uniform guarantees | M10, M17, M22, M26 |
| [M28](#m28-why-one-exact-label-cannot-settle-for-every-source) | Narrative | Why one exact label cannot settle for every source | M04, M08, M24, M25 |
| [M29](#m29-the-precise-sense-in-which-the-entropy-bit-is-sharp) | Narrative | The precise sense in which the entropy bit is sharp | M09, M23, M24, M28 |
| [M30](#m30-the-complete-universal-work-statement) | Narrative | The complete universal work statement | M14, M17, M20, M22–M29 |

## Background and preliminaries

### M01. States, populations, and coherence

**Phase:** Background/preliminaries.

**Central question:** What information about a quantum source is contained in its energy populations, and what remains in its coherences?

**Understanding target:** Distinguish a density operator, its spectrum, its diagonal in the energy basis, and the Hamiltonian that defines that basis. Recognize that equal populations do not imply equal states or equal thermodynamic resources.

**Dependencies and story role:** No earlier milestone. These objects give the later energy, entropy, and symmetry statements a common language.

**Conceptual connection:** The oscillator example eventually compares a coherent pure state with its Gibbs-distributed populations.

**Source pointers:** Lostaglio [§I.C and §III.A.3][L]; [model and theorem](../science/model_theorem.md), §1; [oscillator examples](../science/oscillator.md), §2, Eqs. O6–O10.

### M02. Entropy as uncertainty in a quantum state

**Phase:** Background/preliminaries.

**Central question:** Which uncertainty does quantum entropy measure, and how does it differ from uncertainty in an energy measurement?

**Understanding target:** Interpret $`S(\rho)=-\operatorname{Tr}\rho\ln\rho`$ through the state's eigenvalues. Distinguish pure-state entropy from the entropy of measured energy populations, and recognize why a mixed battery output requires more description than its mean energy.

**Dependencies and story role:** M01. Entropy connects local state information to the later accounting of free energy and work quality.

**Conceptual connection:** A diagonal battery has matching von Neumann and energy-distribution entropies; a coherent source need not.

**Source pointers:** Lostaglio [§II.B.2 and §III.A.3][L]; [output criteria](../science/model_theorem.md), §4; [oscillator examples](../science/oscillator.md), §§1–2.

### M03. Gibbs states and the bath temperature

**Phase:** Background/preliminaries.

**Central question:** Why does a thermal bath make one particular state free for each Hamiltonian?

**Understanding target:** Relate inverse temperature, energy levels, the partition function, and the Gibbs probabilities. Explain why a zero-Hamiltonian register is free only in its maximally mixed state, and why an unbounded source requires a finite partition function.

**Dependencies and story role:** M01 and M02. The equilibrium reference determines both allowed ancillas and the resource measured later.

**Conceptual connection:** The same temperature governs the source reference, cutoff ancillas, decoder registers, and battery-charging baths.

**Source pointers:** Lostaglio [§I.B–C][L]; [model and theorem](../science/model_theorem.md), §§1–3; [finite extraction](../science/finite_extraction.md), §§3–4.

### M04. Channels, discarded systems, and physical dilations

**Phase:** Background/preliminaries.

**Central question:** How can a reversible interaction produce an irreversible operation on the system that remains?

**Understanding target:** Understand a channel as adjoining an ancilla, applying a joint unitary, and discarding systems. Track which system is retained and why tracing out a control differs from supplying a free measurement record.

**Dependencies and story role:** M01. This supplies the language for every physically implemented channel in the construction.

**Conceptual connection:** Both thermal compression and statistical control use explicit joint operations whose discarded systems carry away information.

**Source pointers:** Lostaglio [§I.C][L]; [thermal compression](../science/thermal_cutoff.md), §2, Proposition C1; [universal protocol](../science/universal_protocol.md), §4, Eqs. U26–U28. The project pages give the concrete dilations.

### M05. Thermal operations and their resource restrictions

**Phase:** Background/preliminaries.

**Central question:** Which physical ingredients are available when extracting work by thermal operations?

**Understanding target:** Assemble finite Gibbs ancillas, energy-preserving unitaries, and discarded systems into the allowed operation. Keep the specified ground-state battery explicit, and distinguish Gibbs preservation, which follows, from an energy-conserving implementation, which must be supplied.

**Dependencies and story role:** M03 and M04. This fixes the physical contract against which all later constructions are checked.

**Conceptual connection:** For unbounded Hamiltonians, commutation with the full time evolution makes energy preservation precise without an informal manipulation of operator domains.

**Source pointers:** Lostaglio [§I.B–C][L]; [model and theorem](../science/model_theorem.md), §§2–3; [thermal compression](../science/thermal_cutoff.md), §2.

### M06. What a battery must store

**Phase:** Background/preliminaries.

**Central question:** What distinguishes useful stored work from a battery that merely has a large mean energy?

**Understanding target:** Compare a successful energy threshold, concentration of energy per source copy, mean work, output entropy, and success at one exact level. Understand why one fixed oscillator with a specified initial ground state makes these criteria comparable across block lengths.

**Dependencies and story role:** M02 and M05. This introduces the operational outputs that the complete theorem must control.

**Conceptual connection:** Lostaglio's work-bit discussion supplies a local work-storage model; the project uses a fixed ladder to compare an entire protocol sequence.

**Source pointers:** Lostaglio [§II.C.3][L]; [model and theorem](../science/model_theorem.md), §§2 and 4.

### M07. Free energy as distance from equilibrium

**Phase:** Background/preliminaries.

**Central question:** Why does relative entropy to the Gibbs state set the thermodynamic work scale?

**Understanding target:** Connect $`D(\rho\Vert\tau)/\beta`$ to the free-energy excess when energy and entropy are finite. Understand why relative entropy remains the primary definition when separate energy and entropy terms could both diverge.

**Dependencies and story role:** M02, M03, and M06. This joins the source description to the rate the battery is supposed to attain.

**Conceptual connection:** The finite-dimensional estimator uses the energy-minus-entropy formula, while the unbounded-source theorem is formulated directly through relative entropy.

**Source pointers:** Lostaglio [§II.C.2 and §III.A.3][L]; [model and theorem](../science/model_theorem.md), §1; [oscillator examples](../science/oscillator.md), §1.

### M08. Resource order and information monotones

**Phase:** Background/preliminaries.

**Central question:** What can a monotone forbid, and what does it leave unproved about a physical transformation?

**Understanding target:** Relate majorization and thermomajorization to state-conversion order, and explain why one free-energy inequality does not characterize all finite-copy transformations. Use data processing to understand a necessary bound without assuming that every Gibbs-preserving map is a thermal operation.

**Dependencies and story role:** M04, M05, and M07. This separates constructive achievability from converse reasoning.

**Conceptual connection:** Data processing controls both the information lost by cutoff and the maximum work entering the battery; explicit dilations establish achievability.

**Source pointers:** Lostaglio [§II.B–C][L]; [thermal compression](../science/thermal_cutoff.md), §§3–4; [converse](../science/converse.md), §1.

### M09. Coherence under energy-preserving control

**Phase:** Background/preliminaries.

**Central question:** How can a protocol use coherent sources without an external phase reference?

**Understanding target:** Connect thermal operations with time-translation covariance. Distinguish dephasing an entire $`n`$-copy source at its total energy from independently dephasing each copy: the former retains coherence inside degenerate total-energy sectors, including $`|01\rangle\langle10|`$.

**Dependencies and story role:** M01 and M05. This resolves the symmetry constraint before introducing collective measurements and extraction.

**Conceptual connection:** The construction uses controls that commute with total energy. Its full asymptotic rate is consistent with the review's work-locking statement applied to the complete physical source.

**Source pointers:** Lostaglio [§III.A.2–4, especially Eqs. 53–54][L]; [finite extraction](../science/finite_extraction.md), §2; [oscillator examples](../science/oscillator.md), §2.

### M10. Independent copies and uniform statistical bounds

**Phase:** Background/preliminaries.

**Central question:** What does having many identical source copies make predictable when the state itself is unknown?

**Understanding target:** Distinguish independent and identically distributed inputs, concentration for a fixed state, and a bound uniform over all states of one fixed finite-dimensional system. Understand why a uniform finite-dimensional estimate does not itself supply a uniform rate over unbounded sources.

**Dependencies and story role:** M04 and M07. This introduces the statistical quantifiers needed by the finite engine and later schedule.

**Conceptual connection:** The review motivates many-copy thermodynamics; the project supplies the explicit error bounds used to choose source-independent stages.

**Source pointers:** Lostaglio [§II.C.2][L]; [finite extraction](../science/finite_extraction.md), §1; [universal protocol](../science/universal_protocol.md), §2.

### M11. Reading spectra through collective symmetry

**Phase:** Background/preliminaries.

**Central question:** How can a collective measurement estimate entropy without knowing the state's eigenbasis?

**Understanding target:** Interpret Schur-sector labels as estimates of the state spectrum, and relate their concentration to entropy continuity. Explain why these projectors commute with the total Hamiltonian and can be combined with an energy measurement.

**Dependencies and story role:** M04, M09, and M10. This turns abstract entropy into information available to an energy-compatible procedure.

**Conceptual connection:** Covariance constrains the controls but still allows collective spectral information; the project provides the Schur-sector argument absent from the introductory review.

**Source pointers:** Lostaglio [§II.B.2 and §III.A.2][L]; [finite extraction](../science/finite_extraction.md), §2.1, Eqs. F16–F21; [universal protocol](../science/universal_protocol.md), §2.

### M12. A test for a free-energy threshold

**Phase:** Background/preliminaries.

**Central question:** How can one energy-compatible test recognize every source above a promised free-energy threshold?

**Understanding target:** Combine energy and spectral-entropy estimates into a commuting projector. Separate its high acceptance probability on every promised source from its exponentially small acceptance probability on the Gibbs state, and explain how a positive margin controls both errors.

**Dependencies and story role:** M07, M10, and M11. This is the statistical engine that distinguishes useful resource from equilibrium.

**Conceptual connection:** Free energy becomes an operational discrimination threshold rather than only a state function; the quantitative test is supplied locally.

**Source pointers:** Lostaglio [§II.C.2 and §III.A.2][L]; [finite extraction](../science/finite_extraction.md), §2, especially Eqs. F22–F29.

### M13. Purity from the location of a resource

**Phase:** Background/preliminaries.

**Central question:** How can identifying a resource block purify a register that began in a Gibbs state?

**Understanding target:** Follow the controlled placement of the unknown source among thermal blocks, the unique-acceptance projectors, and the reversible shift of a maximally mixed register. Explain how false positives and source rejection bound the remaining impurity without an initially pure memory.

**Dependencies and story role:** M05 and M12. This connects statistical distinguishability to a physical resource that can charge a battery.

**Conceptual connection:** The review supplies the resource-theory rules; the position-decoding construction supplies an explicit energy-conserving realization with all registers accounted for.

**Source pointers:** Lostaglio [§I.C and §II.C.3][L]; [finite extraction](../science/finite_extraction.md), §3, Eqs. F30–F37, and §6 for attribution.

### M14. A complete finite-dimensional extraction engine

**Phase:** Background/preliminaries.

**Central question:** What complete work-extraction capability is available before treating an unbounded, unknown source?

**Understanding target:** Integrate the threshold test, register purification, and finite-bath sector swap. State the resulting promise: one operation charges the ground-start ladder to $`\Delta\lfloor\ell r/\Delta\rfloor`$ with vanishing error uniformly over finite-dimensional states satisfying $`f\ge r+s`$, with output supported on ground and target levels.

**Dependencies and story role:** M06, M12, and M13. This is the background capstone and the construction's inherited interface.

**Conceptual connection:** All auxiliary systems begin in Gibbs states; finiteness at each stage entails no practical bound on their size.

**Source pointers:** Lostaglio [§I.C and §II.C.3][L]; [finite extraction](../science/finite_extraction.md), Lemma F1 and §§4–6, especially Eq. F49.

## Narrative and innovation

### M15. Why an unbounded source changes the task

**Phase:** Narrative/innovation.

**Central question:** Why does a finite-dimensional extraction theorem not immediately solve the unknown-source problem?

**Understanding target:** Identify the unknown high-energy tail and distinguish a fixed cutoff from a cutoff schedule. Explain why demanding that every copy lie below one cutoff can make success vanish, even when each individual copy has high probability of being retained.

**Dependencies and story role:** M10 and M14. This identifies the first missing mechanism between the background engine and the universal theorem.

**Conceptual connection:** The review's finite-dimensional setting supplies the starting point; the project must handle finite relative entropy without an assumed tail rate.

**Source pointers:** Lostaglio [Introduction, “Scope,” and §II.C.2][L]; [model and theorem](../science/model_theorem.md), §§1 and 5; [thermal compression](../science/thermal_cutoff.md), §§1 and 5.

### M16. Replacing the tail by a Gibbs state

**Phase:** Narrative/innovation.

**Central question:** How can every source copy enter a finite-dimensional protocol without conditioning on a rare collective event?

**Understanding target:** Understand the channel $`\Phi_K(\rho)=\Pi_K\rho\Pi_K+\operatorname{Tr}(Q_K\rho)\tau_K`$, where $`\Pi_K`$ projects onto the first $`K`$ energy eigenvectors and $`Q_K=I-\Pi_K`$. Follow its conditional-swap implementation, identify the retained ancilla, and explain why low-energy coherence survives while tail information is discarded without postselection.

**Dependencies and story role:** M05 and M15. This supplies the exact physical reduction on which the remaining construction rests.

**Conceptual connection:** A finite Gibbs ancilla implements the cutoff through an energy-conserving unitary. Strong commutation with time evolution also settles the unbounded-operator domain issue.

**Source pointers:** Lostaglio [§I.C and §III.A.2][L]; [thermal compression](../science/thermal_cutoff.md), §§1–2, Proposition C1 and Eqs. C1–C4.

### M17. Recovering relative entropy from finite cutoffs

**Phase:** Narrative/innovation.

**Central question:** Why does replacing a tail by thermal noise eventually preserve the entire free-energy rate?

**Understanding target:** Connect Gibbs preservation, nested cutoff channels, trace-norm convergence, and lower semicontinuity. Explain why $`D(\Phi_K(\rho)\Vert\tau_K)`$ increases to $`D(\rho\Vert\tau)`$ even without a quantitative convergence rate or separate finite energy and entropy assumptions.

**Dependencies and story role:** M07, M08, and M16. This converts the physical cutoff into a mathematically sufficient approximation.

**Conceptual connection:** Data processing bounds every finite cutoff from above; lower semicontinuity closes the limit from below. The monotone limit is the new bridge to the inherited finite engine.

**Source pointers:** Lostaglio [§II.C.2][L]; [thermal compression](../science/thermal_cutoff.md), §§3–5, Proposition C2 and Eqs. C5–C10.

### M18. Learning one number from consumed specimens

**Phase:** Narrative/innovation.

**Central question:** What must a universal extractor learn about its unknown input before choosing a work target?

**Understanding target:** Explain why estimating the scalar cutoff free energy is sufficient. Follow the use of $`m_n=\lfloor\sqrt n\rfloor`$ training copies, joint energy and Schur labels, clipping to the known finite range, and a state-uniform estimation error bound at fixed cutoff.

**Dependencies and story role:** M10, M11, and M17. This supplies target information while consuming a vanishing fraction of the available source.

**Conceptual connection:** Energy-commuting training projectors make the eventual choice compatible with thermal operations; training copies are included in the resource count.

**Source pointers:** Lostaglio [§II.C.2 and §III.A.2][L]; [universal protocol](../science/universal_protocol.md), §2, Eqs. U3–U13.

### M19. Conservative work bins and finite labels

**Phase:** Narrative/innovation.

**Central question:** How can an imperfect free-energy estimate select a work value that the extraction engine can safely supply?

**Understanding target:** Relate grid width $`a_K`$, estimation tolerance $`s_K`$, and the conservative target $`r=\max\{0,b-4s_K\}`$. Explain the resulting extraction margin, oscillator-level rounding, and finite output alphabet. An accurate estimate can reach at most two neighboring coarse bins.

**Dependencies and story role:** M12, M14, and M18. This connects statistical information to an implementable battery command.

**Conceptual connection:** The work-bit perspective becomes a family of fixed-ladder targets; conservative margins make the finite threshold promise applicable to every correct branch.

**Source pointers:** Lostaglio [§II.C.3][L]; [universal protocol](../science/universal_protocol.md), §3, Eqs. U14–U25.

### M20. Compiling adaptive choices into one thermal operation

**Phase:** Narrative/innovation.

**Central question:** How can a protocol act on a statistical outcome without treating measurement and classical feedback as free external resources?

**Understanding target:** Assemble orthogonal training projectors, predetermined Gibbs baths for all branches, and controlled extraction unitaries into one energy-conserving unitary. Explain why discarding the training block yields the required branch mixture and why shared battery ground states cause no conflict.

**Dependencies and story role:** M05, M13, M18, and M19. This closes the physical implementation of the statistical strategy.

**Conceptual connection:** The channel-dilation viewpoint turns adaptive language into a single allowed operation, with no additional pure record or coherent controller.

**Source pointers:** Lostaglio [§I.C and §III.A.2][L]; [universal protocol](../science/universal_protocol.md), §4, Eqs. U26–U28; [finite extraction](../science/finite_extraction.md), §5.

### M21. Choosing one cutoff schedule for every source

**Phase:** Narrative/innovation.

**Central question:** How can one deterministic schedule serve every source when its tail convergence rate is unknown?

**Understanding target:** Separate state-uniform error bounds at fixed $`K`$ from pointwise convergence as $`K`$ increases. Explain how even stage thresholds $`N_K`$ control extraction error, training loss, rounding, and the finite-alphabet entropy contribution while keeping $`K(n)`$ constant on adjacent even-odd pairs.

**Dependencies and story role:** M14, M17, M19, and M20. This integrates the local constructions into a common source-independent sequence.

**Conceptual connection:** Slow diagonalization uses known finite-stage bounds; it never estimates or assumes a rate for the source's high-energy tail.

**Source pointers:** Lostaglio [§II.C.2][L], for many-copy context; [universal protocol](../science/universal_protocol.md), §5, Eqs. U29–U37 and the explicit envelope U31a.

### M22. Work concentration and mean work at every block length

**Phase:** Narrative/innovation.

**Central question:** How do the cutoff, training, and extraction errors combine into the full work-rate guarantee?

**Understanding target:** Follow the bound on $`\mathbb E|X_n/n-f(\rho)|`$. Separate the source-dependent cutoff loss from grid, training, rounding, and failure contributions. Explain why their convergence gives both probability concentration and convergence of mean work along every sufficiently large integer block length.

**Dependencies and story role:** M17 and M21. This is the principal achievability statement obtained from the assembled protocol.

**Conceptual connection:** The relative-entropy rate becomes operationally attainable for each fixed source, although the point at which a specified accuracy is reached may depend on that source.

**Source pointers:** Lostaglio [§II.C.2–3][L]; [universal protocol](../science/universal_protocol.md), §6, Eqs. U38–U40; [model and theorem](../science/model_theorem.md), Theorem M1.

### M23. Two principal work levels and one bit of entropy

**Phase:** Narrative/innovation.

**Central question:** Why can a universal extractor have a sharply concentrated work rate while retaining a bounded ambiguity in exact output energy?

**Understanding target:** Derive the two-bin concentration from the short estimation interval, then account for failures across the full finite alphabet. Explain why their contribution vanishes and the battery entropy is at most $`\ln 2+o(1)`$, with two principal work levels separated by $`o(n)`$.

**Dependencies and story role:** M19, M21, and M22. This adds work quality to the rate guarantee.

**Conceptual connection:** The two levels belong to the coarse work grid and need not be adjacent oscillator rungs. The entropy bound is about the battery output.

**Source pointers:** Lostaglio [§II.C.3][L]; [universal protocol](../science/universal_protocol.md), §7, Eqs. U41–U43.

### M24. Sharp outputs along paired grids

**Phase:** Narrative/innovation.

**Central question:** How can the same universal protocol also attain an exact-level success criterion?

**Understanding target:** Explain why two grids displaced by half a bin cannot both place a fixed cutoff free energy near a boundary. With the cutoff unchanged across a pair, at least one member has one dominant output level. Its probability tends to one and its work per copy tends to the optimal rate.

**Dependencies and story role:** M19, M21, and M23. This connects the all-integer protocol to an exact-level limsup definition.

**Conceptual connection:** The favorable member may depend on the source. The conclusion concerns a subsequence, while rate concentration holds throughout the sequence.

**Source pointers:** Lostaglio [§II.C.3][L]; [universal protocol](../science/universal_protocol.md), §8, Eqs. U44–U46; [output criteria](../science/model_theorem.md), §4.

### M25. Why the rate is optimal

**Phase:** Narrative/innovation.

**Central question:** What prevents another allowed extractor from reliably charging the battery faster?

**Understanding target:** Follow the relative-entropy budget from Gibbs preservation to the battery, including the fixed ground state's finite initial contribution. Apply a binary energy-threshold measurement and the oscillator's Gibbs tail to bound reliable work. Recognize the resulting weak converse and its exact-label consequence.

**Dependencies and story role:** M07, M08, M22, and M24. This matches the constructive rate with an operational upper bound.

**Conceptual connection:** The argument uses finite relative entropy directly, avoiding subtraction of infinite energy and entropy. It does not assert a strong converse above the rate.

**Source pointers:** Lostaglio [§II.C.2–3][L]; [converse](../science/converse.md), §§1–3, Eqs. V1–V11.

### M26. Coherent and finite-energy oscillator sources

**Phase:** Narrative/innovation.

**Central question:** What does the theorem predict for concrete bosonic sources with familiar energy statistics?

**Understanding target:** Explain why finite mean oscillator energy implies finite entropy and a finite thermodynamic rate. Compare a coherent geometric superposition with a Gibbs state having the same energy populations, and track the coherence retained inside a cutoff.

**Dependencies and story role:** M09, M17, M22, and M25. These examples connect the abstract theorem to visible physical distinctions.

**Conceptual connection:** Dephasing the whole multi-copy source preserves equal-total-energy coherence; dephasing copies separately can destroy the resource. The example therefore respects the review's covariance and work-locking constraints.

**Source pointers:** Lostaglio [§III.A.2–4][L]; [oscillator examples](../science/oscillator.md), §§1–2, Eqs. O1–O10.

### M27. Slow tails and the limit of uniform guarantees

**Phase:** Narrative/innovation.

**Central question:** How slowly can a permitted source approach its asymptotic rate, and why can a mean-energy bound fail to give a common sample guarantee?

**Understanding target:** Connect a finite-energy tail proportional to $`1/[j^2\ln^2(j+1)]`$ with logarithmically slow cutoff recovery. Then distinguish it from the rare-high-energy construction, which makes fixed-sample inputs nearly indistinguishable while their target rates remain separated.

**Dependencies and story role:** M10, M17, M22, and M26. This identifies the practical content of pointwise convergence.

**Conceptual connection:** The universal schedule works for each fixed source; a uniform rate over all sources with a bounded mean energy is a stronger claim and fails here.

**Source pointers:** Lostaglio [§II.C.2][L], for asymptotic context; [oscillator examples](../science/oscillator.md), §§3–4, Eqs. O11–O21.

### M28. Why one exact label cannot settle for every source

**Phase:** Narrative/innovation.

**Central question:** Why can no universal, rate-consistent extractor select one almost-certain exact energy label at every late block length for every source?

**Understanding target:** Connect continuity of finite experiments, continuity of the largest output probability on a countable alphabet, and local constancy of a label whose probability exceeds one half. Explain how the Baire argument conflicts with a continuously varying, locally nonconstant target rate.

**Dependencies and story role:** M04, M08, M24, and M25. This identifies the obstruction that rate optimality alone does not reveal.

**Conceptual connection:** A commuting qubit family makes the statistical obstruction physical; the canonical page attributes its canonical-estimation antecedents.

**Source pointers:** Lostaglio [§II.C.3][L], for work-output context; [output boundary](../science/output_boundary.md), §§1–4, Theorems 1–2, and §7.

### M29. The precise sense in which the entropy bit is sharp

**Phase:** Narrative/innovation.

**Central question:** Which unavoidable entropy cost matches the construction's one-bit upper bound?

**Understanding target:** Combine covariance for stationary inputs with the residual largest-atom obstruction to obtain a residual set of sources with entropy limsup at least $`\ln 2`$. Reconcile equality for the construction with entropy liminf zero, possible privileged sources, and the distinction between residual sets and sets of full measure.

**Dependencies and story role:** M09, M23, M24, and M28. This integrates the output construction and its converse with exact quantifiers.

**Conceptual connection:** The bit quantifies battery-output ambiguity. It is neither a per-source persistent entropy floor nor a one-bit loss of extracted work.

**Source pointers:** Lostaglio [§III.A.2][L]; [output boundary](../science/output_boundary.md), §§3–6; [universal protocol](../science/universal_protocol.md), §§7–8.

### M30. The complete universal work statement

**Phase:** Narrative/innovation.

**Central question:** What has been established for one fixed physical model, and which distinctions are essential to its meaning?

**Understanding target:** Assemble the finite-relative-entropy source domain, ground-start oscillator, common thermal-operation sequence, all-integer work and mean convergence, two-level concentration, entropy bound, and exact-level limsup. Distinguish inherited finite-dimensional extraction from the compression and scheduling that extend it, and keep the efficiency and uniformity limits visible.

**Dependencies and story role:** M14, M17, M20, and M22–M29. This is the narrative capstone, joining construction, optimality, examples, and output limits.

**Conceptual connection:** The review's resource-theoretic framework becomes a precise universal extraction statement with explicit ancillary resources and quantified work quality.

**Source pointers:** Lostaglio [§I.C, §II.C.2–3, and §III.A.2–4][L]; [model and theorem](../science/model_theorem.md), Theorem M1 and §6; [scientific route](../science/README.md).

[L]: https://arxiv.org/abs/1807.11549v2
