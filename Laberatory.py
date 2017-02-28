#------------------------------------------------imports---------------------------------------------------------------
from pylab import imshow, show, get_cmap
from numpy import random
import scipy.ndimage
import matplotlib.pyplot as plt
import os

#-------------------------------------------------settings-------------------------------------------------------------
SAVE = True
SHOW = False
ITERATIONS = 15

#--------------------------------------------------sizing--------------------------------------------------------------
size = 100


#--------------------------------------------------creating------------------------------------------------------------
Z= random.random((size,size))


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

#-------------------------------------------------filtering------------------------------------------------------------
for i in range(ITERATIONS):

    Z = scipy.ndimage.filters.percentile_filter(Z,50,size=50)

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