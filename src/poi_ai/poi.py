import pandas as pd
import matplotlib.pyplot as plt
pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)
points = pd.read_csv('/Users/ambikha/PycharmProjects/trips/data/poi.csv')
print(points.head())

print(points.columns)
poi = points[["name", "latitude_radian", "longitude_radian", "links", "categories"]].copy()
print(poi.head(10))
poi.plot.scatter(y = "latitude_radian", x = "longitude_radian")
plt.savefig("graph.png")