import matplotlib.pyplot as plt 
import numpy as np
from mpl_toolkits.axes_grid1.inset_locator import zoomed_inset_axes
from mpl_toolkits.axes_grid1.inset_locator import mark_inset

fig = plt.figure()
t, Ue, Ua = np.loadtxt(r"Daten/81_diff_rechteck_10khz_100mVpp.lvm", usecols = (0,3,4), unpack = True) ## Daten auslesen 

ax = plt.subplot()
plt.xlabel("$t$ [s]")
plt.ylabel("$U_{a}$ [V]")
plt.title("Rechtecks-Eingansspannung der Frequenz $f = 10$ kHz")
ax.plot(t, Ue, label="Eingansspannung")
ax.plot(t, Ua, label="Ausgangsspannung")
plt.legend()


axins = zoomed_inset_axes(ax, 10, loc=6)
x1, x2, y1, y2 = 0.000195, 0.00021, -0.7, 0.7 # specify the limits
axins.set_xlim(x1, x2) # apply the x-limits
axins.set_ylim(y1, y2) # apply the y-limits6
plt.xticks(visible=False)
plt.yticks(visible=False)
axins.plot(t, Ue)
axins.plot(t, Ua)
mark_inset(ax, axins, loc1=3, loc2=4, fc="none", ec="0.2")

plt.show()
