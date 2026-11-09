# Optimality and the meaning of the work rate

The achievable rate is the relative entropy from equilibrium divided by the inverse temperature. This page proves that no thermal processor can reliably exceed it. The argument uses a binary battery-energy test, so it also applies when the source has finite relative entropy but separate energy and entropy expressions are not finite.

Read the [model and theorem](model_theorem.md) for the resource convention and the [universal protocol](universal_protocol.md) for achievability. All logarithms are natural.

## 1. A relative-entropy budget for the battery

Let the source Gibbs state be $\tau$, let $D(\rho\Vert\tau)<\infty$, and use the fixed oscillator battery

$$
H_W=\Delta\sum_{k=0}^{\infty} k|k\rangle\langle k|,
\qquad
\tau_W=Z_W^{-1}e^{-\beta H_W},
\qquad
Z_W=\frac{1}{1-e^{-\beta\Delta}}.
\tag{V1}
$$

The battery starts in its ground state. A thermal operation from the source and battery to the battery maps $\tau^{\otimes n}\otimes\tau_W$ to $\tau_W$. This follows directly by appending Gibbs states, commuting the joint unitary with the additive Hamiltonian, and tracing out the other systems.

Data processing therefore gives, for its output $\omega_{W,n}$,

$$
\begin{aligned}
D(\omega_{W,n}\Vert\tau_W)
&\le D\!\left(\rho^{\otimes n}\otimes|0\rangle\langle0|
\,\middle\Vert\,\tau^{\otimes n}\otimes\tau_W\right)\\
&=nD(\rho\Vert\tau)+\ln Z_W.
\end{aligned}
\tag{V2}
$$

The term $\ln Z_W$ is the initial battery's own finite athermality. It contributes no nonzero rate as $n$ grows. No source estimate or source-independence assumption is needed for this upper bound.

## 2. A reliable energy threshold cannot exceed the free-energy rate

For a proposed work density $w>0$, measure whether the battery energy is at least $nw$. Its Gibbs probability is

$$
q_n(w)
=\operatorname{Tr}\!\left[
\mathbf 1_{[nw,\infty)}(H_W)\tau_W\right]
=e^{-\beta\Delta\lceil nw/\Delta\rceil}
\le e^{-\beta nw}.
\tag{V3}
$$

Write $p_n(w)$ for the corresponding probability in $\omega_{W,n}$. Applying data processing once more, now to this binary measurement, yields

$$
\begin{aligned}
nD(\rho\Vert\tau)+\ln Z_W
&\ge d\bigl(p_n(w)\Vert q_n(w)\bigr)\\
&\ge p_n(w)\ln\frac{1}{q_n(w)}-h_2\bigl(p_n(w)\bigr)\\
&\ge \beta nw\,p_n(w)-\ln2.
\end{aligned}
\tag{V4}
$$

Here $d$ is binary relative entropy and $h_2$ is binary entropy. Consequently,

$$
p_n(w)\le
\frac{nD(\rho\Vert\tau)+\ln Z_W+\ln2}{\beta nw}.
\tag{V5}
$$

If the energy density converges in probability to a finite value $v$, then $p_n(w)\to1$ for every $0<w<v$. Equation (V4), followed by $w\uparrow v$, proves

$$
v\le f(\rho):=\frac{D(\rho\Vert\tau)}{\beta}.
\tag{V6}
$$

This converse permits coherent or mixed battery outputs and makes no assumption about their entropy. It is a weak converse for reliable work: it excludes success probability tending to one above $f(\rho)$, but does not assert that the success probability must tend to zero there.

### Exact-label success with vanishing error

Suppose a processor places probability at least $1-\varepsilon$ on an individual energy level $w_n>0$. Its probability of energy at least $w_n$ is at least $1-\varepsilon$, so the same argument gives

$$
(1-\varepsilon)\beta w_n
\le nD(\rho\Vert\tau)+\ln Z_W+\ln2.
\tag{V7}
$$

Thus the ordered criterion that first takes a $\limsup$ over batch size and then lets $\varepsilon\downarrow0$ is also bounded by $f(\rho)$. The paired-grid construction in the [universal protocol](universal_protocol.md) attains this criterion. It does not promise a sharply selected individual label at every sufficiently large batch size.

## 3. The constructed output also attains the mean-energy rate

The constructed battery output has a finite energy alphabet at every $n$, and its entropy satisfies

$$
S(\omega_{W,n})\le\ln2+o(1).
\tag{V8}
$$

Its energy and entropy are therefore finite. Expanding the left side of (V2) is legitimate and gives

$$
\beta\operatorname{Tr}(H_W\omega_{W,n})
-S(\omega_{W,n})
\le nD(\rho\Vert\tau).
\tag{V9}
$$

The upper limit of the mean work per source copy is at most $f(\rho)$. For the reverse inequality, let $X_n$ denote the battery energy. The facts that $X_n\ge0$ and $X_n/n\to f(\rho)$ in probability imply, for every $0<\delta<f(\rho)$,

$$
\frac{\mathbb E X_n}{n}
\ge(f(\rho)-\delta)
\Pr\!\left[\frac{X_n}{n}\ge f(\rho)-\delta\right].
\tag{V10}
$$

Taking the lower limit and then $\delta\downarrow0$ proves

$$
\frac{\mathbb E X_n}{n}\longrightarrow f(\rho).
\tag{V11}
$$

For $f(\rho)=0$, nonnegativity and (V9) suffice. The battery's own nonequilibrium free energy has the same rate because its entropy divided by $n$ vanishes. This identifies the output as work at the asymptotic rate claimed here, while the [output boundary](output_boundary.md) explains the residual uncertainty between individual energy labels.

## 4. Which ingredients are inherited

Monotonicity of relative entropy under quantum channels is an established information-theoretic result. Its use as a thermodynamic work bound is also established. The binary test above is included to make the exact oscillator-battery convention and the finite-relative-entropy domain explicit; it does not require continuity of energy or entropy on an infinite-dimensional state space.

- H. Umegaki, “Conditional expectation in an operator algebra, IV (Entropy and information),” Kodai Mathematical Seminar Reports 14, 59–85 (1962). [Article](https://doi.org/10.2996/kmj/1138844604).
- G. Lindblad, “Completely positive maps and entropy inequalities,” Communications in Mathematical Physics 40, 147–151 (1975). [Article](https://doi.org/10.1007/BF01609396).
- G. Ferrari, L. Lami, T. Theurer, and M. B. Plenio, “Asymptotic State Transformations of Continuous Variable Resources,” Communications in Mathematical Physics 398, 291–351 (2023). [Open article](https://pmc.ncbi.nlm.nih.gov/articles/PMC9898434/). Its infinite-dimensional relative-entropy converse framework is related background; the present achievability construction uses exact thermal operations and is given separately.

Return to the [scientific reading route](README.md).
