import matplotlib.pyplot as plt
import control as ctrl

num = [1, 10]
den = [1, 2, 17, 16, 64, 0]
sys = ctrl.TransferFunction(num, den)

ctrl.root_locus_plot(sys, plot=True, title="")
plt.subplots_adjust(left=0.05, right=0.95, top=0.95, bottom=0.05)

plt.xlim([-20, 20])
plt.ylim([-20, 20])

plt.show()
