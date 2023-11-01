import numpy as np
from matplotlib import pyplot as plt
from scipy.optimize import curve_fit

np.random.seed(1983)

Keq = 1000.0

Q = np.arange(0, 40, 8)  # mM
Iratio = 1.0 + Keq * Q * 1E-3 +  np.random.normal(0, 1., Q.size)


fig, ax = plt.subplots(1, 1, sharey=True, figsize=(5, 3))
ax.scatter(Q, Iratio)

# Regression

def lin(x, m, b):
    return m * x + b

popt, pcov = curve_fit(lin, Q, Iratio, bounds=((0, 0), (1E6, 10.)))
perr = np.sqrt(np.diag(pcov))

ax.plot(Q, lin(Q, *popt),
        label=f"K = {popt[0] / 1E-3:.0f} ± {perr[0] / 1E-3:.0f} $M^{{-1}}$, "
              f"b = {popt[1]:.2f} ± {perr[1]:.2f}")

# Other settings
ax.set_xlabel("Quencher Concentration, [Q] (mM)")
ax.set_ylabel("$[I(0)]_0 / [I(0)]_Q$")

plt.legend()

plt.tight_layout()
plt.show()