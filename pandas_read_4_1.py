import pandas as pd
import matplotlib.pyplot as plt
data = pd.read_csv('happyscore_income.csv')
print(data.keys())
print('#'*50)
# print(data)

# print happyScore feature : 03 ways
# all feature column
# print('data features', data.columns.values)
# print(data('happyScore'))
# print(data("happyScore"))
# print(data.happyScore)

# Sorting and Filtering Data Using Pandas
data.sort_values(by='avg_income', inplace=True)
print(data)
print('#'*50)
# apply filter : print out avg_income > 1500
richest = data[data.avg_income > 15000]
print(richest)
print('#'*50)
print(richest.count())
print("#"*50)
print('first richest country : \n', richest.iloc[0])
print("#"*50)
print('last richest country : \n', richest.iloc[-1])
print("#"*50)
print('pandas version : ', pd.__version__)
plt.scatter(richest['avg_income'], richest['happyScore'])
plt.xlabel('avg income')
plt.ylabel('happy score')
plt.title('avg income Vs happy Score')
# for k, row in richest.iterrows():
  #  plt.text(x=row['avg_income'], y=row['happyScore'], s=row['country'])
[plt.text(x=row['avg_income'], y=row['happyScore'], s=row['country']) for k, row in richest.iterrows()]
# plt.text(richest.iloc[0]['avg_income'], richest.iloc[0]['happyScore'],
         # richest.iloc[0]['country'])
# plt.text(richest.iloc[-1]['avg_income'], richest.iloc[-1]['happyScore'],
         # richest.iloc[-1]['country'])
# plt.text(s='Algeria', y=richest.iloc[-5]['happyScore'], x=richest.iloc[-5]['avg_income'])
plt.show()






