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

pyp.ion()

#first, create a contour plot for sin(x)*sin(y) (and make it look nice!)


#second, in a separate figure, plot the function sin^2 (x)
#write a short programme to integrate this function using the trapzoidal rule (integral ~ (b-a)*(f(b)+f(a))/2.)), where the length of the interval b-a can be given to the function as a parameter
def app_integrate (interval, upperlimit):
#plot this function for some different values of the interval, to see how well it converges

#########################################
#finally, replot the contour figure and make the second figure an inset of the contour plot figure
fig, ax = pyp.subplots()
