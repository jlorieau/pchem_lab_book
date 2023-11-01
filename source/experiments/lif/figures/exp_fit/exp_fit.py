import numpy as np
from matplotlib import pyplot as plt
from scipy.optimize import curve_fit

I0 = 100.
k = 1E5

tdead = np.arange(-5.0, 0.0, 0.1)  # microseconds
t = np.arange(0.0, 40, 0.1)  # microseconds
t_total = np.concatenate((tdead, t))

# Model the dead time
mean = 0.0
stdev = 1.0
Idead = np.random.normal(mean, stdev, tdead.size)

# Model the decay
Isignal = I0 * np.exp(- k * t * 1E-6) + np.random.normal(mean, stdev, t.size)

# Combine the two
I = np.concatenate((Idead, Isignal))

# Create the subplots
fig, (ax1, ax2) = plt.subplots(1, 2, sharey=True, figsize=(5, 3))

# Without truncation
ax1.plot(t_total, I)
ax1.set_title('Before truncation')
ax1.set_xlabel('time (us)')
ax1.set_xticks(np.arange(0, 50, 10.))
ax1.set_ylabel('Intensity (A.U.)')

# With truncation
ax2.plot(t, Isignal)
ax2.set_title('After truncation')
ax2.set_xticks(np.arange(0, 50, 10.))

# Fit the truncated data
def func(x, a, b):
    return a * np.exp(-b * x)

popt, pcov = curve_fit(func, t, Isignal, bounds=((1., 1E-6), (150., 10.)))
perr = np.sqrt(np.diag(pcov))
print(popt)
print(perr)

# Add fit
I0_fit, k_fit = popt
I0_err, k_err = perr
ax2.plot(t, func(t, I0_fit, k_fit))
ax2.annotate(f"$I_0$ = {I0_fit:.2f} ± {I0_err:.2f}\n"
             f"k = {k_fit * 1E6 / 1E5:.3f} ± {k_err * 1E6 / 1E5:.3f} $\cdot 10^5 s^{{-1}}$",
             xy=(0.625, 0.725), xycoords='subfigure fraction',
             fontsize=9)

plt.tight_layout()
plt.show()
