# One protocol for all finite-relative-entropy sources

This page constructs the sequence of thermal operations in the [main theorem](model_theorem.md). At block length $`n`$, every input specimen is compressed to a finite Gibbs-compatible system. A sublinear part of the compressed block controls a conservative work target for the remaining specimens. Two alternating grids make the same construction attain an exact battery level along a source-dependent subsequence, while every block length retains a narrow two-level output distribution.

The construction depends on the known Hamiltonian $`H`$, inverse temperature $`\beta`$, and fixed battery spacing $`\Delta`$. It does not use the source state or a bound on its tail.

## 1. The finite-dimensional dependency

The [fixed-threshold extraction result](finite_extraction.md) supplies the following interface. This is the finite-dimensional ingredient, whose hypothesis tests and decoding construction are attributed and proved on that page.

Fix a finite Hamiltonian $`G`$, a positive margin $`s`$, and a target rate $`r\ge0`$. There is a thermal operation on $`\ell`$ input specimens and the fixed ground-initialized oscillator battery with target

```math
w_{\ell,r}=\Delta\left\lfloor\frac{\ell r}{\Delta}\right\rfloor.
\qquad\text{(U1)}
```

Its battery output is diagonal and supported on $`\{0,w_{\ell,r}\}`$ for every input state. For every i.i.d. input $`\sigma^{\otimes\ell}`$ satisfying

```math
\frac1\beta D(\sigma\|\tau_G)\ge r+s,
```

the target population is at least $`1-\epsilon_\ell(G,\beta,s)`$. The error bound is independent of $`\sigma`$ and $`r`$, and

```math
\epsilon_\ell(G,\beta,s)\longrightarrow0
\qquad(\ell\to\infty)
\qquad\text{(U2)}
```

for each fixed $`G`$ and $`s`$. The implementation uses finite Gibbs ancillas, an energy-conserving unitary, and no auxiliary pure state. For a zero target, the identity operation suffices. Use the explicit error function in equation (F10) of the finite extraction proof. Its bound is a polynomial times a decaying exponential; the stage argument below needs its uniformity and convergence for each fixed finite system.

## 2. A scalar estimate with energy-commuting controls

At cutoff $`K\ge2`$, let $`H_K`$, $`\tau_K`$, and $`\Phi_K`$ be the objects defined in [thermal compression](thermal_cutoff.md). For the current source write

```math
\sigma_K=\Phi_K(\rho),
\qquad
f_K=\frac1\beta D(\sigma_K\|\tau_K).
```

The following quantities depend only on the cutoff Hamiltonian:

```math
R_K=E_K-E_1,
\qquad
F_K=E_K+\frac{\ln Z_K}{\beta}.
\qquad\text{(U3)}
```

Every state $`\sigma`$ on $`\mathcal H_K`$ satisfies

```math
0\le f_{H_K}(\sigma)
=\mathrm{Tr}(H_K\sigma)-\frac{S(\sigma)}\beta
 +\frac{\ln Z_K}\beta
\le F_K.
\qquad\text{(U4)}
```

Use $`m`$ specimens as a training block. Let $`\{E_e^{(m)}\}`$ be the spectral projections of its total Hamiltonian, with eigenvalue $`e`$, and let $`\{P_\lambda^{(m)}\}`$ be its Schur–Weyl projections. The Young diagram $`\lambda`$ is a partition of $`m`$ with at most $`K`$ rows. Schur–Weyl projections commute with every collective unitary $`V^{\otimes m}`$, and therefore with the total Hamiltonian. The products

```math
R_{e,\lambda}=E_e^{(m)}P_\lambda^{(m)}
\qquad\text{(U5)}
```

are mutually orthogonal projections summing to the identity. Their classical labels define the estimates

```math
\widehat E=\frac em,
\qquad
q_i=\frac{\lambda_i}{m},
\qquad
\widehat f=\widehat E-\frac{\mathsf H(q)}\beta
 +\frac{\ln Z_K}\beta,
\qquad\text{(U6)}
```

where $`\mathsf H(q)=-\sum_i q_i\ln q_i`$. Clip the last quantity to the known interval:

```math
\widetilde f=\min\{F_K,\max\{0,\widehat f\}\}.
\qquad\text{(U7)}
```

Clipping cannot increase its distance from the true value in (U4).

These labels are a convenient way to analyze the projectors. The physical protocol below uses the projectors directly as controls and does not prepare an external measurement register.

### A uniform finite-sample bound

Fix a tolerance $`s>0`$. Choose a dyadic number $`t\in(0,1]`$ satisfying

