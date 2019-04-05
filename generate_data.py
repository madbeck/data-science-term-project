
import requests
import urllib

key = "AIzaSyBeyECnXDJ-oLMp5WMySXDiBTmHNYNCfzU"
base_URL = "https://maps.googleapis.com/maps/api/place/nearbysearch/json?"
parameters = {
	'location': "41.827268,-71.400564",
	'radius': "1000", #in meters
	'type': "supermarket",
	# 'keyword': "bajas",
	'key': key
}

url = base_URL + urllib.parse.urlencode(parameters)
url = urllib.parse.unquote(url)
print(url)

response = requests.get(url).json()
restaurants = response['results']
print(len(restaurants))
for restaurant in restaurants:
	print(restaurant['name'])

# url = urllib.request.Request(base_URL, headers=parameters)
# example = "https://maps.googleapis.com/maps/api/place/nearbysearch/json?location=-33.8670522,151.1957362&radius=1500&type=restaurant&keyword=cruise&key=YOUR_API_KEY"

