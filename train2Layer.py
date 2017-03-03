from scipy import misc
import glob
import os
from numpy import random
from pylab import imshow, show, get_cmap
import numpy as np
import matplotlib.pyplot as plt

X=np.empty((0,4425))
Y=np.empty((0,4425))
os.chdir("TrainingFaces")
for picture in glob.glob("*.jpg"):
    image = misc.imread(picture, flatten=1)
    image=image[:,:59]/225
    image=image.flatten()
    X = np.vstack([X, image])
Y=X


def nonlin(x, deriv=False):
    stretch_factor = 100
    if (deriv == True):
        return x/stretch_factor * (1 - x/stretch_factor)

    return 1 / (1 + np.exp(-x/stretch_factor))

np.random.seed(1)

# randomly initialize our weights with mean 0
syn0 = 2 * random.random((4425,4425)) - 1

for j in range(500):

    # Feed forward through layers 0, 1, and 2
    l0 = X
    l1 = nonlin(np.dot(l0, syn0))

    # how much did we miss the target value?
    l1_error = Y - l1

    if (j % 10) == 0:
        print("Error:" + str(np.mean(np.abs(l1_error))))

    training_coef = 1

    # in what direction is the target l1?
    # were we really sure? if so, don't change too much.
    l1_delta = l1_error * nonlin(l1, deriv=True)*training_coef

    syn0 += l0.T.dot(l1_delta)

Z=random.random((1,4425))

l1 = nonlin(np.dot(Z, syn0))

outImage=l1.reshape((75,59))
Z=Z.reshape((75,59))
plt.subplot(1, 2, 1)
imshow(Z, cmap="gray", interpolation='nearest')
plt.subplot(1, 2, 2)
imshow(outImage, cmap="gray", interpolation='nearest')
show()
