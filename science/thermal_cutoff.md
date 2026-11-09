# Thermal compression without tail postselection

A finite-dimensional extractor can process an unbounded source if each source specimen is first converted to a finite system by a thermal operation. The conversion below replaces the population outside a chosen energy sector by the Gibbs state of that sector. It never rejects a specimen. Its relative-entropy loss vanishes as the sector grows, even when no tail bound is supplied.

The [model and theorem](model_theorem.md) fix the source Hamiltonian and the thermal-operation convention. The [universal protocol](universal_protocol.md) uses this compression independently on every input specimen.

## 1. The channel

Let

```math
H=\sum_{i=1}^{\infty}E_i|i\rangle\langle i|,
\qquad
0=E_1\le E_2\le\cdots,
\qquad
Z_\beta=\sum_i e^{-\beta E_i}<\infty.
```

The vectors form a complete orthonormal basis, and $`H`$ denotes the self-adjoint diagonal operator with its natural domain. Fix a finite integer $`K`$. Write

```math
\Pi_K=\sum_{i=1}^K|i\rangle\langle i|,
\qquad
Q_K=I-\Pi_K,
\qquad
\mathcal H_K=\Pi_K\mathcal H,
```

```math
H_K=H|_{\mathcal H_K},
\qquad
Z_K=\sum_{i=1}^K e^{-\beta E_i},
\qquad
\tau_K=\frac{e^{-\beta H_K}}{Z_K}.
```

The output of the compression is a state on $`\mathcal H_K`$. For any trace-class input operator $`X`$, define

```math
\Phi_K(X)
=\Pi_KX\Pi_K+\operatorname{Tr}(Q_KX)\tau_K.
\tag{C1}
```

The first term is identified with an operator on $`\mathcal H_K`$. In particular, for a state $`\rho`$,

```math
\Phi_K(\rho)
=\Pi_K\rho\Pi_K+
\bigl(1-\operatorname{Tr}(\Pi_K\rho)\bigr)\tau_K.
\tag{C2}
```

The retained block preserves all coherences within the first $`K`$ energy eigenvectors. Coherences between that block and its complement are discarded. The population of the complement becomes a Gibbs contribution.

## 2. An exact energy-conserving implementation

**Proposition C1.** The map $`\Phi_K`$ is a thermal operation from $`(\mathcal H,H)`$ to $`(\mathcal H_K,H_K)`$. It uses one finite Gibbs ancilla and no work storage, pure auxiliary state, or conditional acceptance.

**Proof.** Append a $`K`$-dimensional ancilla $`A`$ with Hamiltonian $`H_K`$ and initial state $`\tau_K`$. On the source and ancilla basis, define

```math
U_K\bigl(|i\rangle_S|j\rangle_A\bigr)=
\begin{cases}
|j\rangle_S|i\rangle_A,&1\le i\le K,\ 1\le j\le K,\\
|i\rangle_S|j\rangle_A,&i>K,\ 1\le j\le K.
\end{cases}
\tag{C3}
```

This is a permutation of the complete product basis and satisfies $`U_K^2=I`$. It is therefore a bounded unitary. On the first block, the two systems have identical energy lists, so swapping them preserves the energy $`E_i+E_j`$. On the second block the unitary is the identity.

This basis description also resolves the domain issue associated with unbounded $`H`$. Let

```math
H_{SA}=H\otimes I_A+I_S\otimes H_K.
```

Equation (C3) gives

```math
U_Ke^{-itH_{SA}}=e^{-itH_{SA}}U_K
\qquad(t\in\mathbb R).
\tag{C4}
```

Thus $`U_K`$ commutes with every spectral projection of $`H_{SA}`$, maps its domain onto itself, and satisfies $`U_KH_{SA}=H_{SA}U_K`$ on that domain. Energy conservation is meant in this strong sense, rather than as a formal commutator of unbounded operators.

To compute the reduced output on $`A`$, decompose $`\rho`$ into its $`\Pi_K`$ and $`Q_K`$ blocks. The low-energy block transforms as

```math
U_K\bigl(\Pi_K\rho\Pi_K\otimes\tau_K\bigr)U_K^\dagger
=\tau_K\otimes\Pi_K\rho\Pi_K.
```

The high-energy block remains $`Q_K\rho Q_K\otimes\tau_K`$. The two off-diagonal blocks still have source support between orthogonal low- and high-energy sectors after applying $`U_K`$, so their partial traces over the source vanish. Discarding the old source therefore gives

```math
\operatorname{Tr}_S\!\left[
U_K(\rho\otimes\tau_K)U_K^\dagger
\right]
=\Pi_K\rho\Pi_K+\operatorname{Tr}(Q_K\rho)\tau_K.
```

The appended Gibbs ancilla is the output system. This proves (C1) and its thermal implementation. $`\square`$

Discarding the old source is part of the operation. Its entire input resource remains charged to the protocol. There is no measurement outcome whose preparation or reset has been omitted.

## 3. Gibbs preservation and nesting

Let $`\tau=e^{-\beta H}/Z_\beta`$. Since

```math
\Pi_K\tau\Pi_K=\frac{Z_K}{Z_\beta}\tau_K,
```

the channel satisfies

```math
\Phi_K(\tau)=\tau_K.
\tag{C5}
```

The family is also consistent across cutoffs. For $`K\le L`$, let $`\Phi_{K\leftarrow L}`$ be (C1) with input space $`\mathcal H_L`$, input Hamiltonian $`H_L`$, and output Gibbs state $`\tau_K`$. The same conditional-swap construction makes it a finite-dimensional thermal operation. It satisfies

