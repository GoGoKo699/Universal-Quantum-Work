# Uniform extraction above a known free-energy threshold

A fixed extraction target can be implemented without knowing the source state. The processor only needs the promise that the source free energy exceeds that target by a positive margin. This page proves the finite-dimensional statement with a uniform error bound and an explicit thermal dilation.

The construction combines a joint energy and Schur-sector test with position-based decoding. In this extraction problem, there is no quantum memory to preserve. Tests on different bath blocks therefore commute, and an exact controlled-shift unitary can perform the decoding on a genuinely Gibbs-initialized register. A final finite bath transfers the resulting purity to a fixed energy level of a ground-state battery.

## 1. Setting and finite-dimensional extraction lemma

Let the source Hilbert space have dimension $`d<\infty`$, with Hamiltonian $`H`$ and inverse temperature $`\beta>0`$. Define

```math
Z=\operatorname{Tr}e^{-\beta H},
\qquad
\tau=\frac{e^{-\beta H}}{Z},
\qquad
f_H(\rho)=\frac{D(\rho\Vert\tau)}{\beta}.
\tag{F1}
```

All logarithms are natural. For finite dimension,

```math
f_H(\rho)
=\operatorname{Tr}(H\rho)
-\frac{S(\rho)}{\beta}
+\frac{\ln Z}{\beta}.
\tag{F2}
```

The battery is the fixed oscillator

```math
H_W=\Delta\sum_{k=0}^{\infty}k\,|k\rangle\langle k|,
\qquad \Delta>0,
\tag{F3}
```

initialized in $`|0\rangle`$. When $`W`$ is a nonnegative integer multiple of $`\Delta`$, the notation $`|W\rangle`$ denotes the battery eigenstate of energy $`W`$.

A thermal operation appends a finite ancillary system in its Gibbs state at inverse temperature $`\beta`$, applies a unitary commuting with the total additive Hamiltonian, and discards subsystems. A finite product of such operations has the same form after combining its ancillary systems.

**Lemma F1, uniform fixed-target extraction.** Fix $`H,\beta,\Delta`$, a target rate $`r\ge0`$, and a margin $`s>0`$. For every positive integer $`\ell`$, there is a thermal operation $`\mathcal E_{\ell,r,s}`$ from $`\ell`$ source copies and the grounded battery to the battery, independent of $`\rho`$, with the following properties.

Set

```math
W_\ell=\Delta\left\lfloor\frac{\ell r}{\Delta}\right\rfloor.
\tag{F4}
```

For every source state, the battery output is diagonal and supported on $`\{|0\rangle,|W_\ell\rangle\}`$. For every state satisfying

```math
f_H(\rho)\ge r+s,
\tag{F5}
```

its target population obeys

```math
\langle W_\ell|
\mathcal E_{\ell,r,s}
\bigl(\rho^{\otimes\ell}\otimes|0\rangle\langle0|\bigr)
|W_\ell\rangle
\ge 1-\epsilon_\ell(H,\beta,s),
\tag{F6}
```

where $`\epsilon_\ell\to0`$ exponentially up to a polynomial factor. The error bound is uniform in $`\rho`$, $`r`$, and $`\Delta`$. Every auxiliary register starts in its full Gibbs state. The construction uses no initially pure helper, coherence reference, or positive-energy work loan.

If $`W_\ell=0`$, the identity on the battery proves the statement exactly. If $`d=1`$, condition (F5) is empty, and the identity is again sufficient. For $`d\ge2`$, the following explicit bound applies.

Let

```math
R=E_{\max}(H)-E_{\min}(H),
\qquad
A_\ell=(\ell+1)^{d(d+1)/2},
\tag{F7}
```

and write $`h_2(x)=-x\ln x-(1-x)\ln(1-x)`$. Choose any fixed $`t\in(0,1]`$ satisfying

```math
\frac{t}{2}\ln(d-1)+h_2\!\left(\frac{t}{2}\right)
\le\frac{\beta s}{4}.
\tag{F8}
```

Such a positive $`t`$ always exists and depends only on $`d,\beta,s`$. Define