```math
h_2(t/2)+\frac t2\ln(K-1)\le\frac{\beta s}{2},
\qquad\text{(U8)}
```

where $`h_2(u)=-u\ln u-(1-u)\ln(1-u)`$. For definiteness, take the largest number in $`\{1,1/2,1/4,\ldots\}`$ satisfying (U8). Such a number exists.

If $`p`$ is the ordered spectrum of $`\sigma`$, the standard Schur spectrum bound is

```math
\Pr_\sigma\!\left[\|q-p\|_1>t\right]
\le (m+1)^{K(K+1)/2}e^{-mt^2/2}.
\qquad\text{(U9)}
```

It follows from the Schur block estimate

```math
\mathrm{Tr}\bigl(P_\lambda^{(m)}\sigma^{\otimes m}\bigr)
\le(m+1)^{K(K-1)/2}e^{-mD(q\|p)},
```

the bound $`(m+1)^K`$ on the number of diagrams, and Pinsker's inequality with natural logarithms. The Schur estimate is the spectrum-estimation ingredient of [Keyl and Werner](https://arxiv.org/abs/quant-ph/0102027); the dimension and counting bounds used here are also stated in the [finite extraction proof](finite_extraction.md). They are uniform in the spectrum, including its boundary.

The entropy difference on the complementary event obeys

```math
|\mathsf H(q)-\mathsf H(p)|
\le h_2(t/2)+\frac t2\ln(K-1)
\le\frac{\beta s}{2}.
\qquad\text{(U10)}
```

The first inequality is the classical finite-alphabet entropy continuity bound. It follows by coupling the two distributions with mismatch probability $`\|q-p\|_1/2`$ and bounding each conditional entropy by the binary mismatch entropy plus the logarithm of the remaining $`K-1`$ possibilities.

The total-energy measurement has the distribution of a sum of $`m`$ independent energy outcomes, each in an interval of width $`R_K`$. Hoeffding's bound gives

```math
\Pr_\sigma\!\left[
|\widehat E-\mathrm{Tr}(H_K\sigma)|>s/2
\right]
\le2e^{-ms^2/(2R_K^2)}.
\qquad\text{(U11)}
```

