import pandas as pd

#Creating a pandas series which is a list of grades
grades = pd.Series([72, 95, 84, 67])
print(f'Here are a series of grades.')
print(grades)

#Accessing the first grade in the series
grades[0]
print(f'The first grade listed is {grades[0]}')

#Counting the number of grades
grades.count()
print(f'There are {grades.count()} grades listed')

#Find the average of the grades
grades.mean()
print(f'The mean grade is {grades.mean()}') 

#Finding the minimum grade
grades.min()
print(f'The minumum grade is {grades.min()}')

#Finding the max grade
grades.max()
print(f'The highest grade is {grades.max()}')

#Finding the standard deviation of the grades
grades.std()
print(f'The standard deviation of the grades is {grades.std()}')

#Finding stats including the quartiles using the describe call
grades.describe()
print(f'A summary of the statistics of the grades is listed below')
print(grades.describe())

#Initializing the series of grades with a dictionary
grades = pd.Series({'Wally': 87, 'Eva': 100, 'Sam': 94})
print('Here is a dictionary of grades')
print(grades)

grades['Eva']
print('Here is the score for Eva')
print(grades['Eva'])

print('Here is the score for Wally.')
print(grades.Wally)

#Using the values attribute to return the underlying array
grades.values
print('Here are the values of the grades of the students in class.')
print(grades.values)

print('Chris Kollbaum')
