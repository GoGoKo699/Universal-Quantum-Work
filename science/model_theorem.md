# Model and universal extraction theorem

An engine receives $n$ specimens of an unknown quantum state, together with a battery in a fixed ground state. The source Hamiltonian and bath temperature are known. The engine may use Gibbs ancillas and energy-conserving unitaries, and its description must be chosen independently of the source state.

For a source with finite relative entropy to its Gibbs state, the construction below extracts the full relative-entropy work rate along every block length in probability and in mean. Its battery entropy is at most one bit asymptotically. The same sequence also attains the optimal exact-level rate when that rate is defined by a limsup over block lengths.

## 1. Source and temperature

Let $\mathcal H$ be a separable infinite-dimensional Hilbert space with a specified orthonormal energy basis. The known source Hamiltonian is

$$
H=\sum_{i=1}^{\infty}E_i|i\rangle\langle i|,
\qquad
0=E_1\le E_2\le\cdots,
\qquad
Z_\beta=\operatorname{Tr}e^{-\beta H}<\infty,
\tag{M1}
$$

for a fixed inverse temperature $\beta>0$. A constant energy shift has been used to put the ground energy at zero. The operator is self-adjoint on its natural domain. The finite partition function implies finite multiplicity below every finite energy and $E_i\to\infty$.

Write

$$
\tau=\frac{e^{-\beta H}}{Z_\beta},
\qquad
\mathcal S_D=
\{\rho\in\mathcal D(\mathcal H):D(\rho\|\tau)<\infty\},
\qquad
f(\rho)=\frac1\beta D(\rho\|\tau).
\tag{M2}
$$

All logarithms are natural. Relative entropy is understood in its standard extended-valued form for density operators on a separable Hilbert space. In particular, its definition is not an unevaluated subtraction of two infinite entropies.

When the source has finite mean energy, its entropy is finite and

$$
f(\rho)
=\operatorname{Tr}(H\rho)-\frac{S(\rho)}\beta
 +\frac{\ln Z_\beta}\beta.
\tag{M3}
$$

Finiteness follows from the Gibbs variational bound $S(\rho)\le\beta\operatorname{Tr}(H\rho)+\ln Z_\beta$. The theorem itself assumes only finite $D(\rho\|\tau)$, so that it also covers Hamiltonians and states for which the energy and entropy terms in (M3) are separately infinite. The relative-entropy formulation remains well defined in that case.

The input at block length $n$ is $\rho^{\otimes n}$ for one fixed but unknown $\rho$. The processor receives no classical description of $\rho$, candidate list, energy ceiling, or tail bound. The Hamiltonian, temperature, and integer $n$ remain available to its designer.

## 2. One fixed oscillator battery

Choose any fixed gap $\Delta>0$. The work storage system is

$$
\mathcal H_W=\ell^2(\mathbb N_0),
\qquad
H_W=\Delta\sum_{k=0}^{\infty}k|k\rangle\langle k|.
\tag{M4}
$$

It starts each block in $|0\rangle\langle0|$. The battery Hilbert space and Hamiltonian are the same for every $n$ and every source. Its Gibbs state is

$$
\tau_W=\frac{e^{-\beta H_W}}{Z_W},
\qquad
Z_W=\frac1{1-e^{-\beta\Delta}}.
\tag{M5}
$$

Only finitely many battery levels are used at any particular block length. There is no dimension bound on the union of those levels as $n$ increases. The specified ground state is the initial work-storage resource, not an uncounted auxiliary pure state.

## 3. Allowed thermal operations

For each $n$, the processor appends a finite-dimensional ancillary system $B_n$ with a specified Hamiltonian $G_n$ and Gibbs state

$$
\gamma_n=\frac{e^{-\beta G_n}}{\operatorname{Tr}e^{-\beta G_n}}.
$$

A product of finitely many finite Gibbs ancillas is included in this notation. It applies a unitary $U_n$ on source, battery, and ancilla, and discards everything except the battery:

$$
\mathcal T_n(X)
=\operatorname{Tr}_{S^nB_n}
\left[U_n(X\otimes\gamma_n)U_n^\dagger\right].
\tag{M6}
$$

