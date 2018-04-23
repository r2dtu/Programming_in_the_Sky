"""
File: multiclass_perceptron.py
Description: Programming in the Sky Workshop 2018 - Advanced Python
Session (Applications of Python: Machine Learning).

Overview of Project:

(a) Load in the data set data0.txt. This has 2-d data in four classes
(coded as 0,1,2,3). Each row consists of three numbers: the two
coordinates of the data points and the label.

(b) Run the multiclass Perceptron algorithm to learn a classifier.
Create a plot that shows all the data points (with different colors
and shapes for different labels) as well as the decision region.

"""

import numpy as np
import matplotlib.pyplot as plt
import random
from sklearn.linear_model import Perceptron
from mlxtend.plotting import plot_decision_regions


def label(w, b, x):
	"""
		w is a k-dimensional vector of d-dimensional vectors
		b is a k-dimensional vector of scalar terms
		Prediction: On instance x, predict label arg maxj (wj · x + bj )
	"""
	# TODO <YOUR CODE HERE>
	# Create an array to store the results of each dot product.
	# Loop through w and b (i.e. with j as your counter)
	# 	a) Calculate wj · x + bj, and record the result.
	# Return the index of the largest result.


def multi_perceptron(data, labels):
	"""
	Setting: X = Rd and Y = {1,2,...,k}
	Model: w1,...,wk ∈ Rd and b1,...,bk ∈ R
	Description: Creates a multi-class Perceptron model.
	"""
	# TODO Your code here. Hopefully the comments above will 
	# lead you in the right direction.

	# 1) Initialize k w-vectors in d-dimensions and k b-values to 0
	# 2) Loop through the entire data set while some training point
	# (x, y), i.e. (data point, label) is misclassified.
	# 	a) Predict a data point x using w and b (call your label
	# 	function).
	# 	b) Check if the prediction matches the actual label. If so,
	# 	do nothing. If not:
	#		aa) for the correct label y:
	#			 - w[y] = w[y] + x
	#			 - b[y] = b[y] + 1
	#			for incorrect label y_:
	#			 - w[y_] = w[y_] - x
	#			 - b[y_] = b[y_] - 1

	return w, b


# Read in a file to classify.
input_data = np.loadtxt('data0.txt')

###############################################################################
# Main program. Do NOT edit any code below this line.
data = input_data[:, [0, 1]].astype(int)
labels = input_data[:, 2].astype(int)

# Run the multiclass perceptron algorithm
w, b = multi_perceptron(data, labels)

# Plot the decision boundaries (fit something random so it's happy)
clf_m = Perceptron()
clf_m.fit(np.random.randint(2, size=(4, 2)), np.arange(0, 4).reshape(4, 1))

# Use the w & b calculated coefficients
clf_m.coef_ = np.asarray(w)
clf_m.intercept_ = b

# Plot the result
plot_decision_regions(data, labels, clf_m)
plt.show()

