import numpy as np 
import matplotlib.pyplot as plt 
from matplotlib import rc


#Locale settings
import locale
# Set to German locale to get comma decimal separater
locale.setlocale(locale.LC_NUMERIC, "de_DE")
plt.rcdefaults()
# Tell matplotlib to use the locale we set above
plt.rcParams['axes.formatter.use_locale'] = True

"""
t_1, U_e_1, U_a = np.loadtxt(r"10_2_b_A.lvm", usecols = (0,3,4), unpack = True) ## Daten auslesen 
t_2, U_e_2, U_b = np.loadtxt(r"10_2_b_B.lvm", usecols = (0,3,4), unpack = True) ## Daten auslesen 
t_3, U_e_3, U_c = np.loadtxt(r"10_2_b_C.lvm", usecols = (0,3,4), unpack = True) ## Daten auslesen 
t_4, U_e_4, U_d = np.loadtxt(r"10_2_b_D.lvm", usecols = (0,3,4), unpack = True) ## Daten auslesen 
"""

fig, axs = plt.subplots(5, sharex=True, sharey=True, gridspec_kw={'hspace': 0})
plt.subplots_adjust(left = 0.125, right = 0.9, wspace = 0.3, hspace = 0.5)
axs[2].set( ylabel='$U$ [V]')
axs[4].set(xlabel='$t$ [s]')

axs[3].plot(t_1, U_a, label="$U_A$")
axs[2].plot(t_2, U_b, label="$U_B$")
axs[1].plot(t_3, U_c, label="$U_C$")
axs[0].plot(t_4, U_d,  label="$U_D$")
axs[4].plot(t_1, U_e_4, label="$U_E$ / Takt")
plt.yticks([])

for ax in axs:
    ax.legend(loc=1)
    ax.label_outer()

plt.savefig("Pulsfahrplan.png")