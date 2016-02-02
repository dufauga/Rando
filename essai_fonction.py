# -*- coding: utf-8 -*-
"""
Created on Tue Feb 02 15:22:55 2016
Projet collaboratif
@author: Amelie, Leonida and Amandine
"""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib import animation

#Une fonction

x=np.linspace(-30.,30.,10000)

def fonc(x):
  """ 
  Une fonction mathématique qui fait un sinus cardinal
  
  Entrées: x
  
  Sortie y qui est un SinC
  """

  return np.sin(x)/x
  
y=fonc(x)
  
fig=plt.figure("Sinus cardinal")
plt.clf()
line, = plt.plot([],[])
plt.xlim(-30.,30.)
plt.ylim(-2.,2.)

def init():
    line.set_data([],[])
    return line,

dx=.1    
def animate(i):
    x2=x+i*dx
    y=fonc(x2)
    line.set_data(x, y)
    return line,
    
anim = animation.FuncAnimation(fig, animate, init_func=init, 
                               frames=1000, interval=20, blit=True)

plt.show()

  
#Affichage
  
  #j'y comprends rien