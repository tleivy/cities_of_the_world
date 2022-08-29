import pandas as pd
import numpy as np

data = pd.read_csv('cities_of_the_world.csv')
print(data)
data = data.sort_values('population', ascending=False)[0:10]
for rec in data:
    print("{}, {} - population = {}".format(data.country, data.city, data.population))
