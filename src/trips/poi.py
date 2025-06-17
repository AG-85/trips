import pandas as pd
pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)
points = pd.read_csv('/Users/ambikha/PycharmProjects/trips/data/poi.csv')
print(points.head())