The right side is defined to be zero when $`R_K=0`$, since the energy outcome is then constant. The form of the bounded-sum inequality is [Hoeffding, Theorem 2](https://doi.org/10.1080/01621459.1963.10500830). The energy and Schur outcomes need not be independent; a union bound is sufficient.

Define

```math
B_{K,s}(m)
=\min\!\left\{1,
(m+1)^{K(K+1)/2}e^{-mt^2/2}
 +2e^{-ms^2/(2R_K^2)}
\right\},
\qquad\text{(U12)}
```

with the same convention for $`R_K=0`$. Equations (U8)–(U11) imply

```math
\sup_{\sigma\in\mathcal D(\mathcal H_K)}
\Pr_\sigma\!\left[
|\widetilde f-f_{H_K}(\sigma)|>s
\right]
\le B_{K,s}(m),
\qquad
B_{K,s}(m)\longrightarrow0.
\qquad\text{(U13)}
```

## 3. Work grids and their finite output alphabets

Fix the cutoff-dependent tolerances

```math
a_K=\frac1{\beta K},
\qquad
s_K=\frac1{100\beta K^2}.
\qquad\text{(U14)}
```

Here $`a_K`$ is the work-rate bin width and $`s_K`$ is the estimation tolerance. Both have units of energy. At block length $`n`$, use the phase

```math
\theta_n=
\begin{cases}
0,&n\text{ even},\\
1/2,&n\text{ odd}.
\end{cases}
\qquad\text{(U15)}
```

For phase $`\theta`$, the bin containing $`x`$ has index and lower endpoint

```math
j_{K,\theta}(x)=\left\lfloor\frac{x}{a_K}-\theta\right\rfloor,
\qquad
b_{K,\theta,j}=a_K(j+\theta).
\qquad\text{(U16)}
```

Only the finite index set

```math
\mathcal J_{K,\theta}
=\{j_{K,\theta}(x):0\le x\le F_K\}
\qquad\text{(U17)}
```

can occur. For each of these bins, set

```math
r_{K,\theta,j}
=\max\{0,b_{K,\theta,j}-4s_K\}.
\qquad\text{(U18)}
```

The training and extraction block lengths are

```math
m_n=\lfloor\sqrt n\rfloor,
\qquad
\ell_n=n-m_n.
\qquad\text{(U19)}
```

The branch target is the exact oscillator energy

```math
w_{n,j}
=\Delta\left\lfloor
\frac{\ell_n r_{K,\theta_n,j}}\Delta
\right\rfloor.
\qquad\text{(U20)}
```

For a fixed $`n`$ and $`K`$, every possible battery outcome belongs to the source-independent alphabet

```math
\mathcal A_{n,K}
=\{0\}\cup
\{w_{n,j}:j\in\mathcal J_{K,\theta_n}\}.
\qquad\text{(U21)}
```

The harmless overestimate

```math
M_K=\left\lceil\frac{F_K}{a_K}\right\rceil+4
\qquad\text{(U22)}
```

satisfies $`|\mathcal A_{n,K}|\le M_K`$ for both phases and every $`n`$. All output energies obey

```math
0\le w_{n,j}\le nF_K.
\qquad\text{(U23)}
```

To see that the extraction promise is available, suppose $`|\widetilde f-f_K|\le s_K`$. If the observed bin has positive target rate $`r_j`$, then

```math
f_K\ge b_j-s_K=r_j+3s_K.
\qquad\text{(U24)}
```

Thus the primitive with margin $`s_K`$ applies. A zero target uses the identity. In either case,

```math
0\le r_j\le f_K,
\qquad
f_K-r_j\le a_K+5s_K.
\qquad\text{(U25)}
```

For a positive target, the second bound follows from $`b_j>\widetilde f-a_K`$. If $`r_j=0`$, then $`b_j\le4s_K`$, which gives $`f_K\lt a_K+5s_K`$.

## 4. Compiling the controls into a thermal operation

Apply $`\Phi_K`$ independently to all $`n`$ source specimens. The resulting state is exactly $`\sigma_K^{\otimes n}`$. On its first $`m_n`$ factors, group the projectors in (U5) by the bin of their estimate:

```math
P_j=\sum_{(e,\lambda):\,
j_{K,\theta_n}(\widetilde f(e,\lambda))=j}
R_{e,\lambda}.
\qquad\text{(U26)}
```

These projections are orthogonal, sum to the identity, and commute with the training Hamiltonian.

For each branch $`j`$, choose the finite extraction unitary supplied by Section 1 on the remaining $`\ell_n`$ specimens, the common battery, and a finite Gibbs bath $`B_j`$. Append all branch baths at the outset in their product Gibbs state. Extend each branch unitary by the identity on the unused baths. Then

```math
U_{n,K}=\sum_j P_j\otimes U_{n,j}
\qquad\text{(U27)}
```

is a unitary: orthogonality of the $`P_j`$ eliminates every cross term in $`U_{n,K}^\dagger U_{n,K}`$. Each control projector commutes with the training energy and each branch unitary preserves the remaining total energy. Therefore (U27) is energy conserving.

Each branch uses only the battery sector $`\mathrm{span}\{|0\rangle,|w_{n,j}/\Delta\rangle\}`$. Its unitary extends by the identity on the orthogonal battery sector, which is invariant under the battery Hamiltonian. This extension commutes with the full time evolution even though the battery Hamiltonian is unbounded. A common ground level across different branches creates no conflict because their training projectors are orthogonal.

After applying (U27), discard the training specimens, extraction specimens, and all baths. Tracing out training removes its off-diagonal control blocks. The battery state is therefore

```math
\omega_{n,K}(\rho)
=\sum_j
\mathrm{Tr}\bigl(P_j\sigma_K^{\otimes m_n}\bigr)
\,\omega_{n,j}(\sigma_K^{\otimes\ell_n}).
\qquad\text{(U28)}
```

The output is diagonal and supported on (U21), by the corresponding properties of the finite primitive. The training specimens supply the control record and are consumed. Their number is included in $`n`$, so their loss is included in the rate factor $`\ell_n/n`$. No external record is prepared or erased.

Conditioning thermal operations on energy-commuting projectors is an inherited compilation technique, used in [Watanabe and Takagi's universal construction](https://pmc.ncbi.nlm.nih.gov/articles/PMC12957447/). Equation (U27) gives the implementation required here, including the discarded training and all branch baths.

## 5. A single source-independent cutoff schedule

Choose the failure budget

```math
\eta_K=
\frac1{K^2\bigl(1+\ln M_K+\beta F_K\bigr)}.
\qquad\text{(U29)}
```

This choice gives three useful bounds:

```math
\eta_K\le\frac1{K^2},
\qquad
\eta_K\ln M_K\le\frac1{K^2},
\qquad
\eta_KF_K\le\frac1{\beta K^2}.
\qquad\text{(U30)}
```

The last two conditions control the entropy and mean-energy contributions of rare failures even when the finite-dimensional maximum $`F_K`$ grows rapidly.

Use the deterministic error envelopes

```math
\overline B_K(M)
=\sup_{m\ge M}B_{K,s_K}(m),
\qquad
\overline\epsilon_K(L)
=\sup_{\ell\ge L}\epsilon_\ell(H_K,\beta,s_K),
\qquad\text{(U31)}
```

where the suprema are over integers. Each envelope tends to zero at fixed $`K`$. These are bounds over sample sizes, not over unknown sources; the source uniformity has already been established in (U2) and (U13).

The envelopes can be bounded by finite expressions. For any $`p\ge0`$, $`c>0`$, and $`L\ge0`$, set

```math
v_{p,c}(L)=\max\{L,p/c-1\},
\qquad
G_{p,c}(L)=(v_{p,c}(L)+1)^p e^{-cv_{p,c}(L)}.
\qquad\text{(U31a)}
```

Differentiating $`(x+1)^p e^{-cx}`$ shows that its supremum over real $`x\ge L`$ is $`G_{p,c}(L)`$. Each polynomial-times-exponential term in (U12) and in the primitive's equation (F10) therefore has this explicit decreasing upper envelope. Summing those envelopes gives finite expressions that certify the conditions below; no search over source states is involved.

Recursively choose an even integer $`N_K`$, for $`K=2,3,\ldots`$. Take the least even integer satisfying

```math
N_K\ge\max\{4,2K,N_{K-1}+2\},
\qquad\text{(U32)}
```

with the $`N_{K-1}`$ condition omitted for $`K=2`$, and

```math
\overline B_K(\lfloor\sqrt{N_K}\rfloor)\le\eta_K/2,
\qquad
\overline\epsilon_K(N_K-\lfloor\sqrt{N_K}\rfloor)
\le\eta_K/2,
\qquad\text{(U33)}
```

```math
\frac{F_K}{\sqrt{N_K}}\le a_K,
\qquad
\frac\Delta{N_K}\le a_K.
\qquad\text{(U34)}
```

Such a finite integer exists for every fixed $`K`$: the two error envelopes vanish, $`m_n/n\le n^{-1/2}`$, and $`n^{-1}\to0`$. All the quantities in (U32)–(U34) depend only on the known model and the finite-dimensional bounds. No source-tail convergence estimate enters their definition.

For $`n\ge N_2`$, set

```math
K(n)=\max\{K\ge2:N_K\le n\}.
\qquad\text{(U35)}
```

For the finitely many smaller blocks, leave the battery at its ground level. The strict growth in (U32) makes $`K(n)`$ well defined and finite, and $`K(n)\to\infty`$. Since every $`N_K`$ is even,

```math
K(2t)=K(2t+1)
\qquad\text{(U36)}
```

for every pair after the initial finite segment. Use the operation from Section 4 at this cutoff.

For every $`n\ge N_2`$, with $`K=K(n)`$, equations (U33) and (U34) imply

```math
B_{K,s_K}(m_n)+\epsilon_{\ell_n}(H_K,\beta,s_K)
\le\eta_K,
\qquad
\frac{m_nF_K}{n}\le a_K,
\qquad
\frac\Delta n\le a_K.
\qquad\text{(U37)}
```

Both $`m_n`$ and $`\ell_n`$ are nondecreasing in $`n`$, so the error-envelope conditions continue to hold throughout each stage. These are the finite-stage bounds used below.

## 6. Work concentration and convergence of the mean

Fix an arbitrary source state $`\rho`$. At a given $`n`$, a correct training estimate has probability at least $`1-B_{K,s_K}(m_n)`$. Every branch compatible with that event satisfies its extraction promise by (U24). Equation (U28) and the uniform primitive error therefore give a joint event of probability at least $`1-\eta_K`$ on which the estimate is correct and the battery reaches its branch target.

Let $`X_n`$ denote the measured battery energy. On that event, (U20), (U25), and (U37) give

```math
0\le f_K(\rho)-\frac{X_n}{n}
\le a_K+5s_K+\frac{m_nF_K}{n}+\frac\Delta n
\le c_K,
\qquad
c_K=3a_K+5s_K.
\qquad\text{(U38)}
```

On every event, both $`X_n/n`$ and $`f_K(\rho)`$ lie in $`[0,F_K]`$. Consequently,

```math
\mathbb E_\rho\left|
\frac{X_n}{n}-f_K(\rho)
\right|
\le c_K+\eta_KF_K
\le c_K+\frac1{\beta K^2}.
\qquad\text{(U39)}
```

For a source with finite $`f(\rho)=D(\rho\|\tau)/\beta`$, the cutoff theorem gives $`f_K(\rho)\uparrow f(\rho)`$. Hence

```math
\mathbb E_\rho\left|
\frac{X_n}{n}-f(\rho)
\right|
\le f(\rho)-f_{K(n)}(\rho)
 +c_{K(n)}+\frac1{\beta K(n)^2}
\longrightarrow0.
\qquad\text{(U40)}
```

This proves convergence in probability and convergence of the mean along the full sequence. The first term on the right is source dependent. The theorem makes no uniform convergence-rate claim for it.

## 7. Two work values and one bit of output entropy

On a correct estimate, $`\widetilde f`$ lies in

```math
[f_K(\rho)-s_K,f_K(\rho)+s_K]\cap[0,F_K].
```

Its length is at most $`2s_K\lt a_K`$, so it intersects at most two consecutive bins. The corresponding target rates differ by at most $`a_K`$, including the clipping of negative rates to zero. Their rounded battery energies differ by at most

```math
\ell_na_K+\Delta.
\qquad\text{(U41)}
```

Let $`\mathcal B_{n,\rho}`$ be this set of at most two energy values. It is used only to describe the output; the implemented protocol does not know the set. The joint success bound gives

```math
\Pr_\rho[X_n\in\mathcal B_{n,\rho}]\ge1-\eta_K.
\qquad\text{(U42)}
```

Let $`p`$ be the actual probability outside this set. Splitting the classical output entropy according to membership in the set gives

```math
S(\omega_n(\rho))
\le h_2(p)+(1-p)\ln2+p\ln M_K.
```

Because $`p\le\eta_K\le1/4`$, the binary entropy is increasing on the relevant interval. Equations (U30) and (U42) yield the uniform bound

```math
S(\omega_n(\rho))
\le\ln2+h_2(\eta_K)+\frac1{K^2}
=\ln2+o(1).
\qquad\text{(U43)}
```

The remainder in this entropy estimate is independent of the source. It controls the entropy of rare failure labels as well as that of the two principal labels. A high-probability two-label statement without the finite-alphabet accounting in (U22) and (U29) would not by itself prove (U43).

## 8. Alternating grids and the exact-level limsup

For any real $`x`$, the two boundary sets satisfy

```math
\max\left\{
\mathrm{dist}(x,a_K\mathbb Z),
\mathrm{dist}(x,a_K(\mathbb Z+1/2))
\right\}\ge a_K/4.
\qquad\text{(U44)}
```

Indeed, after reducing $`x`$ modulo $`a_K`$, the two distances sum to $`a_K/2`$. At least one is therefore at least $`a_K/4`$.

Consider a pair $`n=2t,2t+1`$. By (U36), both block lengths have the same cutoff, width, tolerance, and value $`x=f_K(\rho)`$. Choose the member of the pair whose grid is at distance at least $`a_K/4`$ from $`x`$. Since $`s_K\lt a_K/4`$, all estimates within $`s_K`$ of $`x`$ belong to a single bin for that member. Its exact target energy $`w_{n,\rho}`$ therefore satisfies

```math
\langle w_{n,\rho}/\Delta|
\omega_n(\rho)
|w_{n,\rho}/\Delta\rangle
\ge1-\eta_K,
\qquad\text{(U45)}
```

```math
\left|\frac{w_{n,\rho}}n-f(\rho)\right|
\le f(\rho)-f_K(\rho)+c_K.
\qquad\text{(U46)}
```

The favorable member and the displayed label may depend on $`\rho`$. The actual operation at each $`n`$ was fixed in advance. Equations (U45) and (U46) supply at least one successful block in every sufficiently late pair, hence an unbounded subsequence of asymptotically sharp energy outputs at rate $`f(\rho)`$.

For each fixed error tolerance, this proves the lower bound for the exact-level limsup score defined in the [main theorem](model_theorem.md). The [relative-entropy converse](converse.md) supplies the matching upper bound after the tolerance tends to zero. At the other member of a pair, the full-sequence concentration, mean, and entropy guarantees in Sections 6 and 7 still hold.

## 9. What the construction uses

Every block length uses a finite cutoff, finitely many training projectors, finitely many work labels, and a finite product of finite Gibbs baths. All nonthermal input resources are the $`n`$ source specimens and the explicitly specified ground state of the common battery. The protocol places no bound on bath dimension, bath energy, interaction complexity, or running time as $`n`$ increases.

The finite-dimensional concentration and extraction ingredients are used with their state-uniform bounds at a fixed cutoff. The thermal cutoff supplies convergence of the retained relative entropy for each source. The even stage thresholds combine these two facts without assuming a uniform tail rate. The shifted grids specify how the resulting work output meets both a full-sequence concentration criterion and an exact-level limsup criterion.
