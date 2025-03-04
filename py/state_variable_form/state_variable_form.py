import numpy as np
import scipy.signal as signal
import matplotlib.pyplot as plt

# assume SISO
n = int(input("Enter number of state variables: "))

# A matrix
print(" -- A")

A = np.zeros((n, n))
for i in range(n):
    for j in range(n):
        A[i, j] = float(input(f"Enter value for row {i + 1}, column {j + 1} of matrix A: "))

# B vector
print(" -- B")

B = np.zeros((n, 1))
for i in range(n):
    B[i, 0] = float(input(f"Enter value for row {i + 1} of vector B: "))

# C vector
print(" -- C")

C = np.zeros((1, n))
for j in range(n):
    C[0, j] = float(input(f"Enter value for column {j + 1} of vector C: "))

# D
print(" -- D")
D = np.zeros((1, 1))
D[0, 0] = float(input("Enter D: "))

# bounds
lower = float(input("Enter lower time bound: "))
upper = float(input("Enter upper time bound: "))
t = np.linspace(lower, upper, 1000)

# input
in_type = input("Enter input type (sin, heaviside): ")
if in_type == "sin":
    u = np.sin(t)
elif in_type == "heaviside":
    step_t = float(input("Enter step time: "))
    u = np.heaviside(t - step_t, 1)
else:
    print("Unknown input type, exiting...")
    exit()

# initial state 
x0 = np.zeros((1, n))

# setup system
sys = signal.StateSpace(A, B, C, D)

# solve 
t_out, y_out, x_out = signal.lsim(sys, U=u, T=t, X0=x0)

# plot
plt.plot(t_out, y_out, label="Output y(t)")
plt.plot(t_out, u, '--', label="Input u(t)")
plt.legend()
plt.xlabel("Time")
plt.ylabel("Response")
plt.show()