```math
e_\ell^{\mathrm{energy}}=
\begin{cases}
2\exp[-\ell s^2/(8R^2)],&R>0,\\
0,&R=0,
\end{cases}
\qquad
\alpha_\ell
=A_\ell e^{-\ell t^2/2}+e_\ell^{\mathrm{energy}}.
\tag{F9}
```

One valid choice is

```math
\epsilon_\ell(H,\beta,s)
=\min\left\{
1,\,
\alpha_\ell
+(A_\ell+1)e^{-\beta\ell s/4}
\right\}.
\tag{F10}
```

In particular, with the energy exponent omitted when $`R=0`$,

```math
c=\min\left\{\frac{t^2}{2},\,\frac{s^2}{8R^2},\,
\frac{\beta s}{4}\right\}>0
\tag{F11}
```

gives $`\epsilon_\ell\le\min\{1,(2A_\ell+3)e^{-c\ell}\}`$. No convergence rate uniform in an increasing cutoff dimension is asserted.

The proof has three parts: a source-independent test with small Gibbs acceptance, an exact unitary that purifies a Gibbs register using that test, and a finite-bath conversion from purity to battery energy.

## 2. A commuting free-energy test

Write

```math
H^{(\ell)}=\sum_{i=1}^{\ell}H_i.
\tag{F12}
```

Schur-Weyl duality decomposes the source block as

```math
(\mathbb C^d)^{\otimes\ell}
\cong
\bigoplus_{\lambda}
\mathcal U_\lambda\otimes\mathcal V_\lambda,
\tag{F13}
```

where $`\lambda=(\lambda_1,\ldots,\lambda_d)`$ is a nonincreasing list of nonnegative integers summing to $`\ell`$. Let $`\Pi_\lambda`$ be the corresponding projector and $`q_\lambda=\lambda/\ell`$. Every $`\Pi_\lambda`$ commutes with $`V^{\otimes\ell}`$ for every one-copy unitary $`V`$. Taking $`V=e^{-itH}`$ shows that $`\Pi_\lambda`$ commutes with $`H^{(\ell)}`$.

Let $`R_E`$ be the spectral projector of $`H^{(\ell)}`$ with energy $`E`$. The commuting projectors $`\Pi_\lambda R_E`$ define the joint numerical estimate

```math
\widehat f_\ell(\lambda,E)
=\frac{E}{\ell}
-\frac{H(q_\lambda)}{\beta}
+\frac{\ln Z}{\beta}.
\tag{F14}
```

For a real threshold $`a`$, define the orthogonal projector

```math
P_\ell(a)=
\sum_{\lambda,E:\,\widehat f_\ell(\lambda,E)\ge a}
\Pi_\lambda R_E.
\tag{F15}
```

This operator commutes with $`H^{(\ell)}`$. The construction below uses it as a unitary control. It does not require an external measurement record.

### 2.1 Schur-sector bounds

Put $`c_d=d(d-1)/2`$. Three elementary bounds suffice:

```math
\#\{\lambda\}\le(\ell+1)^d,
\qquad
\dim\mathcal U_\lambda\le(\ell+1)^{c_d},
\qquad
\dim\mathcal V_\lambda\le e^{\ell H(q_\lambda)}.
\tag{F16}
```

The first bound counts all possible row-length lists. Weyl's dimension formula gives the second:

```math
\dim\mathcal U_\lambda
=\prod_{i<j}\frac{\lambda_i-\lambda_j+j-i}{j-i}
\le(\ell+1)^{c_d}.
\tag{F17}
```

For the third, a standard Young tableau determines a word listing the row occupied by each integer. This injects the tableaux into words with row counts $`\lambda_i`$, so

```math
\dim\mathcal V_\lambda
\le\frac{\ell!}{\prod_i\lambda_i!}
\le e^{\ell H(q_\lambda)}.
\tag{F18}
```

Consequently

```math
\operatorname{rank}\Pi_\lambda
\le(\ell+1)^{c_d}e^{\ell H(q_\lambda)}.
\tag{F19}
```

