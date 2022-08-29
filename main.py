from collections import namedtuple


def format_line_split(raw_line):
    """
    this function tokenizes the raw input line
    :param raw_line: an un-formatted file line
    :return: a list of the words in the line
    """
    return raw_line.replace('","', "|").replace('"', "").split("|")


def sub_list(lst, start_index, finish_index):
    """
    this function creates a sublist of a given list
    :param lst: origin list
    :param start_index: starting index
    :param finish_index: finish index
    :return: a sub list of the origin list
    """
    return lst[start_index:finish_index]


def population_parse2int(pop_temp):
    """
    this function parses a string representing the population to an integer
    :param pop_temp: a string representing the population of a city
    :return: population parsed to int
    """
    if pop_temp == "":
        pop_temp = -1
    return int(float(pop_temp))


def new_city(formatted_line):
    """
    this function creates a namedtuple object representing a city
    the properties are: name, country and population
    :param formatted_line: a tokenized input line
    :return: a namedtuple representing a city
    """

    pop_int = population_parse2int(formatted_line[9])
    return City(name=formatted_line[0], country=formatted_line[4], population=pop_int)


def new_country(city_tuple):
    """
    this function creates a namedtuple object representing a city
    the object's properties are: name, population and city_counter
    :param city_tuple: a namedtuple representing a city
    :return: a namedtuple representing a country
    """
    return Country(name=city_tuple.country, population=city_tuple.population, city_counter=1)


def increment_country_properties(country_dict, source_city, key):
    """
    this function updates a country namedtuple properties:
    it adds the source city's population to the country's population
    it adds 1 to the country's city counter
    then creates a new country tuple and updates the dictionary
    :param country_dict: a dictionary of all countries and their data
    :param source_city:
    :param key: the country's name
    :return:
    """
    temp_pop = country_dict[key][1] + source_city[2]  # adding city population to country total
    city_count = country_dict[key][2] + 1  # incrementing country's city counter

    new_tuple = Country(name=key, population=temp_pop, city_counter=city_count)
    country_dict[key] = new_tuple


def update_country_dict(country_dict, city):
    """
    this function checks if the country is in the country data dictionary
    if it isn't it creates a new country tuple and adds it to the dictionary
    if it is it updates the matching country data
    :param country_dict: a dictionary containing country data tuples
    :param city: a tuple containing city data
    :return:
    """
    key = city.country
    if key not in country_dict.keys():
        country_tuple = new_country(city)
        country_dict[key] = country_tuple
    else:
        increment_country_properties(country_dict, city, key)


def read_file(file_name, city_list, country_dict):
    """
    this function reads a given file and creates a list of the cities a countries
    :param file_name:
    :param city_list:
    :param country_dict:
    :return:
    """
    with open(file_name, 'r', encoding='utf-8') as f:
        # reading cities and creating objects
        raw_line = f.readline()  # skipping header line
        raw_line = f.readline()  # loading first line
        while raw_line != "":
            line = format_line_split(raw_line)  # cleaning the raw input
            curr = new_city(line)
            city_list.append(curr)
            update_country_dict(country_dict, curr)

            raw_line = f.readline()  # reading the next line of data


def print_country_cities_num():
    """
    this function prints countries (alpha sorted) and number of cities
    :return:
    """
    countries_alpha_sorted = sorted(country_data.items(), key=lambda country: country[0])
    print("")
    print("countries and number of cities")
    print("------------------------------")
    for country in countries_alpha_sorted:
        print("{}, num of cities: {}".format(country[1][0], country[1][2]))
    print("\n")


def ten_most_populated_cities():
    """
    this function prints the 10 most populated cities
    :return:
    """
    population_sorted = sorted(cities, key=lambda city: city[2], reverse=True)
    ten_biggest_cities = sub_list(population_sorted, 0, 10)
    print("ten most populated cities")
    print("-------------------------")
    for city in ten_biggest_cities:
        print("{}, {} - population: {}".format(city.name, city.country, city.population))
    print("\n")


def ten_bottom_populated_countries():
    """
    this function finds and prints the 10 bottom populated countries
    :return:
    """
    pop_sorted_countries = sorted(country_data.items(), key=lambda country: country[1][1])
    ten_bottom_pop = []
    counter = 0
    for country in pop_sorted_countries:
        if country[1][1] > 0:
            counter += 1
            ten_bottom_pop.append(country)
        if counter == 10:
            break
    print("ten bottom populated countries")
    print("----------------------------")
    for country in ten_bottom_pop:
        print("{} - population: {}".format(country[1][0], country[1][1]))


# creating namedtuple type - City, Country
City = namedtuple('City', 'name country population')
Country = namedtuple('Country', 'name population city_counter')
cities = []  # a list of city tuples
country_data = {}  # a dictionary of country tuples

if __name__ == '__main__':
    read_file('cities_of_the_world.csv', cities, country_data)
    print_country_cities_num()
    ten_most_populated_cities()
    ten_bottom_populated_countries()
