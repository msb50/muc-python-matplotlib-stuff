import matplotlib.pyplot as pyp
import numpy as n
import matplotlib.animation as animation

y, x = n.meshgrid(n.linspace(-3, 3,100), n.linspace(-3, 3,100))

z = n.sin(x)*n.sin(y)
z = z[:-1, :-1]

ax = pyp.subplot(111)

quad = pyp.pcolormesh(x, y, z)

pyp.colorbar()

pyp.ion()
pyp.show()

for phase in n.linspace(0,10*n.pi,200):
    z = n.sin(x+phase)*n.sin(y*phase) 
    z = z[:-1, :-1]

    quad.set_array(z.ravel())
    pyp.title('Phase: %.2f'%phase)
    pyp.draw()

pyp.ioff()
pyp.show()

