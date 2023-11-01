import numpy as np
from matplotlib import pyplot as plt
from scipy.optimize import curve_fit

np.random.seed(1983)

k = 1E7

Q = np.arange(0, 40, 8)  # mM

# Generate the data with error

Qoverall = []
kdyn = []  # dynamic quencher
kstat = []  # static quencher

for i in range(3):
    Qoverall.append(Q)
    kdyn.append(k + 1E5 * Q * 1E-3 + np.random.normal(0, 1E2, Q.size))
    kstat.append(k + 0 * Q * 1E-3 + np.random.normal(0, 1E2, Q.size))

Qoverall = np.concatenate(Qoverall)
kdyn = np.concatenate(kdyn)
kstat = np.concatenate(kstat)

fig, ax = plt.subplots(1, 1, sharey=True, figsize=(5, 3))

ax.scatter(Qoverall, kdyn)
ax.scatter(Qoverall, kstat)

# Fit the curves
def func(x, m, b):
    return m * x + b

popt_dyn, pcov_dyn = curve_fit(func, Qoverall * 1E-3, kdyn, bounds=((0, 0), (1E8, 1E8)))
perr_dyn = np.sqrt(np.diag(pcov_dyn))

print(popt_dyn)
print(perr_dyn)

popt_stat, pcov_stat = curve_fit(func, Qoverall * 1E-3, kstat, bounds=((0, 0), (1E8, 1E8)))
perr_stat = np.sqrt(np.diag(pcov_stat))

print(popt_stat)
print(perr_stat)

ax.plot(Q, func(Q * 1E-3, *popt_dyn), label="dynamic")
ax.plot(Q, func(Q * 1E-3, *popt_stat), label="static")

ax.set_xlabel("Quencher concentration, [Q] (mM)")
ax.set_ylabel("$k_{app}$ ($s^{-1}$)")

plt.legend()
plt.tight_layout()
plt.show()