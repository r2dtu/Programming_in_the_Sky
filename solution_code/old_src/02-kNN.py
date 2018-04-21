# Supervised Learning - Classification (k-NN)

# Classification - KNN
from sklearn.datasets import load_iris
from sklearn.neighbors import KNeighborsClassifier
import matplotlib.pyplot as plt
import plotfuncs as pf

iris = load_iris()
data, labels = iris.data, iris.target

kNN = KNeighborsClassifier(n_neighbors=3)
kNN.fit(data, labels)

# Predict a 2cm x 2cm sepal and 5cm x 3cm petal.
result = kNN.predict([[2, 2, 5, 3],])
#knn.predict_proba([[2, 2, 5, 3],])
print(iris.target_names[result])

# 2D plot
feat1_idx = 0
feat2_idx = 1
data = data[:, (feat1_idx, feat2_idx)]
kNN.fit(data, labels)

xx, yy = pf.make_meshgrid(data[:, 0], data[:, 1], 100)
# plt.cm.coolwarm
pf.plot_contours(plt, kNN, xx, yy, cmap=plt.cm.get_cmap('winter', 3))
plt.scatter(data[:, 0], data[:, 1], c=labels, cmap=plt.cm.get_cmap('winter', 3), edgecolor='k')
plt.show()

