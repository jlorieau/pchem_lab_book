import matplotlib.pyplot as plt
import numpy as np
from matplotlib import cm

#%% Plot contour
extent = (5, 0, 5, 0)

def peak(X, Y, freq, width):
    denom1 = (X - (extent[0] - freq[0]))**2 + width[0]**2
    denom2 = (Y - freq[1])**2 + width[1]**2
    return np.pi**-2 * width[0] * width[1] / (denom1 * denom2)

delta = 0.01
x = np.arange(*sorted(extent[0:2]), delta)
y = np.arange(*sorted(extent[2:4]), delta)
X, Y = np.meshgrid(x, y)

Z = peak(X, Y, freq=(1.22, 1.22), width=(0.15, 0.15))  # methyl
Z += peak(X, Y, freq=(3.69, 3.69), width=(0.15, 0.15))  # methylene
Z += 0.6*peak(X, Y, freq=(1.22, 3.69), width=(0.15, 0.15))  # crosspeak 1
Z += 0.6*peak(X, Y, freq=(3.69, 1.22), width=(0.15, 0.15))  # crosspeak 2

norm = cm.colors.Normalize(vmax=abs(Z).max(), vmin=-abs(Z).max())

fig, axs = plt.subplots(nrows=1, ncols=1)
axs.imshow(Z, extent=extent, cmap=cm.PRGn, norm=norm)

axs.set_title("$^1$H COSY 2D of Ethanol")
axs.set_xlabel("$^1$H Chemical Shift (ppm)")
axs.set_ylabel("$^1$H Chemical Shift (ppm)")

arrowprops = dict(facecolor='black', headwidth=7.0, headlength=5.0, width=1.0)
axs.annotate("CH3-CH3 (diagonal)",
             xy=(1.2, 1.0), xycoords='data',
             xytext=(2.2, 0.4), textcoords='data',
             va='top', ha='left',
             arrowprops=arrowprops)
axs.annotate("CH2-CH2 (diagonal)",
             xy=(3.75, 4.0), xycoords='data',
             xytext=(4.9, 4.7), textcoords='data',
             va='top', ha='left',
             arrowprops=arrowprops)
axs.annotate("CH3-CH2 (crosspeak)",
             xy=(3.75, 1.0), xycoords='data',
             xytext=(4.9, 0.4), textcoords='data',
             va='top', ha='left',
             arrowprops=arrowprops)
axs.annotate("CH2-CH3 (crosspeak)",
             xy=(1.2, 4.0), xycoords='data',
             xytext=(2.2, 4.7), textcoords='data',
             va='top', ha='left',
             arrowprops=arrowprops)

fig.show()
