# Objectives
# 1 Find out the average age of the patients in the dataset.
# 2 Analyze where a majority of the individuals are from.
# 3 Look at the different costs between smokers vs. non-smokers.
# 4 Figure out what the average age is for someone who has at least one child in this dataset.

import pandas as pd
import numpy as np

# Create my data frame
health_data = pd.read_csv('insurance.csv')

# O1
avg_age = int(health_data['age'].mean())

# O2
most_populous_region = health_data['region'].mode()

# O3
# df.loc[:,[(df[col] > 14).any() for col in df.columns]]
# a = health_data.loc[:,["smoker"]  'yes']
# a = health_data['smoker'].str.contains('yes')  # returns true if smoker = yes
# Seems related https://stackoverflow.com/questions/46307490/how-can-i-extract-the-nth-row-of-a-pandas-data-frame-as-a-pandas-data-frame/46307819
smoker_avgcost = round(health_data.loc[health_data['smoker'] == 'yes'].groupby('smoker').charges.mean(),2)
nonsmoker_avgcost = round(health_data.loc[health_data['smoker'] == 'no'].groupby('smoker').charges.mean(),2)



# O4


# Output
print('Patients average age is ' + str(avg_age) + '.')
print('Most patients are from the ' + most_populous_region)
print(f"Smokers cost (on average) ${nonsmoker_avgcost}, and Non-smokers cost (on average) ${smoker_avgcost}. It costs {nonsmoker_avgcost}-{smoker_avgcost} less to not smoke!")
