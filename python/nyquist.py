import matplotlib.pyplot as plt
import control as ctrl

num = [0.01, 0.2, 1]
den = [1,1,0,0]
sys = ctrl.TransferFunction(num, den)

ctrl.nyquist_plot(sys)

plt.show()
