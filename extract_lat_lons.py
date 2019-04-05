from bs4 import BeautifulSoup
import csv
import requests
import json

# extract all zip codes
def get_zip_codes():
	URL = 'https://www.zip-codes.com/county/ca-los-angeles.asp'
	
	zip_codes = list()
	r = requests.get(URL, auth = ('user', 'pass'))
	soup = BeautifulSoup(r.text, 'html.parser')
	wrapper = soup.find('table', {'class': 'statTable'})
	outer = wrapper.find_all('td', {'class': 'label'})

	for i in outer[1:]:
		inner = i.find('a')
		zip_codes.append(inner.string[-5:])

	return zip_codes


# extract lat lons from a single zip code
def extract_lat_lon(zip_code):
	URL = 'https://www.zip-codes.com/zip-code/' + zip_code + '/zip-code-' + zip_code + '.asp'
	r = requests.get(URL, auth = ('user', 'pass'))
	soup = BeautifulSoup(r.text, 'html.parser')

	wrapper = soup.find('table', {'class': 'statTable'})
	headers = wrapper.find_all('td', {'class': 'label'})
	
	# find indices of lat, lon in table
	indices = [i for i in range(len(headers)) if headers[i].span.string in ('Latitude:', 'Longitude:')]
	info = wrapper.find_all('td', {'class': 'info'})
	lat = info[indices[0]].string
	lon = info[indices[1]].string
	return (lat, lon)


def lat_lons_from_zip_codes():
	lat_lons = {}

	with open('./data/combined_data_by_zip_code/LA_Ranking_2019-04-04_21-54-40.csv') as csvfile:
		readCSV = csv.reader(csvfile, delimiter=',')
		# extract column headers
		columns = next(readCSV)

		for row in readCSV:
			zip_code = row[1]
			lat_lon = extract_lat_lon(zip_code)
			lat_lons[zip_code] = lat_lon

	return lat_lons


#########################################################################################

# running program
lat_lons = lat_lons_from_zip_codes()
with open('lat_lons.txt', 'w') as outfile:
	json.dump(lat_lons, outfile)

