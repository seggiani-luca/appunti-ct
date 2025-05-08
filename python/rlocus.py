import matplotlib.pyplot as plt
import control as ctrl

num = [0.01, 0.2, 1]
den = [1, 1, 0, 0]
sys = ctrl.TransferFunction(num, den)

ctrl.root_locus_plot(sys, plot=True, title="")
plt.subplots_adjust(left=0.05, right=0.95, top=0.95, bottom=0.05)


plt.show()
