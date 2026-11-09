# Exact output levels and the entropy boundary

A universal work extractor can make the work per copy converge to the source free energy without making one exact battery level overwhelmingly likely at every block length. The distinction already appears for commuting two-level sources. It follows from continuity of finite-sample statistics, rather than from a restriction on thermal operations.

This page proves two statements. First, one source-independent processor sequence cannot select a canonical exact output with probability tending to one along every integer block length when its limiting value varies on every source interval. Second, any sequence with the correct work rate has a dense residual set of sources for which the largest output atom is at most $1/2+o(1)$ along a subsequence. For energy-incoherent batteries this implies an infinitely-often entropy lower bound of $\ln 2$.

All logarithms are natural. A residual set is the complement of a countable union of nowhere dense sets. The conclusions below concern Baire category and make no Lebesgue-measure claim.

## 1. A continuous family of experiments

Let $I=[a,b]$ be a compact interval with $a<b$. For each positive integer $n$, let

$$
\theta\longmapsto\sigma_{n,\theta}
$$

be a trace-norm-continuous family of input states. A processor $\Lambda_n$, followed by a fixed countable-outcome measurement, produces a label $A_n\in\mathcal A_n$. Both the processor and measurement are independent of $\theta$. The alphabet may depend on $n$, and each label has a fixed numerical value $e_n(a)$. Define

$$
p_{n,a}(\theta)=\Pr_\theta(A_n=a),\qquad
W_n=e_n(A_n),\qquad
m_n(\theta)=\sup_{a\in\mathcal A_n}p_{n,a}(\theta).
$$

The state $\sigma_{n,\theta}$ may include fixed auxiliary systems. Adaptivity, internal randomization, and discarded systems are absorbed into the channel. No thermodynamic restriction is imposed in Sections 1–3.

Let $f:I\to\mathbb R$ be **nowhere locally constant**: it is not constant on any nonempty open subinterval of $I$. Strict monotonicity is sufficient. Continuity of $f$ is not needed for the proofs, although the free-energy curves used below are smooth.

### Lemma 1: continuity of the largest atom

For every $n$, $m_n$ is continuous on $I$. Its supremum is attained.

**Proof.** Trace-distance contraction under channels and measurements gives

