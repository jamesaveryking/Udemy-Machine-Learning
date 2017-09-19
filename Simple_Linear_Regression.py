# -*- coding: utf-8 -*-
"""
Created on Fri Sep  1 16:08:51 2017

@author: 0
"""
import numpy as np #contains math tools needed for any mathematics in code
import matplotlib.pyplot as plt #used for plotting
import pandas as pd #used for importing and managing datasets

#importing dataset
dataset = pd.read_csv('salary.csv')
X=dataset.iloc[:,:-1].values
y=dataset.iloc[:,1].values
#ordinary least squares method -- finds minimum of sums of variance
from sklearn.cross_validation import training_test_split
X_train, X_test, y_train, y_test = train_test_split(X,y,test_size = 1/3, random_state = 0)

from sklearn.linear_model import LinearRegression
regressor = LinearRegression()
regressor.fit(X_train,y_train) #fits regression object to training classes

#predicting the test set results
y_pred = regressor.predict(X_test)

#plotting observation points and simple linear regression line
plt.scatter(X_train,y_train, color = 'red')
plt.plot(X_train,regressor.predict(X_train), color = 'blue')
plt.title('Salary vs Experience (Training Set)')
plt.xlabel('Years of Experience')
plt.ylabel('Salary')
plt.show()