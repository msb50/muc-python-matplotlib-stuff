import numpy as n
from matplotlib import pyplot as pyp
import matplotlib

font = {'family' : 'sans-serif',
        'weight' : 'normal',
        'size'   : 20}

matplotlib.rc('font', **font)
matplotlib.rc('text', usetex=True)

def integral(x): return 0.5*x-0.25*n.sin(2*x)

def f(x): return n.sin(x)**2

def app_integrate(interval,upperlimit):
  sum = 0.
  steps = int(upperlimit/interval)
  prevlim=0.
  for i in range(1,steps+1):
    term = interval*(f(prevlim)+f(i*interval))/2.
    prevlim=i*interval
    sum+=term
  sum+= (upperlimit-prevlim)*(f(upperlimit)+f(prevlim))/2.
  return sum
   


pyp.ion()

x = n.linspace(0, 10, 100)
X, Y = n.meshgrid(x, x)
Z = (n.sin(X)*n.sin(Y))

fig, ax = pyp.subplots()

levels = n.linspace(-1.5, 1.5, 40)
cs = ax.contourf(X, Y, Z, levels=levels, cmap = pyp.cm.Reds)
#fig.colorbar(cs, format="%.2f")
pyp.text(0.5,0.5,'sin(x)sin(y)')

cbaxes = fig.add_axes([0.55, 0.2, 0.3, 0.025])
cbar = fig.colorbar(cs,cax=cbaxes, orientation='horizontal', ticks=[-1.,-0.5,0.,0.5,1.])
cbar.ax.set_xticklabels(['-1.','-0.5','0','0.5','1.'], family='sans-serif',size=15)

ax.set_ylim([0,10])
ax.set_xlim([0,10])
ax.set_xlabel(r'$\displaystyle x$')
ax.set_ylabel(r'$\displaystyle y$')
pyp.savefig("contour.pdf",bbox_inches='tight')


##########################################
fig, ax = pyp.subplots()
line,=ax.plot(n.linspace(0,10,100), n.sin(n.linspace(0,10,100))**2,'k',lw=2, label = r'$\displaystyle \sin^2 (x)$')
line.set_dashes([10,4,2,4])
ax.plot(n.linspace(0,10,100),[integral(x) for x in n.linspace(0,10,100)],'k',lw=2, label= r'$\displaystyle \textrm{integral}$')
ax.plot(n.linspace(0,10,100),[app_integrate(1.,x) for x in n.linspace(0,10,100)],'b',lw=2, label= r'$\displaystyle \textrm{trapezoid: step 1}$')
ax.plot(n.linspace(0,10,100),[app_integrate(0.1,x) for x in n.linspace(0,10,100)],'g',lw=2, label=  r'$\displaystyle \textrm{trapezoid: step 0.1}$')
pyp.ylim([-0.5,6])
handles, labels = ax.get_legend_handles_labels()
ax.legend(handles, labels, loc = 2, prop ={"size":19},handletextpad = 0.4, labelspacing =0.5, handlelength = 1.7)
pyp.savefig("integral.pdf",bbox_inches='tight')

#######################################
fig, ax = pyp.subplots()

levels = n.linspace(-1.5, 1.5, 40)
cs = ax.contourf(X, Y, Z, levels=levels, cmap = pyp.cm.Reds)
#fig.colorbar(cs, format="%.2f")
pyp.text(0.5,0.5,'sin(x)sin(y)')

cbaxes = fig.add_axes([0.55, 0.2, 0.3, 0.025])
cbar = fig.colorbar(cs,cax=cbaxes, orientation='horizontal', ticks=[-1.,-0.5,0.,0.5,1.])
cbar.ax.set_xticklabels(['-1.','-0.5','0','0.5','1.'], family='sans-serif',size=15)

ax.set_ylim([0,10])
ax.set_xlim([0,10])
ax.set_xlabel(r'$\displaystyle x$')
ax.set_ylabel(r'$\displaystyle y$')

newfig = fig.add_axes([0.48,0.45,0.4,0.4])
newfig.plot(n.linspace(0,10,100), n.sin(n.linspace(0,10,100)),lw=2)
line,=newfig.plot(n.linspace(0,10,100), n.sin(n.linspace(0,10,100))**2,'k',lw=2, label = r'$\displaystyle \sin^2 (x)$')
line.set_dashes([10,4,2,4])
newfig.plot(n.linspace(0,10,100),[integral(x) for x in n.linspace(0,10,100)],'k',lw=2, label= r'$\displaystyle \textrm{integral}$')
newfig.plot(n.linspace(0,10,100),[app_integrate(1.,x) for x in n.linspace(0,10,100)],'b',lw=2, label= r'$\displaystyle \textrm{trapezoid: step 1}$')
newfig.plot(n.linspace(0,10,100),[app_integrate(0.1,x) for x in n.linspace(0,10,100)],'g',lw=2, label=  r'$\displaystyle \textrm{trapezoid: step 0.1}$')
newfig.set_ylim([-0.5,6])
handles, labels = newfig.get_legend_handles_labels()
ax.legend(handles, labels, loc = 2, prop ={"size":15},handletextpad = 0.4, labelspacing =0.5, handlelength = 1.7)
pyp.savefig("contour_with_inset.pdf",bbox_inches='tight')

