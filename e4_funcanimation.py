import matplotlib.pyplot as pyp
import numpy as n
import matplotlib.animation as animation

pyp.ion()

#animate the contourplot from before by introducing a time-dependent phase and plotting n.sin(x+phase)*n.sin(y*phase)
phases = n.linspace(0,10*n.pi,200)
maxlength = 200

fig, ax = pyp.subplots()

#this can be done using the FuncAnimate module:

def animate (i,...):
  return None, #needs to return an iterator

anim = animation.FuncAnimation(fig, animate, maxlength, 
                                 fargs = (#arguments of animate other than i
                                         ),repeat = False)

