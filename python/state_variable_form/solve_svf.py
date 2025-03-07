import scipy.signal as signal

def solve_svf(A, B, C, D, t, u, x0):
    print("A:\n", A);
    print("B:\n", B);
    print("C:\n", C);
    print("D:\n", D);

    # setup system
    sys = signal.StateSpace(A, B, C, D)

    # solve
    t_out, y_out, x_out = signal.lsim(sys, U=u, T=t, X0=x0)
    return x_out, y_out, t_out;
