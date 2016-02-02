# -*- coding: utf-8 -*-
"""
Created on Tue Feb 02 15:22:55 2016
Projet collaboratif
@author: Amelie, Leonida and Amandine
"""

import numpy as np
import matplotlib.pyplot as plt


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
trace=plt.plot(x,y)

  
#Affichage
  
  #j'y comprends rien