$$
\sum_a\left|p_{n,a}(\theta)-p_{n,a}(\theta')\right|
\leq
\left\|\sigma_{n,\theta}-\sigma_{n,\theta'}\right\|_1.
$$

Consequently,

$$
|m_n(\theta)-m_n(\theta')|
\leq\sup_a|p_{n,a}(\theta)-p_{n,a}(\theta')|
\leq\left\|\sigma_{n,\theta}-\sigma_{n,\theta'}\right\|_1.
$$

A probability distribution on a countable set has a positive largest atom. Indeed, if its positive supremum $s$ were not attained, infinitely many distinct atoms would have mass greater than $s/2$, contradicting normalization. $\square$

This argument is important for an infinite battery. Continuity does not follow by treating a countable union of closed sets as closed; that union need not be closed.

### Lemma 2: a dominant label cannot change on an interval

Fix $c>1/2$, an integer $n$, and a connected interval $J\subseteq I$. If $m_n(\theta)\geq c$ for every $\theta\in J$, there is one label $v_n$ such that

$$
p_{n,v_n}(\theta)\geq c\qquad(\theta\in J).
$$

**Proof.** At each point the label of probability at least $c$ is unique. Let its value at $\theta_0$ be $v$. Continuity makes $p_{n,v}(\theta)>1-c$ throughout a neighborhood of $\theta_0$. A different label of probability at least $c$ in that neighborhood would make the sum of the two probabilities exceed one. The dominant label is therefore locally constant. A locally constant map on a connected interval is constant. $\square$

The strict inequality $c>1/2$ is necessary for this argument. At probability $1/2$, two labels can tie and exchange dominance continuously.

## 2. Pointwise canonical-output impossibility

### Theorem 1: no all-integer canonical output

Under the assumptions above, there are no designated labels $a_n(\theta)$ satisfying, for every $\theta\in I$,

$$
p_{n,a_n(\theta)}(\theta)\longrightarrow1,
\qquad
\frac{e_n(a_n(\theta))}{n}\longrightarrow f(\theta)
\quad(n\to\infty).
$$

Both limits are pointwise in $\theta$ and run through all positive integers. No common convergence speed is assumed. The selected labels need not be continuous or measurable functions of $\theta$.

**Proof.** Choose any fixed $c\in(1/2,1)$, and define

$$
F_N(c)=\bigcap_{n\geq N}
\{\theta\in I:m_n(\theta)\geq c\}.
$$

Lemma 1 makes every $F_N(c)$ closed. Pointwise canonical concentration implies

$$
I=\bigcup_{N=1}^{\infty}F_N(c).
$$

The complete metric space $I$ is a Baire space, so at least one $F_N(c)$ has nonempty relative interior. Choose a connected subinterval $J$ of positive length in that interior. For every $n\geq N$, Lemma 2 supplies a label $v_n$ that is independent of $\theta\in J$ and has probability at least $c$.

For each fixed $\theta\in J$, the designated label eventually has probability greater than $1-c$. It must then equal $v_n$, since two distinct labels with those probabilities would have total mass greater than one. Hence

$$
\frac{e_n(v_n)}{n}\longrightarrow f(\theta)
\qquad\text{for every }\theta\in J.
$$

The left-hand side is the same numerical sequence for all $\theta\in J$. Its limit makes $f$ constant on $J$, a contradiction. $\square$

The success assumption can be weakened further to

$$
\liminf_{n\to\infty}p_{n,a_n(\theta)}(\theta)>\frac12
\qquad\text{for every }\theta\in I,
$$

with a different positive margin at each source. In that case the closed sets $F_N(c)$, with rational $c\in(1/2,1)$ and integer $N$, form a countable cover of $I$. Baire again supplies one interval with a common dominant label. The designated label eventually has probability greater than $1/2$, so it must agree with that dominant label. The same contradiction follows.

## 3. A residual entropy obstruction under rate consistency

Canonical concentration is stronger than work-rate consistency. Suppose only that

$$
\forall\theta\in I,\ \forall\varepsilon>0,\qquad
\Pr_\theta\!\left(
\left|\frac{W_n}{n}-f(\theta)\right|>\varepsilon
\right)\longrightarrow0.
$$

### Theorem 2: residual largest-atom bound

There is a dense $G_\delta$ set $R\subseteq I$ such that

$$
\liminf_{n\to\infty}m_n(\theta)\leq\frac12
\qquad(\theta\in R).
$$

The set $R$ can depend on the processor sequence.

**Proof.** Fix a rational $c\in(1/2,1)$. Every $F_N(c)$ is closed. If one had nonempty interior, Lemma 2 would give a positive-length interval $J$ and labels $v_n$ common to all $\theta\in J$, for every $n\geq N$.

For a fixed $\theta\in J$, rate consistency forces

$$
\frac{e_n(v_n)}n\longrightarrow f(\theta).
$$

Otherwise, along a subsequence the event of a fixed positive rate error would have probability at least $c$, contradicting convergence in probability. Since the labels are common on $J$, $f$ would be constant there. Thus every $F_N(c)$ has empty interior and is nowhere dense.

Set

$$
R=I\setminus
\bigcup_{c\in\mathbb Q\cap(1/2,1)}
\bigcup_{N=1}^{\infty}F_N(c).
$$

This is a dense $G_\delta$ set by Baire's theorem. For $\theta\in R$, every rational $c>1/2$ and every $N$ admit an $n\geq N$ with $m_n(\theta)<c$. This is exactly the asserted liminf bound. $\square$

Define the classical min-entropy and Shannon entropy of the output label by

$$
H_\infty(A_n)_\theta=-\ln m_n(\theta),
\qquad
H(A_n)_\theta=-\sum_a p_{n,a}(\theta)\ln p_{n,a}(\theta).
$$

Because $H(A_n)_\theta\geq H_\infty(A_n)_\theta$, Theorem 2 gives

$$
\limsup_{n\to\infty}H_\infty(A_n)_\theta\geq\ln2,
\qquad
\limsup_{n\to\infty}H(A_n)_\theta\geq\ln2
\quad(\theta\in R).
$$

Infinite Shannon entropy is allowed and makes the second inequality immediate. No moment bound on $W_n$ is required.

## 4. Application to a physical work battery

Let $P_w$ be the spectral projections of a countable-spectrum battery Hamiltonian, and let $\omega_{n,\theta}$ be the battery output. Apply Theorem 2 to the energy distribution

$$
p_{n,w}(\theta)=\operatorname{Tr}(P_w\omega_{n,\theta}).
$$

If $\omega_{n,\theta}$ commutes with the battery Hamiltonian, its energy blocks are orthogonal and

$$
S(\omega_{n,\theta})
=H(W_n)_\theta+
\sum_{w:p_{n,w}>0}p_{n,w}\,
S\!\left(\frac{P_w\omega_{n,\theta}P_w}{p_{n,w}}\right)
\geq H(W_n)_\theta.
$$

The equality holds as an identity of extended nonnegative quantities. Energy degeneracies do not weaken the lower bound. For a nondegenerate oscillator battery, the internal-block term vanishes.

Energy incoherence is automatic for the commuting source family relevant here. A thermal operation appends Gibbs states, applies an energy-conserving unitary, and discards subsystems. A stationary source and a ground-state battery make the initial joint state stationary. The global unitary preserves this property, and the reduced output remains stationary under the battery's time evolution. Therefore

$$
\limsup_{n\to\infty}S(\omega_{n,\theta})\geq\ln2
\qquad(\theta\in R)
$$

holds for every rate-consistent thermal processor on that source family, without adding a dephasing assumption to the lower-bound model.

For an arbitrary coherent output state, energy-distribution entropy and von Neumann entropy must be distinguished. The pure state $(|0\rangle+|1\rangle)/\sqrt2$ has energy entropy $\ln2$ and von Neumann entropy zero. The general channel theorem alone therefore gives the energy-label entropy bound, not the von Neumann bound.

### A commuting family with a varying free-energy rate

Choose two energy eigenvectors of the known source Hamiltonian and write their Gibbs probabilities as $\tau_0,\tau_1>0$. Consider

$$
\rho_p=(1-p)|0\rangle\langle0|+p|1\rangle\langle1|.
$$

This family can live in a two-level system or in the first two levels of an oscillator. Its relative entropy to the full Gibbs state is

$$
f(p)=\frac{D(\rho_p\Vert\tau)}\beta
=\frac1\beta\left[
(1-p)\ln\frac{1-p}{\tau_0}
+p\ln\frac p{\tau_1}\right],
$$

and

$$
f'(p)=\frac1\beta\ln\frac{p\tau_0}{(1-p)\tau_1}.
$$

Thus $f$ is strictly increasing on any compact interval of positive length

$$
I\subset\left(\frac{\tau_1}{\tau_0+\tau_1},1\right).
$$

The tensor powers are continuous, with

$$
\|\rho_p^{\otimes n}-\rho_{p'}^{\otimes n}\|_1
\leq n\|\rho_p-\rho_{p'}\|_1
=2n|p-p'|.
$$

All assumptions of the preceding theorems hold. Every member of this oscillator family has finite mean energy. The boundary therefore occurs inside the physical source class of the universal work theorem, without requiring coherence or unusual energy tails.

## 5. The sense in which $\ln 2$ is sharp

The thermal construction supplies, for each source and each $n$, a set of at most two likely energy levels. Let the total probability outside that set be $r_n\leq\eta_n\to0$. Suppose the active battery sector contains at most $M_n$ levels and

$$
\eta_n\ln M_n\longrightarrow0.
$$

Grouping the distribution according to membership in the likely set gives, for all sufficiently large $n$,

$$
S(\omega_n)=H(W_n)
\leq \ln2+h_2(\eta_n)+\eta_n\ln M_n
=\ln2+o(1),
$$

where $h_2(x)=-x\ln x-(1-x)\ln(1-x)$. The size of the error probability alone is insufficient for this entropy estimate; its product with the logarithm of the available output dimension must also vanish.

For the commuting interval in Section 4, combine this upper bound with Theorem 2. The constructed protocol has

$$
\limsup_{n\to\infty}S(\omega_{n,p})=\ln2
$$

on a dense residual set of $p$. The same equality holds for the limsup of the energy-label min-entropy. In particular, if $\mathfrak P$ denotes the class of source-independent thermal processor sequences with the correct rate on this interval and with the same ground-start oscillator battery, then

$$
\inf_{\Lambda\in\mathfrak P}\ \sup_{p\in I}
\limsup_{n\to\infty}S(\omega_{n,p})=\ln2.
$$

This is an unnormalized entropy statement. It does not assert a one-bit work loss, a one-bit entropy production in the bath, or a finite-block work deficit bounded by $\beta^{-1}\ln2$.

### Why the limsup cannot be replaced by a liminf

The construction uses two grids whose boundaries differ by half a bin width on adjacent block lengths. At least one member of every sufficiently late pair has a single likely output label for each fixed source. On those members,

$$
S(\omega_n)\leq h_2(\eta_n)+\eta_n\ln M_n\longrightarrow0.
$$

Consequently the same constructed protocol satisfies

$$
\liminf_{n\to\infty}S(\omega_{n,\rho})=0
$$

for every source, while its limsup is $\ln2$ on the residual commuting family. A lower bound on the entropy at every sufficiently large block length would be false.

### Why the residual set cannot be replaced by every source

Fix any reference source $\rho_0$ in advance. At cutoff stage $K$, translate both grids so that its truncated free-energy value $f_K(\rho_0)$ is one-quarter of a bin width from each grid's boundaries. The grids still differ by half a bin width, so the universal two-bin and paired-grid guarantees for other sources remain valid. For $\rho_0$, however, both members of each sufficiently late pair have a single likely output label. The entropy then tends to zero along the full sequence at $\rho_0$.

The reference is fixed when the machine is designed; it is not supplied as side information about the realized input. This gives a universal thermal construction with a privileged zero-entropy-limit source. It excludes a universal lower bound $\limsup_n S(\omega_{n,\rho})\geq\ln2$ at every source.

### Schedule variant: a null residual exceptional set

The residual lower bound can coexist with entropy convergence to zero for Lebesgue-almost-every parameter in the commuting interval $I$. The following variant strengthens the training schedule. It is not an almost-everywhere conclusion for the unchanged stage thresholds.

Write $a_K$ for the bin width and $s_K$ for the original estimation tolerance. Keep both grids, their half-bin displacement, and the work-extraction margins. Introduce the finer analysis tolerance

$$
\delta_K=\min\{s_K,a_K2^{-K-10}\}.
$$

Increase the even stage thresholds so that, uniformly over all $K$-dimensional inputs and throughout stage $K$, the probability of a training error larger than $\delta_K$ is at most $\eta_K/2$. The finite-dimensional concentration bound permits this at every fixed $K$. Retain the extraction-error bound $\eta_K/2$. Since $\delta_K\leq s_K$, every earlier extraction promise and rate estimate remains valid. The operations change only through the longer source-independent stage schedule.

For the family of Section 4 built from the first two oscillator energy eigenvectors, the cutoff leaves $\rho_p$ unchanged for $K\geq2$. With $q_K=\operatorname{Tr}(\Pi_K\tau)$,

$$
f_K(p)=f(p)+\frac{\ln q_K}{\beta}.
$$

The image $f_K(I)$ has the same width $L=f(b)-f(a)$ at every $K$, and

$$
f_K'(p)=f'(p)\geq c_I>0\qquad(p\in I).
$$

For the two unshifted and half-shifted grids, define the boundary-strip set

$$
B_K=\left\{p\in I:
\operatorname{dist}\!\left(
f_K(p),\,a_K\mathbb Z\cup a_K(\mathbb Z+1/2)
\right)\leq\delta_K\right\}.
$$

The same estimate below holds after any predetermined common translation of the grids. Each relevant rate boundary contributes a parameter interval of length at most $2\delta_K/c_I$. The two grids together have at most $2L/a_K+6$ relevant boundaries. For the decreasing widths used in the construction,

$$
|B_K|
\leq\frac{4(L+3a_2)}{c_I}\frac{\delta_K}{a_K},
\qquad
\sum_{K=2}^{\infty}|B_K|<\infty.
$$

Here $|\cdot|$ denotes Lebesgue measure in the scalar parameter $p$. The first Borel–Cantelli lemma implies that almost every $p$ belongs to only finitely many $B_K$. At each later stage, both grids then place every $\delta_K$-accurate estimate in one bin. At every block length in those stages, its one target level has probability at least $1-\eta_K$. Therefore

$$
S(\omega_{n,p})
\leq h_2(\eta_{K(n)})+\eta_{K(n)}\ln M_{K(n)}
\longrightarrow0
$$

for Lebesgue-almost-every $p\in I$.

The variant still has the correct rate at every $p$. Theorem 2 and the entropy upper bound therefore still give a dense residual set with limsup entropy exactly $\ln2$. That residual set must now have Lebesgue measure zero. This establishes an actual measure-zero example within the thermal construction, rather than relying only on the general distinction between measure and category.

## 6. Scope of the obstruction

**The asymptotic quantifiers matter.** Pointwise convergence permits a different threshold $N(\theta,\varepsilon)$ for each source. Baire's theorem addresses precisely that freedom. It does not replace it by a uniform sample bound.

**A limsup exact-level rate remains possible.** Watanabe and Takagi define their asymptotic work rate using $\lim_{\varepsilon\to0}\limsup_{n\to\infty}$. Good block lengths may depend on the source. The paired-grid sequence satisfies this weaker exact-level convention while retaining all-integer rate concentration. Theorem 1 excludes the stronger requirement that one exact level become overwhelmingly likely at every sufficiently large block length. See [Watanabe and Takagi (2026)](https://www.nature.com/articles/s41467-026-69143-3), Definition 1 and Eqs. (8)–(11).

**A narrow energy window is a different output condition.** Two orthogonal levels can differ by $o(n)$ and hence have the same limiting work per copy. Rate consistency controls their numerical values, not the probability of any one exact label.

**A merely nonconstant target is insufficient.** For Bernoulli samples with mean $p\in[1/4,3/4]$, let $f(p)=\mathbf1_{\{p>1/2\}}$. Output $W_n=n$ when the empirical mean exceeds $1/2+n^{-1/4}$, and $W_n=0$ otherwise. At every fixed $p$, including $p=1/2$, the canonical output has probability tending to one and $W_n/n\to f(p)$. Here the target has constant intervals, so the hypotheses of Theorem 1 fail. This statistical example explains the nowhere-locally-constant assumption.

**No measure statement follows from the Baire argument alone.** A dense $G_\delta$ subset of an interval can have Lebesgue measure zero. The strengthened schedule above realizes that possibility. No almost-everywhere failure or positive-measure entropy lower bound is claimed.

**The alphabet may grow or be countably infinite.** The proofs use total-variation continuity and orthogonal labels, not a fixed finite dimension or a positive minimum energy spacing. A label set or processor chosen from the unknown source itself would change the problem.

## 7. Attribution

The finite-sample canonical-output obstruction and the two-output rounding construction are established in [Dixon, Pavan, Vander Woude, and Vinodchandran (2023)](https://proceedings.neurips.cc/paper_files/paper/2023/file/61d0a96d4a73b626367310b3ad32579d-Paper-Conference.pdf), especially the introductory coin-estimation example. [Chase, Moran, and Yehudayoff (2023)](https://arxiv.org/abs/2304.03757) relate the same limitation to global stability and list replicability. The present proof uses Baire category to retain pointwise, full-sequence quantifiers without a common sample threshold. It then applies the resulting bound to the physical energy distribution.

[Plesnik and Violaris (2024)](https://doi.org/10.1088/1367-2630/ad7f7c) also establish a single-shot deterministic-work obstruction from nonorthogonality. The many-copy, pointwise asymptotic quantifiers here are different.

The two-bin upper bound is an implementation of the one-dimensional list-estimation idea. The thermodynamic work is to realize its branches with counted source specimens, Gibbs ancillas, energy-conserving control, and a ground-start battery. The information-theoretic rounding step is not a separate new distillation principle. The companion [related-work account](../references/related_work.md) distinguishes these inherited ingredients from the infinite-dimensional extraction result.
