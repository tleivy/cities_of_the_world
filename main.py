from collections import namedtuple

# creating namedtuple type - cities
City = namedtuple('City', 'city country population')
cities = []

# reading cities and creating objects
with open('cities_of_the_world.csv', 'r', encoding='utf-8') as f:
    raw_line = f.readline() # skipping header line
    raw_line = f.readline() # loading first line
    while raw_line != "":
        line = raw_line.replace("\"", "").split(",")
        try:
            city = City(city=line[0], country=line[4], population=line[9])
            cities.append(city)
        except IndexError:
            print("INDEX ERROR")
        raw_line = f.readline()

    for i in range(0, 5):
        print(cities[i])



