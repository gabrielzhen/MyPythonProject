import json
import pygal_maps_world.maps
from country_codes import get_country_code
filename='population_data.json'
with open(filename) as f:
    pop_data=json.load(f)
cc_populations={}
for pop_dict in pop_data:
    if pop_dict['Year']=='2010':
        countr_name=pop_dict['Country Name']
        population=int(float(pop_dict['Value']))
        code=get_country_code(countr_name)
        if code:
            cc_populations[code]=population

wm = pygal_maps_world.maps.World()
wm.title='America'
wm.add('2010',cc_populations)
wm.render_to_file('america.svg')