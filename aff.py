### #import subprocess
import numpy as np
from matplotlib import pyplot as plt
import pylab
from matplotlib import ticker
import math
#############################"" DONNEES #############################################
from scipy.stats import linregress

#### erreur uref-uH

#k=1.2, 1.0 ,  0.8 ,0.7 ,0.5, 0.4 , 0.2
# mesh Th2 = buildmesh( a(k*12) + b(k*25) + c(k*12) + d(k*85) + e(k*20) + h(k*110)); // uniforme pour domaine 20
#mesh Th2=buildmesh( a(k*12) + b(k*45) + c(k*42) + d(k*125) + e(k*25) + h(k*110)); // raffi pour domaine 20
# algo newton avec ref sur raffi k=3

###  (cv en 2/3 et 4/3)

errH1=[0.013485,0.016039,0.024262,0.0171801, 0.027245,0.0300035,0.0447295]
errL2=[0.00145441,0.00240175,0.00431993,0.00280512, 0.00546401, 0.00924979,0.016697]
h=[0.0619233,0.0749581,0.0927144,0.125798,0.146349,0.240487,0.361212]

h2=[he**2 for he in h]
h23=[he**(2/3) for he in h]
print(h23)
h43=[he**(4/3) for he in h]


(a,b,_,_,_)=linregress(np.log(h),np.log(h23))
print(a," ",b)
(a,b,_,_,_)=linregress(np.log(h),np.log(h43))
print(a," ",b)


#(aH1e,bH1e,_,_,_)=linregress(h,errH1e) 
#lH1e=[aH1e*he+bH1e for he in h] #zoom ligne
##########################################################"

(aH1,bH1,_,_,_)=linregress(h,errH1) 
lH1=[aH1*he+bH1 for he in h] #entier ligne
print(aH1," ",lH1)
(aH1,bH1,_,_,_)=linregress(np.log(h),np.log(errH1)) #entier coeff h1

#######################################################

(aHH1,bHH1,_,_,_)=linregress(h,errL2) 
lHH1=[aHH1*he+bHH1 for he in h] #entier ligne
print(aHH1," ",lHH1)
(aHH1,bHH1,_,_,_)=linregress(np.log(h),np.log(errL2)) #entier coeff h1


'''
(aL2,bL2,_,_,_)=linregress(h,errL2)
l2=[aL2*he+bL2 for he in h] #entier ligne L2

(aL2,bL2,_,_,_)=linregress(np.log10(h),np.log10(errL2))#entier coef l2

(aL2e,bL2e,_,_,_)=linregress(h,errL2e)  #zoom ligne l2
l2e=[aL2e*he+bL2e for he in h]

(aL2e,bL2e,_,_,_)=linregress(np.log10(h),np.log10(errL2e)) #zoom coef l2
'''

####################" AFFICHAGE ###########################################################

fig1, (ax1,ax2) = plt.subplots(1,2,figsize=(25,15))
#ax1.plot(N,erreo3sur2,label='NIRB error',marker='o',linewidth = 3,markersize=10,color='red')
ax1.plot(h,errH1,label='H1 error proj',marker='o',linewidth = 5,markersize=10,color='green')
#ax1.plot(h,NIRB,label='H1 error ',marker='o',linewidth = 3,markersize=10,color='green')
ax1.plot(h,[he**2 for he in h],label='$h^2$',linewidth = 3,linestyle='--',marker='*',markersize=10,color='black')
ax1.plot(h,[he for he in h],label='$h$',linestyle='--',marker='*',linewidth = 3,markersize=10,color='red')
ax1.plot(h,[he**(2./3) for he in h],label='$h^{2/3}$',linewidth = 3,linestyle='--',marker='D',markersize=10,color='blue')
#ax1.plot(h,lH1e,label='linear reg: $aZ=$'+str(round(aH1e,2)),linewidth = 7,linestyle='--',marker='*',markersize=15,color='red')
ax1.plot(h,lH1,label='linear reg: $c=$'+str(round(aH1,2)),linewidth = 5,linestyle='--',marker='*',markersize=15,color='orange')
ax1.set_xscale('log')
ax1.set_yscale('log')

ax1.legend(loc = 'upper left',prop={'size': 30})
#axes.tick_params(axis = 'both', labelsize = 28)
ax1.set_title("$ H^1 \ relative \ error $",fontsize=38)

