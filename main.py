from collections import namedtuple


def format_line_split(raw_line):
    """
    :param raw_line:
    :return: a list of the words in the line
    """
    return raw_line.replace('","', "|").replace('"', "").split("|")


def sub_list(lst, start_index, finish_index):
    """
    :param lst: origin list
    :param start_index: starting index
    :param finish_index: finish index
    :return: a sub list of the origin list
    """
    return lst[start_index:finish_index]


def population_parse2int(pop_temp):
    """
    :param pop_temp: a string representing the population of a city
    :return: population parsed to int
    """
    if pop_temp == "":
        pop_temp = -1
    return int(float(pop_temp))


# creating namedtuple type - City, Country
City = namedtuple('City', 'name country population')
Country = namedtuple('Country', 'name population city_counter')
cities = []
country_data_lst = []


with open('cities_of_the_world.csv', 'r', encoding='utf-8') as f:

    # reading cities and creating objects
    raw_line = f.readline()  # skipping header line
    raw_line = f.readline()  # loading first line
    while raw_line != "":

        line = format_line_split(raw_line)  # cleaning the raw input
        pop_int = population_parse2int(line[9])
        curr = City(name=line[0], country=line[4], population=pop_int)
        cities.append(curr)

        raw_line = f.readline()  # reading the next line of data

    # getting 10 most populated cities
    population_sorted = sorted(cities, key=lambda city: city[2], reverse=True)
    ten_biggest_cities = sub_list(population_sorted, 0, 10)
    print("ten most populated cities")
    print("-------------------------")
    for city in ten_biggest_cities:
        print("{}, population: {}".format(city.name, city.population))
    print("\n")
    print("\n")
    
    countries_sorted = sorted(cities, key=lambda city: city[1])  # list of cities grouped by countries, alphabetical
    curr_country = countries_sorted[0].country

    city_count = 0
    pop_sum = 0
    
    for city in countries_sorted:
        if city.country == curr_country:  # if it's still the same country
            city_count += 1
            pop_sum += city.population
        else:
            curr = Country(name=curr_country, population=pop_sum, city_counter=city_count)  # create a country tuple
            country_data_lst.append(curr)
            curr_country = city.country  # update current country and initialize
            city_count = 1
            pop_sum = city.population

    print("countries and number of cities")
    print("------------------------------")
    for country in country_data_lst:
        print("{}, num of cities: {}".format(country.name, country.city_counter))    
    print("\n")
    print("\n")

    # finding the ten bottom populated countries
    pop_sorted_countries = sorted(country_data_lst, key=lambda country: country[1])
    ten_bottom_pop = []
    counter = 0
    for country in pop_sorted_countries:
        if country.population > 0:
            counter += 1
            ten_bottom_pop.append(country)
        if counter == 10:
            break    
    
    print("ten less populated countries")
    print("----------------------------")
    for country in ten_bottom_pop:
        print("{}, population: {}".format(country.name, country.population))
