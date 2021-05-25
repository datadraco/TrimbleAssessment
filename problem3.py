"""
Drake Watson
Trimble Data Science Assessment
Problem 3
"""

import pandas as pd
import seaborn as sns

data = pd.read_csv('data/data.csv', names=['Trial', 'Result'])

print(data['Result'].describe())

sns.distplot(data, x='Result')
