import requests
import urllib
import json
import numpy as np
import time

key = "AIzaSyBeyECnXDJ-oLMp5WMySXDiBTmHNYNCfzU"
base_URL = "https://maps.googleapis.com/maps/api/place/nearbysearch/json?"

data = {}
price_levels = {}
wealthy_zips = ['90049', '91381', '90275', '90290', '91436', '90266', '91302', '90265', '90210', '90402', '91108', '90272', '90274', '91011', '90077']
poor_zips = ['90021', '90058', '90013', '90014', '90017', '90007', '90071', '90057', '90015', '90033', '90037', '90006', '90011', '90012', '90073']

with open('./lat_lon_by_zip_code.txt') as json_file:  
	zipcode_info = json.load(json_file)
	for zipcode in poor_zips:
		prices = []
		print(zipcode)
		lat_long = zipcode_info[zipcode]

		commands = [
			{'category': "3km_sm", 'radius':"3000", 'type':"supermarket", 'keyword':""}
		]

		food_access_data = {}
		for command in commands:
			parameters = {
				'location': lat_long,
				'radius': command['radius'],
				'type': command['type'],
				'keyword': command['keyword'],
				'key': key
			}
			url = base_URL + urllib.parse.urlencode(parameters)
			url = urllib.parse.unquote(url)
			response = requests.get(url).json()
			
			places = []
			results = response['results']
			count = len(results)

			while 'next_page_token' in response.keys():
				time.sleep(2)
				parameters = {
				'key': key,
				'pagetoken': response['next_page_token']
				}
				url = base_URL + urllib.parse.urlencode(parameters)
				url = urllib.parse.unquote(url)
				response = requests.get(url).json()
				more_results = response['results']
				count += len(more_results)
				results.append(more_results)

			print("------------")
			for i in range(len(results)):
				result_entry = results[i]
				result_keys = list(result_entry)
				if('price_level' in result_keys):
					priceLevel = result_entry['price_level']
					print(priceLevel)
					prices.append(priceLevel)
			price_levels[zipcode] = prices

			food_access_data[command['category']] = count
		
		print(food_access_data)
		data[zipcode] = food_access_data

print(price_levels)
