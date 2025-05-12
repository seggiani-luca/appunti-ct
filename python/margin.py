import matplotlib.pyplot as plt
import control as ctrl

num = [1, 0.5]
den = [1, 0]
sys = ctrl.TransferFunction(num, den)

ctrl.bode_plot(sys, margins=True, title="")

plt.show()
