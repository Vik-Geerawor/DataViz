import json
from pygal_maps_world import i18n


def run_world_population():
    # load the data into a list
    filename = 'files/population_data.json'
    with open(filename) as f:
        pop_data = json.load(f)

    # Print the 2010 population for each country
    for pop_dict in pop_data:
        if pop_dict['Year'] == '2010':
            country_name = pop_dict['Country Name']
            population = int(float(pop_dict['Value']))
            print(country_name + ": " + str(population))


def show_intl_countries():
    for country_code in sorted(i18n.COUNTRIES.keys()):
        print(country_code, i18n.COUNTRIES[country_code])