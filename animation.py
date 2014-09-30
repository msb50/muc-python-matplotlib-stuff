import matplotlib.pyplot as plt
import numpy as np
import matplotlib.animation as animation


y, x = np.meshgrid(np.linspace(-3, 3,100), np.linspace(-3, 3,100))

z = np.sin(x)*np.sin(y)
z = z[:-1, :-1]

ax = plt.subplot(111)

quad = plt.pcolormesh(x, y, z)

plt.colorbar()

plt.ion()
plt.show()

#for phase in np.linspace(0,10*np.pi,200):
#    z = np.sin(x+phase)*np.sin(y*phase) 
#    z = z[:-1, :-1]
#
#    quad.set_array(z.ravel())
#    plt.title('Phase: %.2f'%phase)
#    plt.draw()
#
#plt.ioff()
#plt.show()


########################################################

phases = np.linspace(0,10*np.pi,200)

def animate(i, phases, x, y):
  phase = phases[i]
  z = np.sin(x+phase)*np.sin(y*phase)
  plt.contourf(x,y,z)
  return None,

plt.ion()
fig, ax = plt.subplots();plt.ylim([-3,3]); plt.xlim([-3,3])
anim = animation.FuncAnimation(fig, animate, 200 , 
                                 fargs = (phases, x, y),repeat = False)
pyp.show() 
#anim.save('anim_test.mp4',codec='libx264',fps=20)
