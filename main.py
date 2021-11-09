# Objectives
# 1 Find out the average age of the patients in the dataset.
# 2 Analyze where a majority of the individuals are from.
# 3 Look at the different costs between smokers vs. non-smokers.
# 4 Figure out what the average age is for someone who has at least one child in this dataset.

import pandas as pd
import numpy as np

# O1
health_data = pd.read_csv('insurance.csv')
avg_age = int(health_data['age'].mean())
# O2
most_populous_region = health_data['region'].mode()
# O3
# df.loc[:,[(df[col] > 14).any() for col in df.columns]]
print(health_data)
print(health_data.head())

# O4



# Output
print('Patients average age is ' + str(avg_age) + '.')
print('Most patients are from the ' + most_populous_region)

