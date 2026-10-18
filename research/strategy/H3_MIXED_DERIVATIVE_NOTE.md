# Mixed derivative extraction for H3

Let f(0)=f'(0)=g(0)=0, and P(u,v)=f(u+v)g(u-v). Elementary differentiation gives

    d_u^2 d_v P(0,0) = f''(0)g'(0).
    d_u^3 P(0,0) = 3 f''(0)g'(0).

The idempotent epsilon_2=(1+sigma_1)(1+sigma_2)(1-sigma_3)/8 in Q[(Z/2)^3] selects the (+,+,-) character. This is the algebraic pattern of Yun–Zhang 2019, Theorem 1.3, for (r,r1)=(3,2), over function fields only.

Falsifiers: f(t)=t^2,g(t)=t gives nonzero mixed derivative 2, while f(t)=t^4,g(t)=t gives zero. f(t)=t^2,g(t)=t^3 gives zero even though f''(0) is nonzero: twist nonvanishing is required. Rank four does not force exterior-cube vanishing, since dim wedge^3(Q^4)=4. Thus the geometric formula alone cannot prove BSD, and neither a rank-based wedge argument nor first-height vanishing is sufficient.

**Unproved arrows:** construct a number-field three-leg cycle and a proved comparison to the complex derivative; then independently prove a rank-four arithmetic reason for its projected pairing to vanish. Neither is available in this project. No claim of new BSD mathematics.
