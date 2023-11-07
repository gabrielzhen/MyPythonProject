import pygal_maps_world.maps
wm = pygal_maps_world.maps.World()
wm.title='America'
wm.add('North America',['ca','mx','us'])
wm.add('center america',['bz', 'cr', 'gt', 'hn', 'ni', 'pa', 'sv'])
wm.render_to_file('america.svg')