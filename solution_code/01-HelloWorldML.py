from sklearn.datasets import load_iris
iris = load_iris()

keys = iris.keys()
print(keys)

"""
import Image
image = Image.open('Iris_Images/iris-setosa.jpg')
image.show()
image = Image.open('Iris_Images/iris-versicolor.jpg')
image.show()
image = Image.open('Iris_Images/iris-virginica.jpg')
image.show()
"""

import numpy as np
import matplotlib.pyplot as plt

feat1_idx = 0
feat2_idx = 1

plt.scatter(iris.data[:, feat1_idx], iris.data[:, feat2_idx],
			c=iris.target, cmap=plt.cm.get_cmap('winter', 3))
def fmt(i, *args):
	return iris.target_names[int(i)]
plt.colorbar(ticks=[0, 1, 2], format=plt.FuncFormatter(fmt))
plt.xlabel(iris.feature_names[feat1_idx])
plt.ylabel(iris.feature_names[feat2_idx]);
plt.show()