If $`p`$ is the eigenvalue list of $`\rho`$ in nonincreasing order, the highest-weight bound for the $`\mathcal U_\lambda`$ representation gives

```math
\operatorname{Tr}(\Pi_\lambda\rho^{\otimes\ell})
\le
(\ell+1)^{c_d}
e^{-\ell D(q_\lambda\Vert p)}.
\tag{F20}
```

Indeed, the largest eigenvalue of the representation of $`\rho`$ on $`\mathcal U_\lambda`$ is $`\prod_i p_i^{\lambda_i}`$. Multiplying this by the two dimension bounds in (F16) gives (F20). Singular $`\rho`$ follow by continuity, with relative entropy interpreted as $`+\infty`$ when its support condition fails. This is the finite-block form of the spectrum-estimation argument of Keyl and Werner [1].

Classical Pinsker's inequality, with natural logarithms, gives $`D(q\Vert p)\ge\|q-p\|_1^2/2`$. Summing (F20) therefore yields the source-uniform bound

```math
\Pr_\rho\{\|q_\lambda-p\|_1>t\}
\le A_\ell e^{-\ell t^2/2}.
\tag{F21}
```

### 2.2 Acceptance of every promised source

The Fannes-Audenaert inequality [2], together with (F8), implies that $`\|q_\lambda-p\|_1\le t`$ guarantees

```math
|H(q_\lambda)-S(\rho)|\le\frac{\beta s}{4}.
\tag{F22}
```

The entropy-continuity expression in (F8) is nondecreasing on $`0\le t\le1`$, so using an upper bound on the actual distance is legitimate.

The total-energy marginal has the same distribution as a sum of $`\ell`$ independent measurements of $`H`$ on $`\rho`$. Each outcome lies in an interval of width $`R`$. Hoeffding's inequality [3] gives

```math
\Pr_\rho\left\{
\left|\frac{E}{\ell}-\operatorname{Tr}(H\rho)\right|>\frac{s}{4}
\right\}
\le e_\ell^{\mathrm{energy}}.
\tag{F23}
```

This statement also holds for coherent $`\rho`$: an energy measurement samples its diagonal energy probabilities. The Schur and energy estimates need not be statistically independent. Their commuting joint measurement and a union bound are sufficient.

Set

```math
a=r+\frac{s}{2}.
\tag{F24}
```

When both (F22) and the complementary event in (F23) hold,

```math
\widehat f_\ell
\ge f_H(\rho)-\frac{s}{2}.
\tag{F25}
```

Every source satisfying (F5) is therefore accepted, except with probability at most $`\alpha_\ell`$:

```math
\operatorname{Tr}\bigl[P_\ell(a)\rho^{\otimes\ell}\bigr]
\ge1-\alpha_\ell.
\tag{F26}
```

The constants do not depend on the source spectrum, its rank, or the target rate.

### 2.3 Small acceptance of the Gibbs state

For a fixed $`\lambda`$, acceptance requires

```math
E\ge
\ell a+\frac{\ell H(q_\lambda)}{\beta}
-\frac{\ell\ln Z}{\beta}.
\tag{F27}
```

On that accepted subspace, the Gibbs density $`\tau^{\otimes\ell}=Z^{-\ell}e^{-\beta H^{(\ell)}}`$ is bounded above by

```math
e^{-\beta\ell a-\ell H(q_\lambda)}I.
\tag{F28}
```

The rank bound (F19) then gives

```math
\begin{aligned}
b_\ell
&:=\operatorname{Tr}\bigl[P_\ell(a)\tau^{\otimes\ell}\bigr]\\
&\le
\sum_\lambda
e^{-\beta\ell a-\ell H(q_\lambda)}
\operatorname{rank}\Pi_\lambda\\
&\le A_\ell e^{-\beta\ell a}.
\end{aligned}
\tag{F29}
```

Summing the ranks within each Schur sector avoids an additional factor for the number of energy values. Equations (F26) and (F29) are the only test properties needed for extraction.

## 3. Purifying a Gibbs register by exact position decoding

