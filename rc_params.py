import matplotlib.pyplot as plt 
from matplotlib import rc

#Locale settings
import locale
# Set to German locale to get comma decimal separater
locale.setlocale(locale.LC_NUMERIC, "de_DE")
# Tell matplotlib to use the locale we set above
plt.rcParams['axes.formatter.use_locale'] = True

font = {'family':'sans-serif','sans-serif':'Helvetica', 'weight': 'bold'}
rc('font',**font)
rc('text', usetex=True)
rc('lines', linewidth=2)
rc('xtick', labelsize=11)
rc('ytick', labelsize=11)
rc('axes', labelsize=12)
rc('legend',fontsize=12)
