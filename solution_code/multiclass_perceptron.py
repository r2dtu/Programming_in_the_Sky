# (a) Load in the data set data0.txt. This has 2-d data in four classes
# (coded as 0,1,2,3). Each row consists of three numbers: the two
# coordinates of the data points and the label.
# (b) Run the multiclass Perceptron algorithm to learn a classifier.
# Create a plot that shows all the data points (with different colors
# and shapes for different labels) as well as the decision region

import numpy as np
import matplotlib.pyplot as plt
import random
from sklearn.linear_model import Perceptron
from mlxtend.plotting import plot_decision_regions

# w is a k-dimensional vector of d-dimensional vectors
# b is a k-dimensional vector of scalar terms
# Prediction: On instance x , predict label arg maxj (wj · x + bj )
def multiclass_label(w, b, x):
	results = np.zeros(len(w))
	for i in range(len(w)):
		results[i] = w[i].dot(x) + b[i]
	return np.argmax(results)

# Setting: X = Rd and Y = {1,2,...,k}
def multiclass_perceptron(data, labels):

	# Get data dimensions d and number of classes k
	d = len(data[0])
	k = len(np.unique(labels))

	# Model: w1,...,wk ∈ Rd and b1,...,bk ∈ R
	# Initialize k w-vectors in d-dimensions and k b-values
	w = np.zeros(d)
	w = [w for i in range(k)]
	b = np.zeros(k)

	# Repeat while some training point (x,y) is misclassified:
	idx_arr = list(range(len(data)))
	changed = True
	while changed != False:
		changed = False
		random.shuffle(idx_arr)
		for i in idx_arr:
			predict = multiclass_label(w, b, data[i])
			actual = labels[i]
			if predict != actual:
				# for correct label y:
				w[actual] = w[actual] + data[i]
				b[actual] = b[actual] + 1
				# for predicted label y:
				w[predict] = w[predict] - data[i]
				b[predict] = b[predict] - 1
				changed = True

	return w, b

input_data = np.loadtxt('data0.txt')
data = input_data[:, [0, 1]].astype(int)
labels = input_data[:, 2].astype(int)

# Multiclass perceptron
w, b = multiclass_perceptron(data, labels)

# Plot the decision boundaries (fit something random so it's happy)
clf_m = Perceptron()
clf_m.fit(np.random.randint(2, size=(4, 2)), np.arange(0, 4).reshape(4, 1))
clf_m.coef_ = np.asarray(w)
clf_m.intercept_ = b
plot_decision_regions(data, labels, clf_m)
plt.show()

