import matplotlib.pyplot as plt
import control as ctrl

num = [10, 0]
den = [1, 2, 1]
sys = ctrl.TransferFunction(num, den)

ctrl.bode_plot(sys, title="")

plt.show()
