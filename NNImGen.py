from pylab import imshow, show, get_cmap
from numpy import random
import scipy.ndimage
Z= random.random((10,10))
print(Z[5][5])
imshow(Z, cmap=get_cmap("Spectral"), interpolation='nearest')
show()