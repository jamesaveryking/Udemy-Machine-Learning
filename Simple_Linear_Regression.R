#Simple Linear Regression Section 2
dataset<-read.csv("Salary_Data.csv")

#y = a + bx, y is dependent, x is dependent

#data preprocessing
library(caTools)
set.seed(123)
split = sample.split(dataset$Salary, SplitRatio = 2/3)
training_set = subset(dataset, split = TRUE)
test_set = subset(dataset, split = FALSE)
#building the simple linear regression set with fit
regressor = lm(formula = Salary ~ YearsExperience,
               training_set)
summary(regressor)
#predicting test results
y_pred = predict(regressor, newdata = test_set)
#visualize the training and test set results
library(ggplot2)
#graph one is prediction of training set
ggplot() +
  geom_point(aes(x = training_set$YearsExperience,y = training_set$Salary),
                 col = "red") +
  geom_line(aes(x = training_set$YearsExperience,y = predict(regressor, newdata = training_set)),
            col = "blue") +
  ggtitle("Salary vs Experience (Training Set)") +
  xlab("Years of Experience") +
  ylab("Salary")
#graph two is prediction of test set
ggplot() +
  geom_point(aes(x = test_set$YearsExperience,y = test_set$Salary),
             col = "red") +
  geom_line(aes(x = test_set$YearsExperience,y = predict(regressor, newdata = training_set)),
            col = "blue") +
  ggtitle("Salary vs Experience (Test Set)") +
  xlab("Years of Experience") +
  ylab("Salary")