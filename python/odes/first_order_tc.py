import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp

# params
K = 1.0  # gain
tc = 2.0 # time constant

v0 = 0.0 # initial condition

st1 = 0.0 # switch times
st2 = 100.0

val0 = 0.0 # piecewise values
val1 = 1.0
val2 = -2.0

# simulation
l_bound = -5
h_bound = 10

# input function
def u(t):
    return np.piecewise(t,
                        [t < st1, (t >= st1) & (t < st2), t >= st2],
                        [val0, val1, val2])

def ode(t, v):
    return (K * u(t) - v) / tc

# time interval
t_span = (l_bound, h_bound)
t_eval = np.linspace(l_bound, h_bound, 100)

# solve ode
sol = solve_ivp(ode, t_span, [v0], t_eval=t_eval)

# get tc value 
v_tc = np.interp(tc, sol.t, sol.y[0])

# plot solution
plt.plot(sol.t, sol.y[0], label="y(t)")
plt.plot(sol.t, u(sol.t), label="u(t)", linestyle="dashed")

# plot tc value
plt.axvline(tc, linestyle="dotted", color="red")
plt.scatter(tc, v_tc, color="red", label=f"y({tc}) ≈ {v_tc:.2f}", zorder=3)

plt.xlabel="Time"
plt.legend()
plt.grid()
plt.show()