The unitary preserves total energy in the strong sense

$$
U_ne^{-itH_{\mathrm{tot},n}}
=e^{-itH_{\mathrm{tot},n}}U_n
\qquad(t\in\mathbb R),
\tag{M7}
$$

where

$$
H_{\mathrm{tot},n}=\sum_{j=1}^nH^{(j)}+H_W+G_n.
$$

This definition is meaningful for the unbounded source and battery Hamiltonians. It implies preservation of their operator domains and commutation with the total Hamiltonian on its domain.

The sequence $\{\mathcal T_n\}$ may depend on $H$, $\beta$, $\Delta$, and $n$. It is independent of $\rho$. Its ancillas are all Gibbs initialized, and the construction uses no catalyst, external phase reference, additional pure memory, or initial work loan. The $o(n)$ specimens used for training are part of the $n$ input specimens and are consumed.

The model permits arbitrary global energy-conserving interactions and finite baths of arbitrarily large dimension. It imposes no running-time, locality, gate-complexity, or bath-energy bound.

## 4. Output criteria

For a source $\rho$, denote the battery state by

$$
\omega_n(\rho)
=\mathcal T_n\!\left(
\rho^{\otimes n}\otimes|0\rangle\langle0|
\right).
\tag{M8}
$$

Let $X_n$ be its energy measurement outcome:

$$
\Pr_\rho[X_n=k\Delta]
=\langle k|\omega_n(\rho)|k\rangle.
\tag{M9}
$$

Since the initial energy is zero, $X_n$ is the battery's energy increase. A full-sequence work-rate criterion requires $X_n/n$ to concentrate at the claimed rate for every sufficiently large block length.

For comparison with an exact-level criterion, fix $0<\varepsilon<1/2$ and define

$$
\mathcal W_n^\varepsilon(\rho)
=\max\!\left(
\{0\}\cup
\left\{k\Delta:
\langle k|\omega_n(\rho)|k\rangle\ge1-\varepsilon
\right\}
\right).
\tag{M10}
$$

The value is conventionally zero if no level has the required population; in that case it does not certify concentration at the ground level. Since $1-\varepsilon>1/2$, at most one nonzero level can qualify. An exact pure-level fidelity criterion gives the same asymptotic expression below, whether fidelity denotes the squared overlap or its square root, after reparameterizing $\varepsilon$.

## 5. Universal extraction theorem

**Theorem M1.** Under (M1), for every fixed $\beta>0$ and $\Delta>0$ there exists one sequence of thermal operations of the form (M6) with the following properties for every $\rho\in\mathcal S_D$.

**Full-sequence work rate.** The battery energy converges in normalized mean absolute deviation:

$$
\lim_{n\to\infty}
\mathbb E_\rho\left|
\frac{X_n}{n}-f(\rho)
\right|=0.
\tag{M11}
$$

In particular,

$$
\frac{X_n}{n}\xrightarrow{\Pr}f(\rho),
\qquad
\frac{\operatorname{Tr}(H_W\omega_n(\rho))}{n}
\longrightarrow f(\rho).
\tag{M12}
$$

**A finite alphabet and two principal levels.** At each $n$, the output is diagonal and supported on a finite set $\mathcal A_n\subset\Delta\mathbb N_0$ fixed independently of the source. There are source-independent sequences $\delta_n,\xi_n\to0$ such that, for each source, a subset $\mathcal B_{n,\rho}\subset\mathcal A_n$ satisfies

$$
|\mathcal B_{n,\rho}|\le2,
\qquad
\Pr_\rho[X_n\in\mathcal B_{n,\rho}]\ge1-\delta_n,
\qquad
\operatorname{diam}(\mathcal B_{n,\rho})\le n\xi_n.
\tag{M13}
$$

The two values are neighboring values of a coarse work grid. They need not be adjacent oscillator levels.

**Battery entropy.** There is a source-independent sequence $u_n\to0$ with

$$
S(\omega_n(\rho))\le\ln2+u_n.
\tag{M14}
$$

Thus the output entropy is at most one bit asymptotically, including the contribution of the low-probability labels outside $\mathcal B_{n,\rho}$.

