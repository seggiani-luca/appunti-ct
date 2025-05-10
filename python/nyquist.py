import matplotlib.pyplot as plt
import control as ctrl

num = [10, 0]
den = [1, 2, 1]
sys = ctrl.TransferFunction(num, den)

ctrl.nyquist_plot(sys, title="", max_curve_magnitude=10, unit_circle=True)

plt.show()
