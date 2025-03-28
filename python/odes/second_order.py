import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp

# params
w = 0.5 # natural frequency
x = 0.3 # damping
b = 0.25 # gain

v0 = 0.0 # initial condition
dv0 = 0.0

st1 = 0.0 # switch times
st2 = 100.0

val0 = 0.0 # piecewise values
val1 = 1.0
val2 = -2.0

# simulation
l_bound = -10
h_bound = 50

# input function
def u(t):
    return np.piecewise(t,
                        [t < st1, (t >= st1) & (t < st2), t >= st2],
                        [val0, val1, val2])

def ode(t, v):
    v1, v2 = v
    dv1_dt = v2
    dv2_dt = b * u(t) - 2 * w * x * v2 - w ** 2 * v1
    return [dv1_dt, dv2_dt]

# time interval
t_span = (l_bound, h_bound)
t_eval = np.linspace(l_bound, h_bound, 100)

# solve ode
sol = solve_ivp(ode, t_span, [v0, dv0], t_eval=t_eval)

# plot solution
plt.plot(sol.t, sol.y[0], label="v(t)")
plt.plot(sol.t, u(sol.t), label="u(t)", linestyle="dashed")
plt.xlabel="Time"
plt.legend()
plt.grid()
plt.show()
