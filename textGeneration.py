from pylab import imshow, show, get_cmap
from numpy import random
import scipy.ndimage
Z= random.random((100,100))>.5

for i in range(1):
    Z=scipy.ndimage.filters.median_filter(Z, size=(3, 1))
    Z=scipy.ndimage.filters.median_filter(Z, size=(1,3))

# Z = scipy.ndimage.filters.sobel(Z)

imshow(Z, cmap="gray", interpolation='nearest')
show()

#comment