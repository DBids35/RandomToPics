from scipy import misc
import glob
import os
from numpy import random
from pylab import imshow, show, get_cmap
import numpy as np
X=np.empty((0,4425))
Y=np.empty((0,4425))
os.chdir("TrainingFaces")
for picture in glob.glob("*.jpg"):
    image = misc.imread(picture, flatten=1)
    image=image[:,:59]
    image=image.flatten()
    X = np.vstack([X, image])
y=X


def nonlin(x, deriv=False):
    x=x/255
    if (deriv == True):
        return x * (1 - x)

    return 255 / (1 + np.exp(-x))

np.random.seed(6)

# randomly initialize our weights with mean 0
syn0 = 2 * random.random((4425, 6000)) - 1
syn1 = 2 * random.random((6000, 4425)) - 1

for j in range(200):

    # Feed forward through layers 0, 1, and 2
    l0 = X
    l1 = nonlin(np.dot(l0, syn0))
    l2 = nonlin(np.dot(l1, syn1))

    # how much did we miss the target value?
    l2_error = y - l2

    if (j % 10) == 0:
        print("Error:" + str(np.mean(np.abs(l2_error))))

    # in what direction is the target value?
    # were we really sure? if so, don't change too much.
    l2_delta = l2_error * nonlin(l2, deriv=True)

    # how much did each l1 value contribute to the l2 error (according to the weights)?
    l1_error = l2_delta.dot(syn1.T)

    # in what direction is the target l1?
    # were we really sure? if so, don't change too much.
    # l1_delta = l1_error * nonlin(l1, deriv=True)

    syn1 += l1.T.dot(l2_error)
    syn0 += l0.T.dot(l1_error)

Z=random.random((1,4425))


l1 = nonlin(np.dot(Z, syn0))
l2 = nonlin(np.dot(l1, syn1))
outImage=l2.reshape((75,59))
Z=Z.reshape((75,59))
imshow(Z, cmap="gray", interpolation='nearest')
show()
imshow(outImage, cmap="gray", interpolation='nearest')
show()
