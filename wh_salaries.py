"""
Drake Watson
Trimble Data Science Assessment
Problem 2
"""

import pandas as pd

salary_df = pd.read_csv('data/white_house_salaries.csv')

# Number of observations in the data set
print("Total Number of Employees", len(salary_df))

# Find how many unique status there are
print("Unique Status Titles:", salary_df.STATUS.unique())

# Find proportion of status titles
print("Proportion of Employee Status:",
      salary_df['STATUS'].value_counts(normalize=True) * 100)

# Find amount of unique position titles
print("Number of Unique Position Titles:",
      len(salary_df['POSITION TITLE'].unique()))

# Convert salary values to int
salary_df['SALARY'] = salary_df['SALARY'].str[:-2]
salary_df['SALARY'] = salary_df['SALARY'].str.replace('\W', '')
salary_df['SALARY'] = salary_df['SALARY'].astype(int)

# Find range of salaries
print("Minimum Salary (> 0):",
      salary_df[salary_df['SALARY'] > 0]['SALARY'].min())
print("Maximum Salary:", salary_df['SALARY'].max())
