import matplotlib.pyplot as plt
import numpy as np
from sklearn import datasets, linear_model
from sklearn.metrics import  mean_squared_error


diabetes = datasets.load_diabetes()

# ['data', 'target', 'DESCR', 'feature_names', 'data_filename', 'target_filename']
# print(diabetes.keys()) 

# [[ 0.03807591  0.05068012  0.06169621 ... -0.00259226  0.01990842 -0.01764613]]
# print(diabetes.data)  

# print(diabetes.DESCR)
# print(diabetes.target)

# selecting one feature
# diabetes_X = diabetes.data[:, np.newaxis, 2]

# selecting all feature
diabetes_X = diabetes.data


# print(diabetes_X)

diabetes_X_train = diabetes_X[:-30]
diabetes_X_test  = diabetes_X[-30:] 

diabetes_y_train = diabetes.target[:-30]
diabetes_y_test  = diabetes.target[-30:]

model = linear_model.LinearRegression()

model.fit(diabetes_X_train, diabetes_y_train)

diabetes_y_predicted = model.predict(diabetes_X_test)

print("MEAN SQUARED ERROR IS: ", mean_squared_error(diabetes_y_test, diabetes_y_predicted))

print("WEIGHTS: ", model.coef_)
print("INTERCEPT: ", model.intercept_)

# plt.scatter(diabetes_X_test, diabetes_y_test)
# plt.plot(diabetes_X_test, diabetes_y_predicted)

# plt.show()