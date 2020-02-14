import pandas as pd

data = pd.read_csv('medals.csv')

# data = pd.read_excel('medals.xlsx')


# data = pd.read_csv('http://winterolympicsmedals.com/medals.csv')

print(data[(data.Medal == 'Gold') & (data.NOC == 'GER') & (data.Event == 'two-man')])