ax1.set_xlabel("$h$ (size of the mesh)", fontsize = 20)
ax1.set_ylabel("Error (log scale)",fontsize=20)
ax1.xaxis.set_major_locator(ticker.MultipleLocator(0.1))
ax1.xaxis.set_major_formatter(ticker.ScalarFormatter())
ax1.xaxis.set_minor_formatter(ticker.ScalarFormatter())
ax1.ticklabel_format(style='plain',axis='x',useOffset=False)
#ax1.yaxis.set_minor_locator(ticker.FixedLocator([0.0001,0.0005,0.001,0.003,0.005,0.006,0.008,0.01,0.02]))
#ax1.yaxis.set_minor_locator(ticker.FixedLocator([5e-5,1e-4,5e-4,0.001,0.003,0.005,0.006,0.008,0.01,0.02,0.03,0.04,0.06,0.08,0.1]))
#ax1.yaxis.set_major_locator(ticker.NullLocator())

#ax1.yaxis.set_major_locator(ticker.FixedLocator([0.1]))
ax1.xaxis.set_minor_formatter(ticker.ScalarFormatter())

ax1.xaxis.set_minor_locator(ticker.NullLocator())
ax1.tick_params(axis = 'both', labelsize = 20)
ax1.yaxis.set_tick_params(which = 'minor', length = 15, width = 3,
                           color = 'black', labelsize = 20, labelcolor = 'black')
ax1.yaxis.set_tick_params(which = 'major', length = 15, width = 3,
                           color = 'black', labelsize = 20, labelcolor = 'black')

ax1.xaxis.set_tick_params(which = 'major', length = 15, width = 3,
                           color = 'black', labelsize = 20, labelcolor = 'black')

ax1.xaxis.set_tick_params(which = 'minor', length = 15, width = 3,
                           color = 'black', labelsize = 20, labelcolor = 'black')

ax2.plot(h,errL2,label='L2 error ',marker='o',linewidth = 5,markersize=10,color='green')
#ax2.plot(h,Erruh,label='H1 proj error',marker='o',linewidth = 5,markersize=15,color='red')
#ax2.plot(H,errL2,label='L2 error',marker='o',linewidth = 5,markersize=12,color='green')
ax2.plot(h,[he**2 for he in h],label='$h^2$',linewidth = 3,linestyle='--',marker='*',markersize=10,color='black')
ax2.plot(h,[he**(4/3) for he in h],label='$h^{4./3}$',linestyle='--',marker='D',linewidth=3,markersize=10,color='blue')
ax2.plot(h,[he for he in h],label='$h$',linestyle='--',marker='*',linewidth=2,markersize=10,color='red')
#ax2.plot(H,[he**(4./3) for he in H],label='$h^{4./3}$',linestyle='--',marker='D',linewidth=3,markersize=10,color='blue')
ax2.plot(h,lHH1,label='linear reg: $c=$'+str(round(aHH1,2)),linewidth = 5,linestyle='--',marker='*',markersize=15,color='orange')
#ax2.plot(h,l2e,label='linear reg: $aZ=$'+str(round(aL2e,2)),linewidth = 5,linestyle='--',marker='*',markersize=15,color='red')

#ax2.get_yaxis().set_visible(False)

ax2.set_xscale('log')
ax2.set_yscale('log')
ax2.set_xlabel("$h$ (size of the mesh)",fontsize=20)
ax2.xaxis.set_major_locator(ticker.MultipleLocator(0.1))
ax2.xaxis.set_major_formatter(ticker.ScalarFormatter())
ax2.xaxis.set_minor_formatter(ticker.ScalarFormatter())
ax2.ticklabel_format(style='plain',axis='x',useOffset=False)
ax2.xaxis.set_minor_locator(ticker.NullLocator())
#ax2.yaxis.set_minor_locator(ticker.FixedLocator([0.03,0.08,0.1]))
#ax2.yaxis.set_major_locator(ticker.NullLocator())
#ax2.yaxis.set_minor_formatter(ticker.ScalarFormatter())

ax2.xaxis.set_tick_params(which = 'major', length = 15, width = 3,
                           color = 'black', labelsize = 20, labelcolor = 'black')
ax2.yaxis.set_tick_params(which = 'minor', length = 15, width = 3,
                           color = 'black', labelsize = 20, labelcolor = 'black')
ax2.yaxis.set_tick_params(which = 'major', length = 15, width = 3,
                           color = 'black', labelsize = 20, labelcolor = 'black')
ax2.xaxis.set_tick_params(which = 'minor', length = 15, width = 3,
                           color = 'black', labelsize = 20, labelcolor = 'black')
ax2.legend(loc = 'upper left',prop={'size': 30})

ax2.set_title("$ L^2 \ relative \ error $",fontsize=38)
#plt.title("$\mathbf{\ H1 and L2 \ relative \ error\ of Poisson equation in L-shape domain }$",fontsize=38)



########### Attention au titre!!
fig1.suptitle("$\mathbf{Relative \ errors \ with \ uniform \ meshes}$",fontsize=38) 
#plt.show()
plt.savefig('steadystokesUnif.eps',format='eps')