This step applies more generally to a finite system $`S`$, its Gibbs state $`\gamma`$, an unknown state $`\sigma`$, and a projector $`P`$ commuting with $`H_S`$. Suppose

```math
\operatorname{Tr}(P\sigma)\ge1-\alpha,
\qquad
\operatorname{Tr}(P\gamma)=b.
\tag{F30}
```

Choose an integer $`M\ge2`$. Append $`M`$ copies $`A_0,\ldots,A_{M-1}`$ of $`S`$, each in $`\gamma`$, together with a register $`J`$ satisfying

```math
H_J=0,
\qquad
\gamma_J=\frac{I_J}{M}.
\tag{F31}
```

The full dimension of $`J`$ is $`M`$. Its initial state is its Gibbs state on the entire register.

First apply

```math
U_{\mathrm{swap}}
=\sum_{j=0}^{M-1}
\operatorname{SWAP}_{S,A_j}\otimes|j\rangle\langle j|_J.
\tag{F32}
```

Each source and bath block has the same Hamiltonian, so this unitary conserves energy. Conditional on the initial label $`j`$, the resulting physical state has $`\gamma`$ on $`S`$, $`\sigma`$ on $`A_j`$, and $`\gamma`$ on every other $`A_k`$.

On the bath blocks, define the unique-acceptance projectors

```math
Q_j=P_{A_j}\prod_{k\ne j}(I-P_{A_k}),
\qquad
Q_{\mathrm{fail}}=I-\sum_{j=0}^{M-1}Q_j.
\tag{F33}
```

The factors act on different blocks. Hence the $`Q_j`$ are pairwise orthogonal projectors, $`Q_{\mathrm{fail}}`$ is a projector, and they all commute with the bath Hamiltonian.

Let $`X_J|j\rangle=|j+1\bmod M\rangle`$. The decoder is

```math
U_{\mathrm{decode}}
=\sum_{j=0}^{M-1}Q_j\otimes X_J^{-j}
+Q_{\mathrm{fail}}\otimes I_J.
\tag{F34}
```

Orthogonality of the controls makes (F34) an exact unitary. It conserves energy because its controls commute with the bath Hamiltonian and $`H_J=0`$.

For an initial label $`j`$, the probability that its source-containing position is uniquely accepted is

```math
\operatorname{Tr}(P\sigma)(1-b)^{M-1}
\ge1-\alpha-(M-1)b.
\tag{F35}
```

On this event, the decoder sends $`|j\rangle_J`$ to $`|0\rangle_J`$. Averaging over the initially uniform label gives

```math
\langle0|\omega_J|0\rangle
\ge1-\alpha-(M-1)b.
\tag{F36}
```

The marginal $`\omega_J`$ is diagonal. Cross terms between different controls have zero partial trace because the control projectors are orthogonal. The identity action on $`Q_{\mathrm{fail}}`$ may add further population to $`|0\rangle`$, which is not needed for the bound.

This is a specialization of the position-based conditional-erasure construction of Faist, Berta, and Brandao [4]. In their general setting, different tests can share a retained memory and need not commute. Here no memory is retained, so the orthogonal projectors (F33) suffice. The construction is already a unitary on the stated Gibbs register and requires no dilation register.

For the extraction problem, take

```math
S=(\mathbb C^d)^{\otimes\ell},
\qquad
\sigma=\rho^{\otimes\ell},
\qquad
\gamma=\tau^{\otimes\ell},
\qquad
P=P_\ell(r+s/2).
\tag{F37}
```

## 4. Charging the ground-state battery with a finite Gibbs bath

Assume $`W_\ell>0`$ and choose

```math
M=
\left\lceil
\exp\!\left[\beta\left(W_\ell+\frac{\ell s}{4}\right)\right]
\right\rceil.
\tag{F38}
```

There is enough margin both to purify this register reliably and to convert its purity to the target energy.

The exact ceiling inequality is

```math
M-1
<
\exp\!\left[\beta\left(W_\ell+\frac{\ell s}{4}\right)\right].
\tag{F39}
```

Using $`W_\ell\le\ell r`$ and (F29),