```math
\Phi_{K\leftarrow L}(\tau_L)=\tau_K,
\qquad
\Phi_{K\leftarrow L}\circ\Phi_L=\Phi_K.
\tag{C6}
```

For the second identity, set $`t_J=\operatorname{Tr}(\Pi_J\rho)`$. Linearity of (C1) gives

```math
\Phi_{K\leftarrow L}(\Pi_L\rho\Pi_L)
=\Pi_K\rho\Pi_K+(t_L-t_K)\tau_K,
```

while the remaining term $`(1-t_L)\tau_L`$ becomes $`(1-t_L)\tau_K`$. Their sum is (C2).

Consequently, data processing for quantum relative entropy gives

```math
D\bigl(\Phi_K(\rho)\|\tau_K\bigr)
\le
D\bigl(\Phi_L(\rho)\|\tau_L\bigr)
\le D(\rho\|\tau).
\tag{C7}
```

Data processing and joint lower semicontinuity are standard properties of relative entropy on separable Hilbert spaces. The form used here, including infinite values and trace-norm convergence, is stated in Shirokov's discussion of these properties in [2024, §1](https://www.mathnet.ru/php/archive.phtml?jrnid=sm&option_lang=eng&paperid=10107&wshow=paper); see also [2022, equations (1.1) and (3.1)](https://doi.org/10.4213/sm9794e).

## 4. Relative entropy converges from below

For this argument, embed the output state $`\Phi_K(\rho)`$ and $`\tau_K`$ back into $`\mathcal H`$ by extending them by zero outside $`\mathcal H_K`$. This mathematical embedding is used to compare trace norms. It is not an additional physical operation.

**Proposition C2.** For every density operator $`\rho`$ on $`\mathcal H`$,

```math
D\bigl(\Phi_K(\rho)\|\tau_K\bigr)
\uparrow D(\rho\|\tau)
\qquad(K\to\infty),
\tag{C8}
```

where the limit may be $`+\infty`$.

**Proof.** Put $`\delta_K=\operatorname{Tr}(Q_K\rho)`$. Strong convergence $`\Pi_K\to I`$ and trace-classness of $`\rho`$ imply $`\delta_K\to0`$. The decomposition

```math
\rho-\Pi_K\rho\Pi_K
=Q_K\rho+\Pi_K\rho Q_K
```

and the Schatten Cauchy–Schwarz inequality give

```math
\|Q_K\rho\|_1
\le\|Q_K\sqrt\rho\|_2\|\sqrt\rho\|_2
=\sqrt{\delta_K},
```

```math
\|\Pi_K\rho Q_K\|_1
\le\|\Pi_K\sqrt\rho\|_2\|\sqrt\rho Q_K\|_2
\le\sqrt{\delta_K}.
```

Hence

```math
\|\Phi_K(\rho)-\rho\|_1
\le2\sqrt{\delta_K}+\delta_K
\longrightarrow0.
\tag{C9}
```

For the Gibbs state, orthogonality of the retained and discarded sectors gives the exact identity

```math
\|\tau_K-\tau\|_1
=2\left(1-\frac{Z_K}{Z_\beta}\right)
\longrightarrow0.
\tag{C10}
```

Joint lower semicontinuity therefore yields

```math
D(\rho\|\tau)
\le\liminf_{K\to\infty}
D\bigl(\Phi_K(\rho)\|\tau_K\bigr).
```

The reverse inequality and monotonicity follow from (C7). Together they prove (C8), including the case of infinite relative entropy. $`\square`$

For finite $`D(\rho\|\tau)`$, define

```math
f_K(\rho)=\frac1\beta D\bigl(\Phi_K(\rho)\|\tau_K\bigr),
\qquad
f(\rho)=\frac1\beta D(\rho\|\tau).
```

Then $`0\le f_K(\rho)\uparrow f(\rho)`$. This statement is pointwise in $`\rho`$. It supplies no common rate at which the free-energy loss disappears over an unrestricted family of source states.

## 5. Why a slow cutoff is sufficient

The product operation $`\Phi_K^{\otimes n}`$ maps $`\rho^{\otimes n}`$ exactly to $`\Phi_K(\rho)^{\otimes n}`$. Its trace is one for every $`K`$ and $`n`$. A fixed cutoff therefore presents a finite-dimensional i.i.d. source to the next part of the engine, regardless of how much population lies above the cutoff.

The retained free-energy rate at fixed $`K`$ is $`f_K(\rho)`$. Once the finite-dimensional protocol has reached its prescribed accuracy, the cutoff can be increased. Proposition C2 ensures that any schedule $`K(n)\to\infty`$ eventually recovers the entire rate for each fixed source, provided that the finite-dimensional processing errors also vanish along that schedule.

This differs operationally from requiring all $`n`$ specimens to lie in the cutoff sector. That event has probability $`[\operatorname{Tr}(\Pi_K\rho)]^n`$, which vanishes at fixed $`K`$ whenever the source has nonzero tail population. Watanabe and Takagi's infinite-dimensional construction uses an increasing cutoff to control that event and imposes its stated source restrictions; see [their main-text discussion after Theorem 3](https://pmc.ncbi.nlm.nih.gov/articles/PMC12957447/). Here the finite-dimensional state is obtained with certainty, and the quantity that converges is its relative entropy.

The next page, [the universal protocol](universal_protocol.md), chooses the increasing cutoff together with the estimation and extraction accuracies. The choice depends only on $`H`$, $`\beta`$, and the fixed battery gap.
