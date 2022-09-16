import pandas as pd

#Creating a dataframe from a dictionary that represents student grades on three exams

grades_dict = {'Wally': [87, 96, 70], 'Eva': [100, 87, 90], 'Sam': [94, 77, 90], 'Katie': [100, 81, 82], 'Bob': [83, 65, 85]}
grades = pd.DataFrame(grades_dict)
print('These are the grades of 5 students on exams in class')
print(grades)

#Now we will label the rows
grades.index = ['Test1', 'Test2', 'Test3']
print('Table with rows labeled')
print(grades)

#Now we will find Eva's and Sam's grades
print('Here are the grades of Eva and Sam')
print(grades['Eva'])
print(grades.Sam)

#Locating different rows and columns
print('Now we will locate different values in the table')
print('Here are the test #1 grades')
print(grades.loc['Test1'])
print('Here are the scores for the second exam')
print(grades.iloc[1])

#Now we will find specific scores in the table
print("Eva's Test2 score")
print(grades.at['Test2', 'Eva'])
print(f'Wally has a grade of {grades.iat[2, 0]} on test3.')

#Using the describe command to get a summary of basic descriptive statistics
print('Here is a table of the statistics of our table')
print(grades.describe())
print('Whoa that is a lot of numbers after the decimal point.  We will change the precision.')
pd.set_option("display.precision",2)
print(grades.describe())

#Finding the mean for each student
print(f'The mean grades for each student is {grades.mean()}')

#Reversing the rows
print('Lets change the table so the most recent exam appears at the top')
print(grades.sort_index(ascending=False))

#Sorting data by columns
print("Let's put the columns in alphabetical order")
print(grades.sort_index(axis=1))
print('Chris Kollbaum')

