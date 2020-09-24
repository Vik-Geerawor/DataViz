import json
from pygal_maps_world import i18n
import pygal
from pygal.style import RotateStyle, LightColorizedStyle


def run_world_population():
    # load the data into a list
    filename = 'files/population_data.json'
    with open(filename) as f:
        pop_data = json.load(f)

    # build a dictionary of population data
    cc_population = {}
    for pop_dict in pop_data:
        if pop_dict['Year'] == '2010':
            country_name = pop_dict['Country Name']
            population = int(float(pop_dict['Value']))
            code = get_country_code(country_name)
            if code:
                cc_population[code] = population

    # group countries into 3 population levels:
    cc_pops_1, cc_pops_2, cc_pops_3 = {}, {}, {}
    for cc, pop in cc_population.items():
        if pop < 10000000:
            cc_pops_1[cc] = pop
        elif pop < 1000000000:
            cc_pops_2[cc] = pop
        else:
            cc_pops_3[cc] = pop

    print(len(cc_pops_1), len(cc_pops_2), len(cc_pops_3))

    wm_style = RotateStyle('#336699', base_style=LightColorizedStyle)
    wm = pygal.maps.world.World(style=wm_style)
    wm.title = 'World Population in 2010, by Country'
    wm.add('0-10m', cc_pops_1)
    wm.add('10m-1bn', cc_pops_2)
    wm.add('>1bn', cc_pops_3)

    wm.render_to_file('world_population.svg')


def get_country_code(country_name):
    """Returns the Pygal 2-digit country code for the given country"""
    for code, name in sorted(i18n.COUNTRIES.items()):
        if name == country_name:
            return code


def americas():
    wm = pygal.maps.world.World()
    wm.titie = 'NCSA'

    wm.add('NA', ['ca', 'mx', 'us'])
    wm.add('CA', ['bz', 'cr', 'gt', 'hm', 'ni'])

    wm.render_to_file('americas.svg')
