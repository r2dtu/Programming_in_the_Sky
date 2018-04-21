from sklearn.datasets.samples_generator import make_blobs
import matplotlib.pyplot as plt
import numpy as np

def plot_svc_decision_function(clf, ax=None):
    """Plot the decision function for a 2D SVC"""
    if ax is None:
        ax = plt.gca()
    x = np.linspace(plt.xlim()[0], plt.xlim()[1], 30)
    y = np.linspace(plt.ylim()[0], plt.ylim()[1], 30)
    Y, X = np.meshgrid(y, x)
    P = np.zeros_like(X)
    for i, xi in enumerate(x):
        for j, yj in enumerate(y):
            P[i, j] = clf.decision_function([[xi, yj]])
    # plot the margins
    ax.contour(X, Y, P, colors='k',
               levels=[-1, 0, 1], alpha=0.5,
               linestyles=['--', '-', '--'])

# Generate random set
X, y = make_blobs(n_samples=100, centers=2,
                  random_state=0, cluster_std=0.45)
plt.scatter(X[:, 0], X[:, 1], c=y, s=100, cmap='autumn');
plt.show()

# Support Vector Classifier
from sklearn.svm import SVC
clf = SVC(kernel='linear')
clf.fit(X, y)

plt.scatter(X[:, 0], X[:, 1], c=y, s=100, cmap='autumn');
plot_svc_decision_function(clf)
plt.show()

plt.scatter(X[:, 0], X[:, 1], c=y, s=100, cmap='autumn');
plt.scatter(clf.support_vectors_[:, 0], clf.support_vectors_[:, 1])
plot_svc_decision_function(clf)
plt.show()

# Kernel methods
from sklearn.datasets.samples_generator import make_circles
X, y = make_circles(100, factor=.1, noise=.1)

clf = SVC(kernel='linear').fit(X, y)

plt.scatter(X[:, 0], X[:, 1], c=y, s=100, cmap='autumn')
plot_svc_decision_function(clf);
plt.show()

clf = SVC(kernel='rbf')
clf.fit(X, y)

plt.scatter(X[:, 0], X[:, 1], c=y, s=50, cmap='autumn')
plot_svc_decision_function(clf)
plt.scatter(clf.support_vectors_[:, 0], clf.support_vectors_[:, 1])
plt.show()
