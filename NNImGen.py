from pylab import imshow, show, get_cmap
from numpy import random
import numpy as np
import scipy.ndimage

syn0 = 2*np.random.random((10,10)) - 1
syn1 = 2*np.random.random((10,1)) - 1
maxX=100
maxY=100

def spotCheck(Z, x, y):
    a=x
    b=y
    if x<0:
        a=0
    elif x>=maxX:
        a=maxX-1

    if y<0:
        b=0
    elif y>=maxY:
        b=maxY-1
    
    return Z[a][b]


def neuralNet(Z, x,y, maxX, maxY):
    X=[x,y, spotCheck(Z, x-1, y-1),spotCheck(Z,x, y-1),spotCheck(Z,x+1, y-1),spotCheck(Z,x+1, y),spotCheck(Z,x+1, y+1), spotCheck(Z,x, y+1),spotCheck(Z,x-1, y+1),spotCheck(Z,x-1, y) ]

    l1 = 1 / (1 + np.exp(-(np.dot(X, syn0))))
    l2 = 1 / (1 + np.exp(-(np.dot(l1, syn1))))
    # print(l2[0])
    return(l2[0])


Z= random.random((maxX,maxY))
Z2=random.random((maxX,maxY))
for x in range(maxX):
    for y in range(maxY):
        Z2[x][y]=neuralNet(Z,x,y,maxX, maxY)
imshow(Z2, cmap="gray", interpolation='nearest')
show()