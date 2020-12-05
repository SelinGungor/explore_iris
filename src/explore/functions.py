from sklearn import datasets, tree, metrics
import numpy as np


def load_dataset():
	return datasets.load_iris(), datasets.load_digits()


def train_and_test():
	iris, digits = load_dataset()

	iris_data = iris.data
	iris_target = iris.target
	
	print(len(iris_data))
	print(type(iris_data))

	# Split the dataset randomly
	iris_test_ids = np.random.permutation(len(iris_data))
	
	# Leave the last 20 entries for testing
	iris_train_set_first = iris_data[iris_test_ids[:-20]]
	iris_test_set_first = iris_data[iris_test_ids[-20:]]
	
	iris_train_set_second = iris_target[iris_test_ids[:-20]]
	iris_test_set_second = iris_target[iris_test_ids[-20:]]
	
	iris_classifier = tree.DecisionTreeClassifier()
	iris_classifier.fit(iris_train_set_first, iris_train_set_second)
	
	predicted_flowers = iris_classifier.predict(iris_test_set_first)
	
	accuracy_score = metrics.accuracy_score(predicted_flowers, iris_test_set_second)*100

	
	print("Predicted flower species")
	print(predicted_flowers)
	print("Actual flower species")
	print (iris_test_set_second)
	print("Accuaracy score: " + str(accuracy_score))
	