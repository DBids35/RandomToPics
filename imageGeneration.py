from pylab import imshow, show, get_cmap
from numpy import random
import scipy.ndimage
Z= random.random((100,100))

for i in range(50):
    Z=scipy.ndimage.filters.median_filter(Z, size=(2,2))

Z = scipy.ndimage.filters.sobel(Z)
imshow(Z, cmap=get_cmap("Spectral"), interpolation='nearest')
show()

#comment