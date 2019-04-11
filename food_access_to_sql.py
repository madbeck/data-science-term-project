import sqlite3
import csv
import json

'''
Reads data from LA_Ranking_2019-04-04_21-54-40.csv file, which contains unemployment, median household income, obesity, and diabetes data for each recorded zip code in LA County. Data is from simplyanalytics.com
'''

zip_code_info = {}

with open('./food_proximity_data.txt') as json_file:  
	zip_code_info = json.load(json_file)

###############################################################################
# Create connection to database
conn = sqlite3.connect('combined_data.db')
c = conn.cursor()

# Delete tables if they exist
c.execute('DROP TABLE IF EXISTS "food_security";')

# Create tables in the database and add data to it. REMEMBER TO COMMIT
c.execute('CREATE TABLE food_security(zip_code text primary key, one_km_sm number, three_km_sm number, one_km_ff number, three_km_ff number);')

for item in zip_code_info:
	c.execute('INSERT INTO food_security VALUES (?, ?, ?, ?, ?)', (item, zip_code_info[item]['1km_sm'], zip_code_info[item]['3km_sm'], zip_code_info[item]['1km_ff'], zip_code_info[item]['3km_ff']))

conn.commit()