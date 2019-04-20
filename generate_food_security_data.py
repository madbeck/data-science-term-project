import requests
import urllib
import json
import numpy as np

key = "AIzaSyBeyECnXDJ-oLMp5WMySXDiBTmHNYNCfzU"
base_URL = "https://maps.googleapis.com/maps/api/place/nearbysearch/json?"

#zipcode : {'groceries1km':#, 'groceries5km':#, ff1km ff5km}
data = {}

with open('./lat_lon_by_zip_code.txt') as json_file:  
	zipcode_info = json.load(json_file)
	for zipcode in zipcode_info:
		lat_long = zipcode_info[zipcode]
		# print(lat_long)

		commands = [{'category': "1km_sm", 'radius':"1000", 'type':"supermarket", 'keyword':""},
		{'category': "3km_sm", 'radius':"3000", 'type':"supermarket", 'keyword':""},
		{'category': "1km_ff", 'radius':"1000", 'type':"", 'keyword':"Fast Food"},
		{'category': "3km_ff", 'radius':"3000", 'type':"", 'keyword':"Fast Food"},]

		food_access_data = {}
		for command in commands:
			parameters = {
				'location': lat_long, #"41.827389, -71.399323",  #get latlong
				'radius': command['radius'],
				'type': command['type'],
				'keyword': command['keyword'],
				'key': key
			}
			url = base_URL + urllib.parse.urlencode(parameters)
			url = urllib.parse.unquote(url)

			response = requests.get(url).json()
			results = response['results']
			for i in range(len(results)):
				result_entry = results[i]
				result_keys = list(result_entry)
				if('price_level' in result_keys):
					priceLevel = result_entry['price_level']
					print(priceLevel)
			food_access_data[command['category']] = len(results)
		# print(food_access_data)
		data[zipcode] = food_access_data

#print(data)

with open('food_proximity_data.txt', 'w') as outfile:
	json.dump(data, outfile)


# parameters = {
# 	'location': "41.827389, -71.399323", #lag_long, #get latlong
# 	'radius': "1000",
# 	'type': "",
# 	# 'pagetoken': 1,
# 	'keyword': "Fast Food",
# 	'key': key
# }

# url = base_URL + urllib.parse.urlencode(parameters)
# url = urllib.parse.unquote(url)
# print(url)

# response = requests.get(url).json()
# restaurants = response['results']
# print(len(restaurants))
# for restaurant in restaurants:
# 	print(restaurant['name'])
