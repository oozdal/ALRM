from __future__ import division
from math import *

#import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt


import numpy as np
import sys
import matplotlib, os
import matplotlib.cm as cm
matplotlib.rcParams['text.usetex'] = True
matplotlib.rcParams['text.latex.unicode'] = True
from matplotlib.ticker import MultipleLocator, FormatStrFormatter
from matplotlib.ticker import AutoMinorLocator
from scipy.interpolate import griddata
from scipy.interpolate import interp1d
import scipy
import pylab, subprocess
import pandas as pd
import shutil
import os.path
from scipy.interpolate import CubicSpline
import seaborn as sns

pylab.rcParams['figure.figsize'] = (8.0, 6.0)
#pylab.rcParams['figure.figsize'] = (10.0, 8.0)

execfile("/home/phylab/hepwork/ExpDATA/ExDATA.py")


def ConvertGeVminus2toPb(valueforGeVminus2):

    return (0.38937929e9)*valueforGeVminus2

############################################################################################################

Accepted_gLneqgR = pd.read_csv('/home/phylab/projects/ALRM_multithread/data/Accepted_gLNEQgR.txt', header=None, sep=" ")
Accepted_gLneqgR.columns =["vp", "MZp", "MWR", "Scot_DM", "Scot_mu", "Scot_tau", "dd1", "dd2", "dd3", "omegah2", "NormSI_P","NormSI_N", "SD_P", "SD_N","sigmaV", "SI_P","SI_N","lm3","mu3","mh1","mh2","mh3","mA2","al1","al2"]

#Excluded_gLneqgR = pd.read_csv('/home/phylab/projects/ALRM_gLneqgR/data/Excluded_gLNEQgR.txt', header=None, sep=" ")
#Excluded_gLneqgR.columns =["vp", "MZp", "MWR", "Scot_DM", "Scot_mu", "Scot_tau", "dd1", "dd2", "dd3", "omegah2", "NormSI_P","NormSI_N", "SD_P", "SD_N","sigmaV", "SI_P","SI_N","lm3","mu3","mh1","mh2","mh3"]



############################################    Plot #9 ####################################################

fig, ax9 = plt.subplots()

#ax9.scatter(np.array(Excluded_gLneqgR["Scot_DM"])/1000., np.array(Excluded_gLneqgR["omegah2"]), c='red', marker=".", zorder=10, label=" Excluded (M$_{Z^\prime} <$ 5.0 TeV)", s=8)

ax9.scatter(np.array(Accepted_gLneqgR["Scot_DM"])/1000., np.array(Accepted_gLneqgR["omegah2"]), c='blue', marker=".", zorder=12, label="Accepted (M$_{Z^\prime} \geq$ 5.0 TeV)",s=8)

    
ax9.text(0.3, 1.5e4, r"$\displaystyle g_L \neq g_R = 0.37 $", size=15)

xmin = 0.0
xmax = 0.9
ymin = 4e-5
ymax = 1e4

ax9.axhspan(0.096,0.122,color='green',fill=True,alpha=.3,linewidth=0.0,zorder=50, label="Planck bound")

mh0_mass = 125.09
mh0_min = (mh0_mass-15.)/1000.
mh0_max = (mh0_mass+15.)/1000.
ax9.axvspan(mh0_min/2., mh0_max/2., color='purple',fill=True,alpha=.2,linewidth=0.0,zorder=50, label="H$_0$ Funnel")

mZ_mass = 91.1876
mZ_min = (mZ_mass-15.)/1000.
mZ_max = (mZ_mass+15.)/1000.
ax9.axvspan(mZ_min/2., mZ_max/2., color='blue',fill=True,alpha=.2,linewidth=0.0,zorder=50, label="Z Funnel")

ax9.axis([xmin,xmax,ymin,ymax])
plt.xlabel(r"$\displaystyle m_{n_e} {\rm\ [TeV]}$", fontsize=20)
plt.ylabel(r"$\displaystyle \Omega_{\rm DM} h^2 $ ", fontsize=20)


