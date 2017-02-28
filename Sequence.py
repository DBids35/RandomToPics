#------------------------------------------------imports---------------------------------------------------------------
from pylab import imshow, show, get_cmap
from numpy import random
import scipy.ndimage
import matplotlib.pyplot as plt
import os

#-------------------------------------------------settings-------------------------------------------------------------
SAVE = True
SHOW = False
ITERATIONS = 50

#--------------------------------------------------sizing--------------------------------------------------------------
size = 250

#--------------------------------------------------creating------------------------------------------------------------
Z= random.random((size,size))

imshow(Z, cmap=get_cmap("Spectral"), interpolation='bicubic')

if SAVE:
    filename = 'output'
    i = 0
    while os.path.exists('{}{:d}.png'.format(filename, i)):
        i += 1
    plt.savefig('{}{:d}.png'.format(filename, i))
    print('saved')


#-------------------------------------------------filtering------------------------------------------------------------
for i in range(ITERATIONS):
    Z = scipy.ndimage.filters.median_filter(Z, size=(size/83,size/10))
    #Z = scipy.ndimage.filters.median_filter(Z, size=(size/10, size/83))

    #Z = scipy.ndimage.filters.gaussian_gradient_magnitude(Z, 1)

#Z = scipy.ndimage.filters.sobel(Z)

#---------------------------------------------------plotting-----------------------------------------------------------


    imshow(Z, cmap=get_cmap("Spectral"), interpolation='bicubic')



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