#data preprocessing
#importing the libraries

#import 3 essential libraries
import numpy as np #contains math tools needed for any mathematics in code
import matplotlib.pyplot as plt #used for plotting
import pandas as pd #used for importing and managing datasets

#importing dataset
dataset = pd.read_csv('../Data-Preprocessing/Data.csv')

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
y[:,0]=labelencoder_y.fit_transform(y[:,0]) #changes dependent values to encoded
#creates two binary columns indicating incidence

#data should be split into two sets -- training set and test set
#machine learning understands correlations through training and testing
#cross-validation library is used
from sklearn.cross_validation import train_test_split
x_train, x_test, y_train, y_test = train_test_split(x,y,test_size = 0.25, random_state=0) #.2-.3 is good size for testing set size

#feature scaling -- machine learning uses Euclidean distances to be able to see distances and changes
#this Euclidean distance sqrt((x2-x1)**2-(y2-y1)**2) can be dominated by large variables
#scaling solves this problem
from sklearn.preprocessing import StandardScaler
sc_x = StandardScaler()
x_train - sc_x.fit_transform(x_train)
x_test - sc_x.transform(x_test) #fit can be removed because it is already fitted
#do dummy variables need to be scaled? -- depends on context
#not scaling does not break model but scaling dummy variables yields greater accuracy
#do dependent categorical variables need to be scaled? -- depends on context but in this no, this is a classification problem but yes in cases of regression with many y variables
