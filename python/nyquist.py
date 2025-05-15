import matplotlib.pyplot as plt
import control as ctrl

num = [10, 100]
den = [10, 1, 10, 1, 0]
sys = ctrl.TransferFunction(num, den)

ctrl.nyquist_plot(sys, title="", max_curve_magnitude=1000, unit_circle=True)

plt.show()
