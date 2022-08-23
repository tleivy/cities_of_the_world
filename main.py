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


def update_country_in_list(country_list, city):
    """
    this function checks if the current city's country is already in the list.
    if it isn't then it creates a new country tuple and adds it to the list
    if it is, updated the population and city counter fields of the country
    :param country_list:
    :param city:
    :return:
    """
    in_list = False
    c_index = 0  # country index
    for country in country_list:
        if country[0] == city.country:
            in_list = True
            break
        c_index += 1

    if not in_list:
        country = Country(name=curr.country, population=curr.population, city_counter=1)
        country_list.append(country)
    else:
        temp_pop = country_list[c_index][1] + city[2]  # adding city population to country total
        temp_cit = country_list[c_index][2] + 1  # incrementing country's city counter
        country_list[c_index] = country_list[c_index]._replace(population=temp_pop)
        country_list[c_index] = country_list[c_index]._replace(city_counter=temp_cit)


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
        update_country_in_list(country_data_lst, curr)

        raw_line = f.readline()  # reading the next line of data

    # printing countries (alpha sorted) and number of cities
    countries_alpha_sorted = sorted(country_data_lst, key=lambda country: country[0])
    print("")
    print("countries and number of cities")
    print("------------------------------")
    for country in countries_alpha_sorted:
        print("{}, num of cities: {}".format(country.name, country.city_counter))
    print("\n")

    # getting 10 most populated cities
    population_sorted = sorted(cities, key=lambda city: city[2], reverse=True)
    ten_biggest_cities = sub_list(population_sorted, 0, 10)
    print("ten most populated cities")
    print("-------------------------")
    for city in ten_biggest_cities:
        print("{}, {} - population: {}".format(city.name, city.country, city.population))
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
    
    print("ten bottom populated countries")
    print("----------------------------")
    for country in ten_bottom_pop:
        print("{} - population: {}".format(country.name, country.population))
