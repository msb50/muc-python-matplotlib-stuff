import numpy as n
from matplotlib import pyplot as pyp
from matplotlib.path import Path
import matplotlib.patches as patches
import matplotlib.animation as animation
from matplotlib.collections import PatchCollection


#make a sketch of a 6*6 plane of square fields
#pull some walls through this plane, and occupy some of the fields with players (denoted by circles) of different colours

fig = pyp.figure(figsize = (6,6))
ax = pyp.axes([0,0,1,1]); pyp.ylim([0,6]); pyp.xlim([0,6])

