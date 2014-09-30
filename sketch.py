import numpy as n
from matplotlib import pyplot as pyp
from matplotlib.path import Path
import matplotlib.patches as patches
import matplotlib.animation as animation
from matplotlib.collections import PatchCollection
from copy import *
from subprocess import *


#sketching a figure of ptcs playing games on a percolated grid


def initialise_rects ( nrows ):
  """determines the rectangles for the matplotlib artist"""
  #
  ndims =2  
  ncols = nrows

  #initial rectangles from gridfile
  rects = []
  facecols = ['white']*nrows**2; edgecols = ['black']*nrows**2
  for y0 in range(nrows):
     for x0 in range(ncols):
         rects.append( patches.Rectangle ((x0,y0),1,1 ) )

  return rects, facecols, edgecols

def initialise_circs ( number, nrows ):
  """determines the circles/ptc shapes for the matplotlib artist"""
  ncols = nrows
  circs = []
  for i in range(number):
     x0=int(n.random.random()*nrows)
     y0=int(n.random.random()*nrows)
     circs.append( patches.Circle ((x0+0.5,y0+0.5), 0.3) )

  return circs

pyp.ion()

#initialise grid
ndim = 2; nrows = 6;
fig = pyp.figure(figsize = (6,6))
ax = pyp.axes([0,0,1,1]); pyp.ylim([0,6]); pyp.xlim([0,6])
rects, rfacecols, redgecols = initialise_rects (nrows)
coll = PatchCollection (rects)
coll.set_facecolor(rfacecols)
coll.set_edgecolor(redgecols)

ax.add_collection(coll)

#initialise percolation
verts1 = [ (0,1), (1,1), (1,2), (2,2), (2,3), (3,3), (3,4), (4,4), (4,3), (5,3), (5,2) ]
codes1 = [Path.MOVETO]+ [Path.LINETO]*10
path1 = Path (verts1, codes1)

verts9 = [ (0,5), (1,5), (2,5)]
codes9 = [Path.MOVETO]+ [Path.LINETO]*2
path9 = Path (verts9, codes9)

patch1 = patches.PathPatch(path1, facecolor = 'None', lw=12);
patch9 = patches.PathPatch(path9, facecolor = 'None', lw=12);
ax.add_patch(patch1)
ax.add_patch(patch9)

#initialise particles
circs = initialise_circs (10, nrows)
coll2 = PatchCollection (circs)
colours = ['r'] + ['y'] + ['Pink']+ ['DarkBlue']*2+['Orange','LightBlue']+  ['y','r','g'] 
coll2.set_facecolor(colours)
ax.add_collection(coll2)

ax.set_xticks([])
ax.set_yticks([])

pyp.savefig("random.pdf", bbox_inches = 'tight')

pyp.show()
