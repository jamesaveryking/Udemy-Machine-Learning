#Data preprocessing part 1 section 2
dataset<-read.csv('Data.csv')


#taking care of missing data
dataset$Age = ifelse(is.na(dataset$Age),#condition checked
                    ave(dataset$Age, FUN = function(x){
                      mean(x,na.rm=TRUE)
                    }),#returned if true
                    dataset$Age) #returned if false -- returns itself)
dataset$Salary = ifelse(is.na(dataset$Salary),#condition checked
                     ave(dataset$Salary, FUN = function(x){
                       mean(x,na.rm=TRUE)
                     }),#returned if true
                     dataset$Salary) #returned if false -- returns itself)

#change categorical variables to numerical value
#factor transforms categorical variable to numeric factors
dataset$Country = factor(dataset$Country,
                         levels = c('France','Spain','Germany'),
                         labels = c(1,2,3))
dataset$Purchase = factor(dataset$Purchased,
                         levels = c('No','Yes'),
                         labels = c(0,1))

x<-dataset[,1:3]
y<-dataset[,4]