import numpy as n
from matplotlib import pyplot as pyp
import matplotlib

font = {'family' : 'sans-serif',
        'weight' : 'normal',
        'size'   : 20}

matplotlib.rc('font', **font)
matplotlib.rc('text', usetex=True)

def f(x): return 0.5*x**3-2.*x**2+2.5*n.sin(x)-x-0.5

def deriv(x): return 1.5*x**2 -4*x + 2.5*n.cos(x) -1

colours = ['b','r','g','y','c','m','k','Orange','Pink','LightBlue','Brown','Gold']
symbols = ['o','s','^','v','p','*','<','x','d', 'D','*','h','8']

def bisolver(ax,x1,x2):
  count = 0
  while n.round(f(x1),1) !=0:
     x1n, x2n = bisect (x1,x2)
     print count, x2n, f(x2n),colours[count],symbols[count]
     if x1n != x1:
        ax.plot([x1n],[f(x1n)],colours[count],marker=symbols[count],ms=20)
        x1 = x1n; x2 = x2n
     else: 
        ax.plot([x2n],[f(x2n)],colours[count],marker=symbols[count],ms=20)
        x1 = x1n; x2 = x2n
     count+=1
  return x1

def bisect(x1,x2):
  if n.sign(f(x1)*f(x2)) < 0:
    xm = (x1+x2)/2
    if n.sign(f(x1)*f(xm)) >0: x1 = xm 
    else: x2 = xm
    return x1, x2
  else: 
    print "wrong initial conditios"
    return None

pyp.ion() #show images on the fly

#pyp.plot(n.linspace(0.,10.,100.), [f(x) for x in n.linspace(0.,10.,100.) ])
#fig2 = pyp.figure();ax = fig2.add_axes([0.11, 0.15, 0.88, 0.7])
fig, ax = pyp.subplots()
ax.plot(n.linspace(0.,10.,100.), [f(x) for x in n.linspace(0.,10.,100.) ],lw =2, label = 'function')
bisolver(ax,0,8.)
ax.plot(n.linspace(2,8,100),[13*(x-4.7)+11*(x-4.7)**2 for x in n.linspace(2,8,100)], lw=2, label = 'expansion')
handles, labels = ax.get_legend_handles_labels()
ax.legend(handles, labels, loc = 4, prop ={"size":19},handletextpad = 0.4, labelspacing =0.5, handlelength = 1.7)
pyp.xlabel(r'$\displaystyle x$')
pyp.ylabel(r'$\displaystyle y$')
pyp.title('Rootfinding')
pyp.xlim([3.5,6.1])
pyp.ylim([-10,40])
pyp.savefig("rootfinding.pdf",bbox_inches='tight')
#info at: http://matplotlib.org/1.3.1/examples/pylab_examples/line_styles.html
