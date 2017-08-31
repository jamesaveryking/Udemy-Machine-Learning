# Udemy-Machine-Learning
Created 8/30/2017#data preprocessing
#importing the libraries

#import 3 essential libraries
import numpy as np #contains math tools needed for any mathematics in code
import matplotlib.pyplot as plt #used for plotting
import pandas as pd #used for importing and managing datasets

#importing dataset
dataset = pd.read_csv('Data.csv')

#create matrix of features in addition to the object of what is read in
#also create matrix of each independent variable (matrix of features)

x = dataset.iloc[:, :-1].values
#colon indicates every line, -1 means not the last column (dependent variable to predict)

#create dependent variable vector
y = dataset.iloc[:,3].values

#replace missing data with mean of values in columns of missing data
    #could be median or mode in strategy
#import library to do this
from sklearn.preprocessing import Imputer
imputer = Imputer(missing_values = 'NaN', strategy = 'mean', axis = 0)#mean is default for strategy
#axis 0 -- col, axis 1 -- rows
imputer.fit(x[:,1:3]) #upper bound excluded, lower bound included in python syntax
x[:,1:3] = imputer.transform(x[:,1:3]) #transform replaces missing data with mean

#change categorical variables to numerical format
from sklean.preprocessing import LabelEncoder, OneHotEncoder
labelencoder_x = LabelEncoder() #instantiates class
x[:,0]=labelencoder_x.fit_transform(x[:,0]) #encodes values to country column
#this can cause problems in machine learning if greater or less than values are used to
#compare numeric values
#change to three separate dummy variables to represent true or false
#use onehotencoder
onehotencoder = OneHotEncoder(categorical_features = [0]) #specifies column to hot encode
x = onehotencoder.fit_transform(x).toarray() #encodes x at column 0
#creates three binary columns indicating incidence
labelencoder_y = LabelEncoder() #instantiates class
y[:,0]=labelencoder_y.fit_transform(y) #changes dependent values to encoded
#creates two binary columns indicating incidence


