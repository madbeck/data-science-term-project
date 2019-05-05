import requests
import urllib
import json
import numpy as np
import time

key = "AIzaSyBeyECnXDJ-oLMp5WMySXDiBTmHNYNCfzU"
base_URL = "https://maps.googleapis.com/maps/api/place/nearbysearch/json?"
data = {}

with open('./lat_lon_by_zip_code.txt') as json_file:  
	zipcode_info = json.load(json_file)
	for zipcode in zipcode_info:
		print(zipcode)
		lat_long = zipcode_info[zipcode]

		commands = [{'category': "1km_sm", 'radius':"1000", 'type':"supermarket", 'keyword':""},
		{'category': "3km_sm", 'radius':"3000", 'type':"supermarket", 'keyword':""},
		{'category': "1km_ff", 'radius':"1000", 'type':"", 'keyword':"Fast Food"},
		{'category': "3km_ff", 'radius':"3000", 'type':"", 'keyword':"Fast Food"},]

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
				results = response['results']
				count += len(results)

			food_access_data[command['category']] = count
		print(food_access_data)
		data[zipcode] = food_access_data

with open('food_proximity_data.txt', 'w') as outfile:
	json.dump(data, outfile)