```math
(M-1)b_\ell
\le A_\ell e^{-\beta\ell s/4}.
\tag{F40}
```

Consequently the position decoder produces

```math
\langle0|\omega_J|0\rangle
\ge
1-\alpha_\ell-A_\ell e^{-\beta\ell s/4}.
\tag{F41}
```

Append a bath $`B`$ with one state $`|b_0\rangle`$ of energy zero and $`M`$ orthonormal states $`|b_{1,j}\rangle`$, $`j=0,\ldots,M-1`$, of energy $`W_\ell`$. Its full Gibbs state is

```math
\gamma_B=
\frac{
|b_0\rangle\langle b_0|
+e^{-\beta W_\ell}
\sum_{j=0}^{M-1}|b_{1,j}\rangle\langle b_{1,j}|
}{
1+M e^{-\beta W_\ell}
}.
\tag{F42}
```

Define $`U_{\mathrm{charge}}`$ by the disjoint transpositions

```math
|0\rangle_J|0\rangle_W|b_{1,j}\rangle_B
\longleftrightarrow
|j\rangle_J|W_\ell\rangle_W|b_0\rangle_B,
\qquad j=0,\ldots,M-1,
\tag{F43}
```

and the identity on the orthogonal complement. Both vectors in each pair have total energy $`W_\ell`$. Thus $`U_{\mathrm{charge}}`$ is exactly unitary and energy conserving. It acts nontrivially only in the battery sector $`\operatorname{span}\{|0\rangle,|W_\ell\rangle\}`$, and extends by identity to the rest of the fixed oscillator.

For the grounded battery, its excitation probability is exactly

```math
p_\ell
=\langle0|\omega_J|0\rangle
\frac{M e^{-\beta W_\ell}}{1+M e^{-\beta W_\ell}}.
\tag{F44}
```

The reserve in (F38) gives

```math
M e^{-\beta W_\ell}\ge e^{\beta\ell s/4},
\qquad
\frac{1}{1+M e^{-\beta W_\ell}}
\le e^{-\beta\ell s/4}.
\tag{F45}
```

Combining (F41), (F44), and (F45) yields

```math
p_\ell
\ge
1-\alpha_\ell-(A_\ell+1)e^{-\beta\ell s/4},
\tag{F46}
```

which proves (F6) and (F10).

The charging unitary is a basis permutation, and $`\omega_J`$ and $`\gamma_B`$ are diagonal. The battery output is therefore exactly

```math
\omega_W
=p_\ell|W_\ell\rangle\langle W_\ell|
+(1-p_\ell)|0\rangle\langle0|.
\tag{F47}
```

The success probability in the lemma is also its squared fidelity with $`|W_\ell\rangle`$. With the unsquared convention, the fidelity is $`\sqrt{p_\ell}`$. No fidelity convention is needed to interpret the population bound.

## 5. Resource accounting and the uniform interface

All initial ancillary states in the construction are Gibbs states. The source-dependent resource is precisely the supplied block $`\rho^{\otimes\ell}`$; the battery starts in the same ground state for every source.

| System | Hamiltonian and initial state | Size |
|---|---|---|
| Source block $`S`$ | $`H^{(\ell)}`$, state $`\rho^{\otimes\ell}`$ | $`d^\ell`$ |
| Position baths $`A_j`$ | $`H^{(\ell)}`$, Gibbs state $`\tau^{\otimes\ell}`$ | $`M`$ blocks, each of dimension $`d^\ell`$ |
| Position register $`J`$ | Zero Hamiltonian, full Gibbs state $`I_J/M`$ | $`M`$ |
| Charging bath $`B`$ | Energies $`0,W_\ell`$, Gibbs state (F42) | $`M+1`$ |
| Battery $`W`$ | Fixed Hamiltonian (F3), initially $`\lvert0\rangle`$ | Only $`\{0,W_\ell\}`$ is active |

The appended Gibbs ancillas have total dimension

```math
\dim(AJB)=d^{\ell M}M(M+1).
\tag{F48}
```

