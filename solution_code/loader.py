###########################################################################
# Name: David Tu														  #
# PID: A12752135 														  #
# Date: Oct. 25, 2017													  #
# Description: This file reads from the zipped (bytes) MNIST data set 	  #
###########################################################################

from struct import unpack
import gzip
from numpy import zeros, uint8, float32
import numpy as np
from pylab import imshow, show, cm
from progress.bar import IncrementalBar

"""
View a single image.
"""
def view_image(image, label=""):
	print("Label: %s" % label)
	imshow(np.reshape(image, (28,28)), cmap=cm.gray)
	show()

"""
Read input-vector (image) and target class (label, 0-9) and return
it as list of tuples.
"""
def get_labeled_data(imagefile, labelfile):
	# Open the images with gzip in read binary mode
	images = gzip.open(imagefile, 'rb')
	labels = gzip.open(labelfile, 'rb')

	# Read the binary data
	# We have to get big endian unsigned int. So we need '>I'
	# Get metadata for images
	images.read(4)  # skip the magic_number
	number_of_images = images.read(4)
	number_of_images = unpack('>I', number_of_images)[0]
	rows = images.read(4)
	rows = unpack('>I', rows)[0]
	cols = images.read(4)
	cols = unpack('>I', cols)[0]

	# Get metadata for labels
	labels.read(4)  # skip the magic_number
	N = labels.read(4)
	N = unpack('>I', N)[0]

	if number_of_images != N:
		raise Exception('number of labels did not match the number of images')

	# Get the data
	x = zeros((N, rows * cols), dtype=uint8)  # Initialize numpy array
	y = zeros((N, 1), dtype=uint8)  # Initialize numpy array
	bar = IncrementalBar('Processing MNIST data set', max=N)
	for i in range(N):
		for element in range(rows * cols):
			tmp_pixel = images.read(1)  # Just a single byte
			tmp_pixel = unpack('>B', tmp_pixel)[0]
			x[i][element] = tmp_pixel
		tmp_label = labels.read(1)
		y[i] = unpack('>B', tmp_label)[0]
		bar.next()

	bar.finish()
	return (x, y)

###############################################################################
train_labels = "train-labels-idx1-ubyte.gz"
train_images = "train-images-idx3-ubyte.gz"
test_labels = "t10k-labels-idx1-ubyte.gz"
test_images = "t10k-images-idx3-ubyte.gz"

# x is 60000 x 784 array -> each row is an image
# y is the label
train_x, train_y = get_labeled_data(train_images, train_labels)
np.save('training_set_images.npy', train_x)
np.save('training_set_labels.npy', train_y)

# Read in test set
test_x, test_y = get_labeled_data(test_images, test_labels)
np.save('test_set_images.npy', test_x)
np.save('test_set_labels.npy', test_y)

