#------------------------------------------------imports---------------------------------------------------------------
from pylab import imshow, show, get_cmap
from numpy import random
import scipy.ndimage
import matplotlib.pyplot as plt
import os

#-------------------------------------------------settings-------------------------------------------------------------
SAVE = False
SHOW = True
ITERATIONS = 5

#--------------------------------------------------sizing--------------------------------------------------------------
size = 250

#--------------------------------------------------creating------------------------------------------------------------
Z= random.random((size,size))


#-------------------------------------------------filtering------------------------------------------------------------
for i in range(ITERATIONS):
    Z = scipy.ndimage.filters.median_filter(Z, size=(size/10,size/10))
    Z = scipy.ndimage.filters.median_filter(Z, size=(size/10, size/10))

    Z = scipy.ndimage.filters.gaussian_gradient_magnitude(Z, 1)

#Z = scipy.ndimage.filters.sobel(Z)

#---------------------------------------------------plotting-----------------------------------------------------------

    plt.subplot(2, 2, 1)
    imshow(Z, cmap=get_cmap("Spectral"), interpolation='bicubic')
    plt.subplot(2, 2, 2)
    plt.imshow(Z, cmap=get_cmap('cubehelix'), interpolation='bicubic')
    plt.subplot(2, 2, 3)
    imshow(Z, cmap=get_cmap("copper"), interpolation='bicubic')
    plt.subplot(2, 2, 4)
    imshow(Z, cmap='gray', interpolation='bicubic')


    #----------------------------------------------------saving------------------------------------------------------------
    if SAVE:
        filename = 'output'
        i = 0
        while os.path.exists('{}{:d}.png'.format(filename, i)):
            i += 1
        plt.savefig('{}{:d}.png'.format(filename, i))
        print('saved')

#--------------------------------------------------displaying----------------------------------------------------------
if SHOW:
    show()


#-----------------------------------------------------END--------------------------------------------------------------