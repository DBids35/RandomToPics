from pylab import imshow, show, get_cmap
from numpy import random
import scipy.ndimage
Z= random.random((100,100))
imshow(Z, cmap="gist_rainbow", interpolation='nearest')
show()
for i in range(10):
    Z=scipy.ndimage.filters.median_filter(Z, size=(14-i, 14-i))


# Z = scipy.ndimage.filters.sobel(Z)
imshow(Z, cmap="gist_rainbow", interpolation='nearest')
show()

#comment