ax9.xaxis.set_major_locator(MultipleLocator(0.1))
ax9.xaxis.set_minor_locator(MultipleLocator(0.025))

#ax9.yaxis.set_major_locator(MultipleLocator(5))
#ax9.yaxis.set_minor_locator(MultipleLocator(1))

plt.yscale('log')

# Set both ticks to be outside
ax9.tick_params(which='both', direction='out')

#plt.legend(loc='upper left',frameon=True)
leg = plt.legend(loc='upper right',frameon=True)
leg.set_zorder(100)

fig.savefig("/home/phylab/projects/ALRM_multithread/plot/MassNRvsRelic_gLneqgR.png", dpi=300)   # save the figure to file
plt.close(fig)
"""
############################################    Plot #10 ####################################################

pylab.rcParams['figure.figsize'] = (10.0, 8.0)

fig, ax10 = plt.subplots()

ax10.scatter(np.array(Excluded_gLneqgR["Scot_DM"])/1000., np.array(Excluded_gLneqgR["SI_P"]), c='red',linewidth = '1.0', marker="*", zorder=10, label=" Excluded (M$_{Z^\prime} <$ 5.0 TeV)")

ax10.scatter(np.array(Accepted_gLneqgR["Scot_DM"])/1000., np.array(Accepted_gLneqgR["SI_P"]), c='blue',linewidth = '1.0', marker="*", zorder=12, label="Accepted (M$_{Z^\prime} \geq $ 5.0 TeV)")

ax10.text(0.025, 1.2e-3, r"$\displaystyle g_L \neq g_R = 0.37 $", size=20)

sc10 = ax10.plot(XENONWIMPMASS/1000., XENON1TXSECTION, c='lime',label=r"${\rm\ XENON1T} $",zorder=20, alpha=0.6, linewidth = '3.0')

ax10.fill_between(XENONWIMPMASS/1000, XENON1TXSECTION, ymax, facecolor = 'navy', interpolate=True, alpha=.2,linewidth=0.0, zorder=5, label=r"$\displaystyle {\rm\ Excluded\ by\ XENON1T} $")

xmin = 0.0
xmax = 0.90
ymin = 1e-11
ymax = 1e-5


ax10.axis([xmin,xmax,ymin,ymax])
plt.xlabel(r"$\displaystyle m_{n_e} $ [TeV]", fontsize=20)
#plt.ylabel(r"$\displaystyle \sigma_{SI}^{\rm proton} \rm Min \left( 1, \frac{\Omega_{\rm DM}}{\Omega_{\rm Planck}}\right)$ [pb]", fontsize=20)
plt.ylabel(r"$\displaystyle \sigma_{SI}^p $ [pb]", fontsize=20)

ax10.xaxis.set_major_locator(MultipleLocator(0.1))
ax10.xaxis.set_minor_locator(MultipleLocator(0.025))

#ax10.yaxis.set_major_locator(MultipleLocator(5))
#ax10.yaxis.set_minor_locator(MultipleLocator(1))

plt.yscale('log')

# Set both ticks to be outside
ax10.tick_params(which='both', direction='out')

#plt.legend(loc='best',frameon=True)
leg = plt.legend(loc='upper right',frameon=True)
leg.set_zorder(100)

fig.savefig("/home/phylab/projects/ALRM_gLneqgR/plot/MassNRvsSIxsection_proton_gLneqgR_II.png")   # save the figure to file
plt.close(fig)

############################################    Plot #11 ####################################################

pylab.rcParams['figure.figsize'] = (10.0, 8.0)

fig, ax11 = plt.subplots()

ax11.scatter(np.array(Excluded_gLneqgR["Scot_DM"])/1000., np.array(Excluded_gLneqgR["SI_N"]), c='red',linewidth = '1.0', marker="*", zorder=10, label=" Excluded (M$_{Z^\prime} <$ 5.0 TeV)")

ax11.scatter(np.array(Accepted_gLneqgR["Scot_DM"])/1000., np.array(Accepted_gLneqgR["SI_N"]), c='blue',linewidth = '1.0', marker="*", zorder=12, label="Accepted (M$_{Z^\prime} \geq $ 5.0 TeV)")

ax11.text(0.025, 1.2e-3, r"$\displaystyle g_L \neq g_R = 0.37 $", size=20)

sc11 = ax11.plot(XENONWIMPMASS/1000., XENON1TXSECTION, c='lime',label=r"${\rm\ XENON1T} $",zorder=20, alpha=0.6, linewidth = '3.0')

ax11.fill_between(XENONWIMPMASS/1000, XENON1TXSECTION, ymax, facecolor = 'navy', interpolate=True, alpha=.2,linewidth=0.0, zorder=5, label=r"$\displaystyle {\rm\ Excluded\ by\ XENON1T} $")

xmin = 0.0
xmax = 0.90
ymin = 1e-20
ymax = 1e-5

ax11.axis([xmin,xmax,ymin,ymax])
plt.xlabel(r"$\displaystyle m_{n_e} $ [TeV]", fontsize=20)
#plt.ylabel(r"$\displaystyle \sigma_{SI}^{\rm neutron} \rm Min \left( 1, \frac{\Omega_{\rm DM}}{\Omega_{\rm Planck}}\right)$ [pb]", fontsize=20)
plt.ylabel(r"$\displaystyle \sigma_{SI}^n $ [pb]", fontsize=20)

ax11.xaxis.set_major_locator(MultipleLocator(0.1))
ax11.xaxis.set_minor_locator(MultipleLocator(0.025))

#ax11.yaxis.set_major_locator(MultipleLocator(5))
#ax11.yaxis.set_minor_locator(MultipleLocator(1))

plt.yscale('log')

# Set both ticks to be outside
ax11.tick_params(which='both', direction='out')

#plt.legend(loc='best',frameon=True)
leg = plt.legend(loc='lower right',frameon=True)
leg.set_zorder(100)

fig.savefig("/home/phylab/projects/ALRM_gLneqgR/plot/MassNRvsSIxsection_neutron_gLneqgR_II.png")   # save the figure to file
plt.close(fig)

############################################    Plot #12 ####################################################

pylab.rcParams['figure.figsize'] = (10.0, 8.0)

fig, ax12 = plt.subplots()

ax12.scatter(np.array(Excluded_gLneqgR["Scot_DM"])/1000., np.array(Excluded_gLneqgR["NormSI_P"]), c='red',linewidth = '1.0', marker="*", zorder=10, label=" Excluded (M$_{Z^\prime} <$ 5.0 TeV)")

ax12.scatter(np.array(Accepted_gLneqgR["Scot_DM"])/1000., np.array(Accepted_gLneqgR["NormSI_P"]), c='blue',linewidth = '1.0', marker="*", zorder=12, label="Accepted (M$_{Z^\prime} \geq $ 5.0 TeV)")

ax12.text(0.025, 1.2e-3, r"$\displaystyle g_L \neq g_R = 0.37 $", size=20)

sc12 = ax12.plot(XENONWIMPMASS/1000., XENON1TXSECTION, c='lime',label=r"${\rm\ XENON1T} $",zorder=20, alpha=0.6, linewidth = '3.0')

ax12.fill_between(XENONWIMPMASS/1000, XENON1TXSECTION, ymax, facecolor = 'navy', interpolate=True, alpha=.2,linewidth=0.0, zorder=5, label=r"$\displaystyle {\rm\ Excluded\ by\ XENON1T} $")

xmin = 0.0
xmax = 0.90
ymin = 1e-11
ymax = 1e-5


ax12.axis([xmin,xmax,ymin,ymax])
plt.xlabel(r"$\displaystyle m_{n_e} $ [TeV]", fontsize=20)
plt.ylabel(r"$\displaystyle \sigma_{SI}^{\rm proton} \rm Min \left( 1, \frac{\Omega_{\rm DM}}{\Omega_{\rm Planck}}\right)$ [pb]", fontsize=20)
#plt.ylabel(r"$\displaystyle \sigma_{SI}^p $ [pb]", fontsize=20)

ax12.xaxis.set_major_locator(MultipleLocator(0.1))
ax12.xaxis.set_minor_locator(MultipleLocator(0.025))

#ax12.yaxis.set_major_locator(MultipleLocator(5))
#ax12.yaxis.set_minor_locator(MultipleLocator(1))

plt.yscale('log')

# Set both ticks to be outside
ax12.tick_params(which='both', direction='out')

#plt.legend(loc='best',frameon=True)
leg = plt.legend(loc='upper right',frameon=True)
leg.set_zorder(100)

fig.savefig("/home/phylab/projects/ALRM_gLneqgR/plot/MassNRvsNormSIxsection_proton_gLneqgR_II.png")   # save the figure to file
plt.close(fig)

############################################    Plot #13 ####################################################

pylab.rcParams['figure.figsize'] = (10.0, 8.0)

fig, ax13 = plt.subplots()

ax13.scatter(np.array(Excluded_gLneqgR["Scot_DM"])/1000., np.array(Excluded_gLneqgR["NormSI_N"]), c='red',linewidth = '1.0', marker="*", zorder=10, label=" Excluded (M$_{Z^\prime} <$ 5.0 TeV)")

ax13.scatter(np.array(Accepted_gLneqgR["Scot_DM"])/1000., np.array(Accepted_gLneqgR["NormSI_N"]), c='blue',linewidth = '1.0', marker="*", zorder=12, label="Accepted (M$_{Z^\prime} \geq $ 5.0 TeV)")

ax13.text(0.025, 1.2e-3, r"$\displaystyle g_L \neq g_R = 0.37 $", size=20)


sc13 = ax13.plot(XENONWIMPMASS/1000., XENON1TXSECTION, c='lime',label=r"${\rm\ XENON1T} $",zorder=20, alpha=0.6, linewidth = '3.0')

ax13.fill_between(XENONWIMPMASS/1000, XENON1TXSECTION, ymax, facecolor = 'navy', interpolate=True, alpha=.2,linewidth=0.0, zorder=5, label=r"$\displaystyle {\rm\ Excluded\ by\ XENON1T} $")

xmin = 0.0
xmax = 0.90
ymin = 1e-20
ymax = 1e-6

ax13.axis([xmin,xmax,ymin,ymax])
plt.xlabel(r"$\displaystyle m_{n_e} $ [TeV]", fontsize=20)
plt.ylabel(r"$\displaystyle \sigma_{SI}^{\rm neutron} \rm Min \left( 1, \frac{\Omega_{\rm DM}}{\Omega_{\rm Planck}}\right)$ [pb]", fontsize=20)
#plt.ylabel(r"$\displaystyle \sigma_{SI}^n $ [pb]", fontsize=20)

ax13.xaxis.set_major_locator(MultipleLocator(0.1))
ax13.xaxis.set_minor_locator(MultipleLocator(0.025))

#ax13.yaxis.set_major_locator(MultipleLocator(5))
#ax13.yaxis.set_minor_locator(MultipleLocator(1))

plt.yscale('log')

# Set both ticks to be outside
ax13.tick_params(which='both', direction='out')

#plt.legend(loc='best',frameon=True)
leg = plt.legend(loc='lower right',frameon=True)
leg.set_zorder(100)

fig.savefig("/home/phylab/projects/ALRM_gLneqgR/plot/MassNRvsNormSIxsection_neutron_gLneqgR_II.png")   # save the figure to file
plt.close(fig)


############################################    Plot #9 ####################################################


pylab.rcParams['figure.figsize'] = (8.0, 6.0)

cm = plt.cm.get_cmap('rainbow')

fig, ax14 = plt.subplots()

#xx = np.array(Accepted_gLneqgR["Scot_DM"])
#yy = np.array(Accepted_gLneqgR["Scot_mu"])

#col = yy - xx
col = np.array(Accepted_gLneqgR["mh3"])

sc14 = ax14.scatter(np.array(Accepted_gLneqgR["Scot_DM"])/1000., np.array(Accepted_gLneqgR["omegah2"]), c=col, cmap=cm ,marker='.', s=10, label=r"$ {\rm\ ALRM\ (M_{Z^\prime} > 5.0\ TeV)} $", zorder=55)

#cbar14 = plt.colorbar(sc14, format = "%.0f", extend="both")
cbar14 = plt.colorbar(sc14)
cbar14.set_label(r"$\displaystyle \lambda_3 $", fontsize=20)


#ax14.scatter(np.array(Excluded_gLneqgR["Scot_DM"])/1000., np.array(Excluded_gLneqgR["omegah2"]), c='red',linewidth = '1.0', marker="*", zorder=10, label=" Excluded (M$_{Z^\prime} <$ 5.0 TeV)")

#ax14.scatter(np.array(Accepted_gLneqgR["Scot_DM"])/1000., np.array(Accepted_gLneqgR["omegah2"]), c='blue',linewidth = '1.0', marker="*", zorder=12, label="Accepted (M$_{Z^\prime} \geq$ 5.0 TeV)")

    
ax14.text(0.3, 1.5e4, r"$\displaystyle g_L \neq g_R = 0.37 $", size=15)

xmin = 0.0
xmax = 0.9
ymin = 4e-5
ymax = 1e4

ax14.axhspan(0.096,0.122,color='green',fill=True,alpha=.2,linewidth=0.0,zorder=50, label="Planck bound")

mh0_mass = 125.09
mh0_min = (mh0_mass-15.)/1000.
mh0_max = (mh0_mass+15.)/1000.
ax14.axvspan(mh0_min/2., mh0_max/2., color='purple',fill=True,alpha=.2,linewidth=0.0,zorder=50, label="H$_0$ Funnel")

mZ_mass = 91.1876
mZ_min = (mZ_mass-15.)/1000.
mZ_max = (mZ_mass+15.)/1000.
ax14.axvspan(mZ_min/2., mZ_max/2., color='blue',fill=True,alpha=.2,linewidth=0.0,zorder=50, label="Z Funnel")

ax14.axis([xmin,xmax,ymin,ymax])
plt.xlabel(r"$\displaystyle m_{n_e} {\rm\ [TeV]}$", fontsize=20)
plt.ylabel(r"$\displaystyle \Omega_{\rm DM} h^2 $ ", fontsize=20)




ax14.axis([xmin,xmax,ymin,ymax])
plt.xlabel(r"$\displaystyle m_{n_e} {\rm\ [TeV]}$", fontsize=20)
plt.ylabel(r"$\displaystyle \Omega_{\rm DM} h^2 $ ", fontsize=20)


ax14.xaxis.set_major_locator(MultipleLocator(0.1))
ax14.xaxis.set_minor_locator(MultipleLocator(0.025))

#ax14.yaxis.set_major_locator(MultipleLocator(5))
#ax14.yaxis.set_minor_locator(MultipleLocator(1))

plt.yscale('log')

# Set both ticks to be outside
ax14.tick_params(which='both', direction='out')

#plt.legend(loc='upper left',frameon=True)
leg = plt.legend(loc='lower right',frameon=True)
leg.set_zorder(100)

fig.savefig("/home/phylab/projects/ALRM_gLneqgR/plot/MassNRvsRelic_gLneqgR_lm3.png", dpi=300)   # save the figure to file
plt.close(fig)


############################################    Plot #10 ####################################################


pylab.rcParams['figure.figsize'] = (8.0, 6.0)

cm = plt.cm.get_cmap('rainbow')

fig, ax15 = plt.subplots()

#xx = np.array(Accepted_gLneqgR["Scot_DM"])
#yy = np.array(Accepted_gLneqgR["Scot_mu"])
#col = yy - xx

#col = np.array(Accepted_gLneqgR["Scot_DM"])/np.array(Accepted_gLneqgR["mh2"])
col = np.array(Accepted_gLneqgR["mh3"])

sc15 = ax15.scatter(np.array(Accepted_gLneqgR["Scot_DM"])/1000., np.array(Accepted_gLneqgR["omegah2"]), c=col, cmap=cm ,marker='.', s=10, label=r"$ {\rm\ ALRM\ (M_{Z^\prime} > 5.0\ TeV)} $", zorder=55)

#cbar15 = plt.colorbar(sc15, format = "%.0f", extend="both")
cbar15 = plt.colorbar(sc15)
 

cbar15.set_label(r"$\displaystyle \frac{m_{n_e}}{m_{h_2}} $", fontsize=20)


#ax15.scatter(np.array(Excluded_gLneqgR["Scot_DM"])/1000., np.array(Excluded_gLneqgR["omegah2"]), c='red',linewidth = '1.0', marker="*", zorder=10, label=" Excluded (M$_{Z^\prime} <$ 5.0 TeV)")

#ax15.scatter(np.array(Accepted_gLneqgR["Scot_DM"])/1000., np.array(Accepted_gLneqgR["omegah2"]), c='blue',linewidth = '1.0', marker="*", zorder=12, label="Accepted (M$_{Z^\prime} \geq$ 5.0 TeV)")

    
ax15.text(0.3, 1.5e4, r"$\displaystyle g_L \neq g_R = 0.37 $", size=15)

xmin = 0.0
xmax = 0.9
ymin = 4e-5
ymax = 1e4

ax15.axhspan(0.096,0.122,color='green',fill=True,alpha=.2,linewidth=0.0,zorder=50, label="Planck bound")

mh0_mass = 125.09
mh0_min = (mh0_mass-15.)/1000.
mh0_max = (mh0_mass+15.)/1000.
ax15.axvspan(mh0_min/2., mh0_max/2., color='purple',fill=True,alpha=.2,linewidth=0.0,zorder=50, label="H$_0$ Funnel")

mZ_mass = 91.1876
mZ_min = (mZ_mass-15.)/1000.
mZ_max = (mZ_mass+15.)/1000.
ax15.axvspan(mZ_min/2., mZ_max/2., color='blue',fill=True,alpha=.2,linewidth=0.0,zorder=50, label="Z Funnel")

ax15.axis([xmin,xmax,ymin,ymax])
plt.xlabel(r"$\displaystyle m_{n_e} {\rm\ [TeV]}$", fontsize=20)
plt.ylabel(r"$\displaystyle \Omega_{\rm DM} h^2 $ ", fontsize=20)


ax15.xaxis.set_major_locator(MultipleLocator(0.1))
ax15.xaxis.set_minor_locator(MultipleLocator(0.025))

#ax15.yaxis.set_major_locator(MultipleLocator(5))
#ax15.yaxis.set_minor_locator(MultipleLocator(1))

plt.yscale('log')

# Set both ticks to be outside
ax15.tick_params(which='both', direction='out')

#plt.legend(loc='upper left',frameon=True)
leg = plt.legend(loc='lower right',frameon=True)
leg.set_zorder(100)

fig.savefig("/home/phylab/projects/ALRM_gLneqgR/plot/MassNRvsRelic_gLneqgR_mh2divmDM.png", dpi=300)   # save the figure to file
plt.close(fig)

"""
