

#Author: Carolina Serrano
#Version: 1.0.0
#Libraries:
#Pandas: http://pandas.pydata.org/
#NumPy: http://www.numpy.org/

#Linear Regression Implementation
"""Problem Set Nº 1: The company doesn't have a strict set of rules on determining the salaries
of its employees, so as a researcher, is your job to find the correlation between salary and years of experience 
in a given dataset and predict what would be the most compatible salary with each time of experience."""


# Importing the libraries
import numpy as np
import pandas as pd

# Importing the dataset
dataset = pd.read_csv('Salary_Data.csv')
X = dataset.iloc[:, :-1].values#Column with independent variables, years os experience
y = dataset.iloc[:, 1].values #Column with dependent variables, salaries


# Training Set and Testing Set -> Spliting the dataset
"""We have 30 observations in the Salary sample, but we only need 1/3 in the test set, which are 10 elements.
Our training model will have 20 elements in order to make it learn from the data.
random_state = 0 ensures that the data is split in exactly the same manner each time we run the code."""
from sklearn.model_selection import train_test_split
Y_train, y_test, x_train, x_test = train_test_split(X, y, test_size = 1/3, random_state = 0)


#Importing the linear regression class from scikit-learn
from sklearn.linear_model import LinearRegression


#Creating the Regressor object
"""The fit() method will be responsible to correlate the salary and the years os experience.
It automatically does the training."""
regressor = LinearRegression()
regressor.fit(Y_train, x_train)

#Predicing the test from the observations
"""Predict target values of the salary values"""
salaryPredictor = regressor.predict(y_test)

training_sample_yrs_experience = X[:10]
training_sample_salary = y[:10]

print("\n==== ACTUAL SALARIES (YEARLY) ====")
print("Yrs of exp         Salary")


for yrs_experience, salary in zip(training_sample_yrs_experience, training_sample_salary):
	print(str(yrs_experience) + '............' + str(salary))

print("\n")

print("\n==== SALARY PREDICTION (YEARLY) ====")
print("Yrs of exp         Salary prediction")
for yrs_experience, prediction in zip(training_sample_yrs_experience, salaryPredictor):
	print(str(yrs_experience) + '............' + str(round(prediction,2)))

	



