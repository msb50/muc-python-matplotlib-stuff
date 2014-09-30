import numpy as n
from matplotlib import pyplot as pyp
import matplotlib

font = {'family' : 'sans-serif',
        'weight' : 'normal',
        'size'   : 20}

matplotlib.rc('font', **font)
matplotlib.rc('text', usetex=True)


pyp.ion() #show images on the fly


#write a rootfinder which finds the root of this function to one digit accuracy, starting from x1 and x2
#plot all the intermediate guesses it needs as dots on the line
#also plot some quadratic function that meets the curve smoothely at the root (eg. a Taylor expansion, or some random guess)


def f(x): return 0.5*x**3-2.*x**2+2.5*n.sin(x)-x-0.5

def expansion(x): 

def rootfind( ax, x1, x2):


colours = ['b','r','g','y','c','m','k','Orange','Pink','LightBlue','Brown','Gold']
symbols = ['o','s','^','v','p','*','<','x','d', 'D','*','h','8']


x1 = 0.; x2 = 8.

fig, ax = pyp.subplots()
ax.plot(n.linspace(0.,10.,100.), [f(x) for x in n.linspace(0.,10.,100.) ],lw =2, label = 'function')
#the expansion
ax.plot( ..., ..., lw =2, label ='expansion')


#legend
handles, labels = ax.get_legend_handles_labels()
ax.legend(handles, labels, loc = 4, prop ={"size":19},handletextpad = 0.4, labelspacing =0.5, handlelength = 1.7)

#pyp.xlim([somewhere, somewhere_else])
#pyp.ylim([somewhere, somewhere_else])
pyp.xlabel(r'$\displaystyle x$')
pyp.ylabel(r'$\displaystyle y$')
pyp.title('Rootfinding')
