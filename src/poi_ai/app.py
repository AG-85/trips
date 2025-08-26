import pandas as pd
import pickle
import os

pd.set_option("display.max_colwidth", None)
pd.set_option("display.max_rows", None)

PICKLE = "/Users/ambikha/PycharmProjects/trips/data/points.pkl"
if os.path.isfile(PICKLE):
    with open(PICKLE, 'rb') as f:
        points = pickle.load(f)
else:
    points = pd.read_csv("/Users/ambikha/PycharmProjects/trips/data/poi.csv")
    with open(PICKLE,"wb") as f:
        pickle.dump(points, f)

#points["links"] = points["links"].str.split("; ")
points["categories"] = points["categories"].str.split("; ")
points_categories = points[["name", "categories"]]
exploded_categories = points_categories.explode("categories")

"""with open("/Users/ambikha/PycharmProjects/trips/data/exploded_categories.pkl", "rb") as f:
    check_read = pickle.load(f)
    if check_read.equals(exploded_categories):
        print("Success!")
    else:
        print("Failure!")"""

def search_nearby_pois(poi_location):
    result = exploded_categories[exploded_categories["name"].str.contains(poi_location)]
    #result = points[points["name"].str.contains(poi_location)]
    return result
    #print(result)
#search_nearby_pois("AREA 51")