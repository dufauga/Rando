# -*- coding: utf-8 -*-
"""
Created on Tue Feb 02 11:03:13 2016

Randonneur avec Python

@author: Grrrrrrrrrrr
"""

# On part d'un profil de montagne envoyé par E.Trouvé - Glacier des Bossons moyenné à 8m

# sample = nb de colo, lines = nd de lignes

# split : sans rien préciser de plus:  enlève saut de ligne espaces tabulation et renvoie ce qui reste

import struct
import numpy as np
#from scipy import interpolate
from scipy.interpolate import griddata

u=np.linspace(0.,5000.,100.)
v=-6./5.*u+6000.

def lire_header(path):
  f = open(path)
  lines = f.readlines()
  f.close()
  out = {}
  for line in lines:
    if "=" in line:
      key= line.split("=")[0].split()[0] # lin se casse sur le = , se qui est à gauche sera la clef
      if key in ["lines","samples"]: # ici permet de na pas lire tout le heder mais juste lines et samples
        out[key] = int(line.split("=")[1])
 # print lines
  return out
  
def read_data(path):
  f = open(path, "rb")
  #data = f.readlinesf.close() 
  #data = f.read()
  #out = struct.unpack(data, "<")
  out = np.fromfile(f, dtype=np.float32)
  f.close()
  return out
  
  
header_path = "BossonsDEM_ll8m.hdr"
header = lire_header(header_path)

data_path = "BossonsDEM_ll8m" # ici c'ets le fichier de données et pas le fichier header
data = read_data(data_path)

dx=1.03112519e1 # en metre
dy=7.19750606e0 # en mètre

nx = header["samples"] # nombre de points en x
ny = header["lines"] # nombre de points en y

x = np.arange(nx) * dx # largeur (en m)
y = (ny - np.arange(ny)) * dy # hauteur (en m) ny - sert à retourner la carte

X, Y = np.meshgrid(x,y) # X et Y sont des vecteurs
Z = data.reshape(ny, nx)

"""
def Altitude(u,v):
    u=int(u*999/x.max())
    v=int(v*549/y.max())
    return u, v
"""

import matplotlib.pyplot as plt
import matplotlib

grad = plt.contourf(X,Y,Z, 100, cmap = matplotlib.cm.terrain) # nappe avec chp de couleur 100 est le nombre de niveaux de couleur

from matplotlib.colors import LightSource

ls=LightSource(azdeg=0,altdeg=65)
rgb= ls.shade(Z,plt.cm.terrain) # on peut mettre aussi cm.terrain


plt.figure(1)
plt.clf()
plt.imshow(rgb, 
           extent=[0,x.max(),0,y.max()], 
           aspect=1, alpha =.5)
cbar = plt.colorbar(grad)
cbar.set_label("Altitude, $z$, [m]")
plt.xlabel("Position, $x$, [m]")
plt.ylabel("Position, $y$, [m]")
plt.contour(X,Y,Z,20, colors = "k")
plt.plot(u,v, "r")
plt.show()

X= X.flatten()
Y=Y.flatten()
Z=Z.flatten()

zi = griddata((X, Y), Z, (u, v), method='cubic')

plt.figure(3)
plt.clf()
plt.plot(u,zi)

"""
for uu in xrange(len(u)):
    for vv in xrange(len(v)):
            uu,vv=Altitude(uu,vv)
            a=Z[uu,vv]
            plt.plot(uu,a)
"""
"""
plt.figure(2)
plt.clf()
plt.plot(u,Z[u,v])
"""