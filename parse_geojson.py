import json

output = list()

with open('./data/geojson/acs2017_5yr_B19013_14000US06037262100.geojson') as json_file:  
    data = json.load(json_file)
    iters = 0
    for p in data['features']:
        properties = p['properties']
        geoid = properties['geoid']
        coords = properties['geometry']['coordinates']
        for i in coords:
            print(i)

        # print('Geoid: ' + geoid)
        iters += 1
    
    print(iters)



