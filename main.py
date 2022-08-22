from collections import namedtuple

# creating namedtuple type - cities
City = namedtuple('City', 'name country population')
cities = []

with open('cities_of_the_world.csv', 'r', encoding='utf-8') as f:
    # reading cities and creating objects
    raw_line = f.readline()  # skipping header line
    raw_line = f.readline()  # loading first line
    while raw_line != "":
        line = raw_line.replace('","', "|").replace('"', "").split("|")  # cleaning the raw input
        pop_temp = line[9]
        if pop_temp == "":
            pop_temp = 0
        pop_temp = int(float(pop_temp))  # parsing population to int

        curr = City(name=line[0], country=line[4], population=pop_temp)
        cities.append(curr)
        raw_line = f.readline()

    # getting 10 most populated cities
    population_sorted = sorted(cities, key=lambda city: city[2], reverse=True)
    ten_biggest_cities = population_sorted[0:10]
    for city in ten_biggest_cities:
        print("{}, population: {}".format(city.name, city.population))

         





