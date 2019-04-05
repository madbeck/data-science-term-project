import sqlite3
import csv
import json

'''
Reads data from LA_Ranking_2019-04-04_21-54-40.csv file, which contains unemployment, median household income, obesity, and diabetes data for each recorded zip code in LA County. Data is from simplyanalytics.com
'''

zipcode_info = {}

with open('./food_proximity_data.txt') as json_file:  
	zipcode_info = json.load(json_file)

###############################################################################
# Create connection to database
conn = sqlite3.connect('food_access.db')
c = conn.cursor()

# Delete tables if they exist
c.execute('DROP TABLE IF EXISTS "zip_code_to_food";')

# Create tables in the database and add data to it. REMEMBER TO COMMIT
c.execute('CREATE TABLE zip_code_to_food(zip_code text primary key, 1km_sm number, 3km_sm number, 1km_ff number, 3km_ff number);')

for zipcode in zipcode_info:
	c.execute('INSERT INTO zip_code_to_food VALUES (?, ?, ?, ?, ?)', (item, zip_code_to_info[item][0], zip_code_to_info[item][1], zip_code_to_info[item][2], zip_code_to_info[item][3]))

conn.commit()