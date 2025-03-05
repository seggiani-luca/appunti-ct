import numpy as np
import scipy.signal as signal
import matplotlib.pyplot as plt

# assume SISO

# outputs
n = int(input("Enter max output degree: "))

alphas = np.zeros((n + 1, 1))
for i in range(n + 1):
    alphas[i, 0] = float(input(f"Enter alpha_{i}: "))

# inputs
p = int(input("Enter max input degree: "))

betas = np.zeros((n + 1, 1))  # take n + 1 anyways and fill with zeroes
for i in range(p + 1):
    betas[i, 0] = float(input(f"Enter beta_{i}: "))

# normalize
denom = alphas[n, 0]

if denom == 0:
    print("Max degree output coefficient can't be 0, exiting...")
    exit()

norm_alphas = alphas / denom
norm_betas = -betas / denom

# A
A = np.hstack((
    np.zeros((n - 1, 1)), np.eye(n - 1)
    ))

A = np.vstack((
    A, -np.transpose(np.resize(norm_alphas, (n, 1)))
    ))

print("Got A:\n", A)

# B
B = np.vstack((
    np.zeros((n - 1, 1)), np.array([1])
    ))

print("Got B:\n", B)

# distinguish p = 0 and p != 0 cases
if p == 0:
    # C
    C = np.zeros((1, n))
    C[0, 0] = norm_betas[0, 0]

    # D
    D = np.zeros((1, 1))
elif p < n:
    # C
    C = np.transpose(np.resize(norm_betas, (n, 1)))

    # D
    D = np.zeros((1, 1))
elif p == n:
    # C
    C = np.resize(norm_betas, (n, 1))
    C -= norm_betas[n, 0] * np.resize(norm_alphas, (n, 1))
    C = np.transpose(C)

    # D
    D = np.array([norm_betas[n, 0]])
else:
    print("Max input degree can't be higher than max output degree, exiting...")
    exit()

print("Got C:\n", C)
print("Got D:\n", D)

# bounds
lower = float(input("Enter lower time bound: "))
upper = float(input("Enter upper time bound: "))
t = np.linspace(lower, upper, 1000)

# input
in_type = input("Enter input type (sin, step): ")
if in_type == "sin":
    u = np.sin(t)
elif in_type == "step":
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

# get constraint
constraint = np.zeros_like(t_out)
dy_out = y_out
du = u

for i in range(n + 1):
    constraint += dy_out * alphas[i, 0] + du * betas[i, 0]
    dy_out = np.gradient(dy_out, t)
    du = np.gradient(du, t)

# plot
plt.plot(t_out, y_out, label="Output y(t)")
plt.plot(t_out, u, '--', label="Input u(t)")
plt.plot(t_out, constraint, label="Constraint", linestyle=':')
plt.legend()
plt.xlabel("Time")
plt.ylabel("Response")
plt.show()
