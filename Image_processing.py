#Image processing - class-1
##-- For comments. 
#:/user/bin/python
#Import blocks
import matplotlib.pyplot as plt
from scipy import misc, ndimage

face = misc.face() #create the face array

#Use different gaussian kernels for smoothing
blurred_face = ndimage.gaussian_filter(face, sigma=3)
very_blurred = ndimage.gaussian_filter(face, sigma=15)

#draw the image

plt.imshow(very_blurred)

#show the image
plt.show()
