# Reading the Image
import matplotlib.pyplot as plt
from scipy import misc,ndimage
brain=plt.imread("Brain.jpg")
plt.imshow(brain)
plt.show()

# Dimensions of the image
brain.shape

# Grey scale image
plt.imshow(brain,cmap='Greys_r')
plt.show()

# Histogram
plt.hist(brain, bins=10)
plt.show()

# Sigma 5 gaussian filter and Histogram
brain_sigma5=ndimage.gaussian_filter(brain, sigma=5)
plt.imshow(brain_sigma5, cmap='Greys_r')
plt.show()
plt.hist(brain_sigma5, bins=10)
plt.show()

# Sigma 10 gaussian filter and Histogram
brain_sigma10=ndimage.gaussian_filter(brain, sigma=10)
plt.imshow(brain_sigma10, cmap='Greys_r')
plt.show()
plt.hist(brain_sigma10, bins=10)
plt.show()

# Sigma 20 gaussian filter and Histogram
brain_sigma20=ndimage.gaussian_filter(brain, sigma=20)
plt.imshow(brain_sigma20, cmap='Greys_r')
plt.show()
plt.hist(brain_sigma20, bins=10)
plt.show()

# Sigma 30 gaussian filter and Histogram
brain_sigma30=ndimage.gaussian_filter(brain, sigma=30)
plt.imshow(brain_sigma30, cmap='Greys_r')
plt.show()
plt.hist(brain_sigma30, bins=10)
plt.show()

# Sigma 40 gaussian filter and Histogram
brain_sigma40=ndimage.gaussian_filter(brain, sigma=40)
plt.imshow(brain_sigma40, cmap='Greys_r')
plt.show()
plt.hist(brain_sigma40, bins=10)
plt.show()

# Sigma 50 gaussian filter and Histogram
brain_sigma50=ndimage.gaussian_filter(brain, sigma=50)
plt.imshow(brain_sigma50, cmap='Greys_r')
plt.show()
plt.hist(brain_sigma50, bins=10)
plt.show()
