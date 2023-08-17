import pandas as pd
import matplotlib.pyplot as plt
data = pd.read_csv('happyscore_income.csv')
print('data keys :', data.keys())
GDP = data.GDP
print('Gross domestic product :\n', GDP)
print('#'*50)
avg_satisfaction = data.avg_satisfaction
print('satisfaction :\n', avg_satisfaction)
print('#'*50)
avg_income = data.avg_income
print('average income :\n', avg_income)
print('#'*50)
happy_score = data.happyScore
print('happy score :\n', happy_score)
print('#'*50)

print('initial data : \n', data)
print('#'*50)
# data.sort_values('avg_satisfaction', inplace=True)
data.sort_values('GDP', inplace=True)
print('sorted data by GDP : \n', data)

# Filter GDP
production = data[data.GDP > 1.0]
print('GDP > 1.0 : \n', production)

# plotting
plt.scatter(production.GDP, production.happyScore)
plt.xlabel('GDP')
plt.ylabel('happy Score')
plt.title('GDP Vs happy score')

#
# [plt.text(x=row['GDP'], y=row['happyScore'], s=row['country']) for k, row in production.iterrows()]

plt.text(production.iloc[0]['GDP'], production.iloc[0]['happyScore'],
         production.iloc[0]['country'])
plt.text(production.iloc[-1]['GDP'], production.iloc[-1]['happyScore'],
         production.iloc[-1]['country'])
plt.show()




