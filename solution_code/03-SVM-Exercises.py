import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
import plotfuncs as pf

# Load Iris set
iris = load_iris()
data, labels = iris.data[:100], iris.target[:100]
data = data[:, (1, 3)]

# Plot with sepal width / petal width
plt.scatter(data[:, 0], data[:, 1], c=labels, cmap='autumn');
plt.xlabel(iris.feature_names[1])
plt.ylabel(iris.feature_names[3])
plt.show()

# Support Vector Classifier
from sklearn.svm import SVC
clf = SVC(kernel='linear', C=10)
clf.fit(data, labels)

# Plot SVC decision
plt.scatter(data[:, 0], data[:, 1], c=labels, cmap='autumn');
pf.plot_svc_decision_function(clf)
plt.show()

# Plot support vectors
plt.scatter(data[:, 0], data[:, 1], c=labels, cmap='autumn');
plt.scatter(clf.support_vectors_[:, 0], clf.support_vectors_[:, 1])
pf.plot_svc_decision_function(clf)
plt.show()

# Exercise 3
data, labels = iris.data, iris.target
data = data[:, (1, 3)]

# Plot with sepal width / petal width
plt.scatter(data[:, 0], data[:, 1], c=labels, cmap='autumn');
plt.xlabel(iris.feature_names[1])
plt.ylabel(iris.feature_names[3])
plt.show()

# Support Vector Classifier
clf = SVC(kernel='linear')
clf.fit(data, labels)

# Plot SVC decision
plt.scatter(data[:, 0], data[:, 1], c=labels, cmap='autumn');
pf.plot_svc_decision_function(clf)
plt.show()

# Plot support vectors
plt.scatter(data[:, 0], data[:, 1], c=labels, cmap='autumn');
plt.scatter(clf.support_vectors_[:, 0], clf.support_vectors_[:, 1])
pf.plot_svc_decision_function(clf)
plt.show()
