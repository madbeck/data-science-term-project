import sqlite3
import csv
import json

'''
Reads data from LA_Ranking_2019-04-04_21-54-40.csv file, which contains unemployment, median household income, obesity, and diabetes data for each recorded zip code in LA County. Data is from simplyanalytics.com
'''

zip_code_to_info = {}

with open('./data/combined_data_by_zip_code/LA_Ranking_2019-04-04_21-54-40.csv') as csvfile:
	readCSV = csv.reader(csvfile, delimiter=',')
	# extract column headers
	columns = next(readCSV)

	for row in readCSV:
		zip_code = row[1]
		unemployment, median_income, obesity, diabetes = row[2], row[3], row[4], row[5]
		zip_code_to_info[zip_code] = (unemployment, median_income, obesity, diabetes)


###############################################################################
# Create connection to database
conn = sqlite3.connect('combined_data.db')
c = conn.cursor()

# Delete tables if they exist
c.execute('DROP TABLE IF EXISTS "zip_codes";')

# Create tables in the database and add data to it. REMEMBER TO COMMIT
c.execute('CREATE TABLE zip_codes(zip_code text primary key, unemployed number, income number, obesity number, diabetes number);')

for item in zip_code_to_info:
	c.execute('INSERT INTO zip_codes VALUES (?, ?, ?, ?, ?)', (item, zip_code_to_info[item][0], zip_code_to_info[item][1], zip_code_to_info[item][2], zip_code_to_info[item][3]))

conn.commit()