**Exact-level subsequence and limsup.** For each source, at least one member of every sufficiently late pair $(2t,2t+1)$ has an exact battery level whose population tends to one and whose energy divided by that block length tends to $f(\rho)$. Consequently,

$$
\lim_{\varepsilon\downarrow0}
\limsup_{n\to\infty}
\frac{\mathcal W_n^\varepsilon(\rho)}n
=\frac{D(\rho\|\tau)}\beta.
\tag{M15}
$$

The favorable member of each pair may depend on $\rho$. All operations, grids, and stage boundaries are fixed independently of $\rho$.

### Proof and dependencies

The [thermal compression theorem](thermal_cutoff.md) gives an exact thermal operation $\Phi_K$ with

$$
\Phi_K(\tau)=\tau_K,
\qquad
\frac1\beta D(\Phi_K(\rho)\|\tau_K)
\uparrow f(\rho).
\tag{M16}
$$

The [finite extraction primitive](finite_extraction.md) supplies a state-uniform, fixed-threshold extractor on each finite cutoff system. The [universal protocol](universal_protocol.md) combines that primitive with energy-commuting training, conservative scalar work bins, and a source-independent sequence of even stage boundaries. Its finite-stage bounds prove (M11)–(M14) and the subsequence lower bound in (M15).

For the matching upper bound, every thermal operation in this model preserves the Gibbs state and therefore obeys

$$
D(\omega_n(\rho)\|\tau_W)
\le nD(\rho\|\tau)+\ln Z_W.
\tag{M17}
$$

Binary data processing for the population of a claimed work level bounds its energy at any fixed success probability. Taking the block-length limsup and then $\varepsilon\downarrow0$ gives the upper bound in (M15). The complete argument, including the threshold and mean-work formulations, is in the [converse](converse.md). $\square$

## 6. Physical content and scope

For a harmonic oscillator source, every finite-mean-energy state belongs to $\mathcal S_D$. The theorem therefore applies to arbitrary mixed or coherent oscillator states with finite energy, without a supplied energy bound or decay envelope. A source with infinite mean energy is included only when its relative entropy in (M2) is finite; no difference of infinite energy and entropy is used to state its rate.

The entropy control also identifies the rate as stored thermodynamic free energy. Since every output has finite support,

$$
\frac{
D(\omega_n(\rho)\|\tau_W)
-D(|0\rangle\langle0|\|\tau_W)
}{\beta n}
=\frac{\operatorname{Tr}(H_W\omega_n(\rho))}{n}
 -\frac{S(\omega_n(\rho))}{\beta n}
\longrightarrow f(\rho).
\tag{M18}
$$

The one-bit bound concerns the battery's entropy. It does not say that the finite-block work deficit is at most $\beta^{-1}\ln2$: the cutoff, training, and conservative grid losses can be larger while remaining sublinear in $n$.

All convergence statements for the work rate are pointwise in the fixed source. The same processor sequence works for every source, but the block length needed for a prescribed work-rate accuracy can depend on that source through the convergence in (M16). The [nonuniformity argument](oscillator.md#4-why-an-energy-bound-does-not-give-a-uniform-sample-guarantee) separates this statement from a uniform finite-sample guarantee over a family specified only by a mean-energy bound.

The exact-level limsup in (M15) is the operational type used by [Watanabe and Takagi](https://pmc.ncbi.nlm.nih.gov/articles/PMC12957447/). Their infinite-dimensional theorem treats a finite candidate set under an additional diagonal-tail condition. The present construction supplies a common sequence for the entire finite-relative-entropy class, while (M11)–(M14) specify its behavior along all block lengths. If their source-generated work-spectrum convention is imposed, choose $\Delta$ to be a positive difference of two source energy eigenvalues. Then the oscillator levels used here lie in that allowed spectrum; for an oscillator source, its own energy spacing is a direct choice.

The finite-dimensional testing, spectrum estimation, and position-decoding methods are inherited ingredients. Their precise role and attribution are recorded in [finite extraction](finite_extraction.md). The finite-dimensional result is combined here with an exact thermal cutoff, a slow state-independent schedule, and paired work grids. No finite-size or efficiency bound uniform in the source is inferred from this combination.