After shifting the source energy origin so that $`E_{\min}(H)=0`$, their Hamiltonian has energy range at most $`\ell M R+W_\ell`$. The construction is finite for every $`\ell`$. It does not bound the bath size, control complexity, or implementation time by a physically economical scaling.

The three energy-conserving unitaries can be composed on the full collection of systems, and all unwanted systems can be traced out at the end. The projectors in the proof specify coherent controls; no observer reads a measurement result. The complete register $`J`$ begins maximally mixed, and the charging bath retains its nonzero ground-sector probability. The protocol therefore makes only the approximate success claim (F6), with an explicit finite-bath error.

For subsequent universal constructions, the useful interface is:

```math
\boxed{
\begin{gathered}
f_H(\rho)\ge r+s
\quad\Longrightarrow\quad
\Pr\!\left[W=\Delta\lfloor\ell r/\Delta\rfloor\right]
\ge1-\epsilon_\ell(H,\beta,s),\\
\operatorname{supp}\omega_W
\subseteq
\operatorname{span}\{|0\rangle,|W_\ell\rangle\},
\qquad
[\omega_W,H_W]=0 .
\end{gathered}
}
\tag{F49}
```

The processor may change when $`r`$ changes, but the error bound does not. A later protocol can therefore choose a predetermined family of target rates, compile their thermal dilations under energy-commuting training controls, and use one common finite-size error bound. The fixed positive margin is essential to that uniform bound.

## 6. Attribution and primary references

The spectral estimator, concentration ingredients, and position-decoding principle are established tools. The proof above makes their finite-dimensional extraction specialization explicit, including a genuinely Gibbs-initialized position register and one fixed ground-state ladder. Faist's 2026 variable-work construction also establishes finite-dimensional universal and fixed-threshold extraction [5]; no novelty claim is made for that underlying capability.

1. M. Keyl and R. F. Werner, “Estimating the spectrum of a density operator,” Physical Review A 64, 052311 (2001). [Published article](https://doi.org/10.1103/PhysRevA.64.052311), [arXiv:quant-ph/0102027](https://arxiv.org/abs/quant-ph/0102027). Section II defines the Schur-sector estimator; Section III, Eqs. (17)–(21), gives the character and highest-weight bounds used in (F20).

2. K. M. R. Audenaert, “A sharp continuity estimate for the von Neumann entropy,” Journal of Physics A: Mathematical and Theoretical 40, 8127–8136 (2007). [Published article](https://doi.org/10.1088/1751-8113/40/28/S18), [arXiv:quant-ph/0610146](https://arxiv.org/abs/quant-ph/0610146). Theorem 1, Eq. (6), with logarithms converted from base two to natural logarithms, gives the entropy modulus in (F8).

3. W. Hoeffding, “Probability Inequalities for Sums of Bounded Random Variables,” Journal of the American Statistical Association 58, 13–30 (1963). [Published article](https://doi.org/10.1080/01621459.1963.10500830). Theorem 2, Eq. (2.6), gives (F23).

4. P. Faist, M. Berta, and F. G. S. L. Brandao, “Thermodynamic Implementations of Quantum Processes,” Communications in Mathematical Physics 384, 1709–1750 (2021). [Published article](https://doi.org/10.1007/s00220-021-04107-w), [arXiv:1911.05563v3](https://arxiv.org/abs/1911.05563v3). The following locators refer to the arXiv version: Section 2.4, Proposition 2.1, treats uniform spectrum and entropy estimation; Section 7.2, Proposition 7.1 and Lemma 7.1, develops position-based conditional erasure; Eqs. (7.8)–(7.15) supply the controlled-swap and decoding architecture specialized in Section 3 above.

5. P. Faist, “Universal thermodynamic implementation of a process with a variable work cost,” [arXiv:2601.20155v1](https://arxiv.org/abs/2601.20155v1) (2026). Section II discusses work extraction; Theorem 1(ii), Eqs. (9)–(10), gives uniform finite-dimensional work guarantees; Appendix C, Lemma 7 and Eqs. (C21)–(C30), provides the fixed-threshold construction. The present proof uses the commuting, no-retained-memory specialization rather than importing a battery initialization by convention.
