from sklearn.cluster import KMeans
import csv
import numpy as np
import csv
import sqlite3

def sk_learn_cluster(X, K):
	"""
	TODO: Implement Sci-Kit Learn's kmeans functionality

	:param X: 2D np array containing features of the words
	:param Y: 1D np array containing labels 
	:param K: number of clusters
	"""
	kmeans = KMeans(n_clusters=K, random_state=0).fit(X)
	return kmeans

def parse_data(): # parse health and economic data from LA
	with open('./data/combined_data_by_zip_code/LA_Ranking_2019-04-04_21-54-40.csv') as combined_data:
		csv_reader = csv.DictReader(combined_data, delimiter = ',')
		data = []
		zip_codes = []
		for row in csv_reader:
			cleaned_row = []
			zip_codes.append(row['FIPS'])
			cleaned_row.append(float(row['% Employment, Unemployed, 2018']))
			cleaned_row.append(float(row['Median Household Income, 2018'])) # maybe flip this one?
			cleaned_row.append(float(row['% Body mass index - Obese, 2018']))
			cleaned_row.append(float(row['% Diabetes, 2018']))
			data.append(np.array(cleaned_row))
		data = np.array(data)
	return data, zip_codes

def parse_food_access_data(): # parse all food access data
	conn = sqlite3.connect('combined_data.db')
	c = conn.cursor()
	sql_command = "SELECT f.zip_code, f.one_km_sm, f.three_km_sm, f.one_km_ff, f.three_km_ff from food_security as f;"
	c.execute(sql_command)
	result = c.fetchall()

	data = []
	zip_codes = []
	for r in result:
		cleaned_row = []
		cleaned_row.append(float(r[1]))
		cleaned_row.append(float(r[2]))
		cleaned_row.append(float(r[3]))
		cleaned_row.append(float(r[4]))
		zip_codes.append(r[0])
		data.append(np.array(cleaned_row))
	data = np.array(data)

	return data, zip_codes

def parse_food_access_sm(): # parse just supermarket data
	conn = sqlite3.connect('combined_data.db')
	c = conn.cursor()
	sql_command = "SELECT f.zip_code, f.three_km_sm from food_security as f;"
	c.execute(sql_command)
	result = c.fetchall()

	data = []
	zip_codes = []
	for r in result:
		cleaned_row = []
		cleaned_row.append(float(r[1]))
		cleaned_row.append(float(r[2]))
		zip_codes.append(r[0])
		data.append(np.array(cleaned_row))
	data = np.array(data)
	return data, zip_codes

def parse_food_access_ff(): # parse just fast food data
	conn = sqlite3.connect('combined_data.db')
	c = conn.cursor()
	sql_command = "SELECT f.zip_code, f.three_km_ff from food_security as f;"
	c.execute(sql_command)
	result = c.fetchall()

	data = []
	zip_codes = []
	for r in result:
		cleaned_row = []
		cleaned_row.append(float(r[1]))
		cleaned_row.append(float(r[2]))
		zip_codes.append(r[0])
		data.append(np.array(cleaned_row))
	data = np.array(data)
	return data, zip_codes

def parse_health_data(): # parse just health data
	with open('./data/combined_data_by_zip_code/LA_Ranking_2019-04-04_21-54-40.csv') as combined_data:
		csv_reader = csv.DictReader(combined_data, delimiter = ',')
		data = []
		zip_codes = []
		for row in csv_reader:
			cleaned_row = []
			zip_codes.append(row['FIPS'])
			cleaned_row.append(float(row['% Body mass index - Obese, 2018']))
			cleaned_row.append(float(row['% Diabetes, 2018']))
			data.append(np.array(cleaned_row))
		data = np.array(data)
	return data, zip_codes

def parse_economic_data(): # parse just economic data
	with open('./data/combined_data_by_zip_code/LA_Ranking_2019-04-04_21-54-40.csv') as combined_data:
		csv_reader = csv.DictReader(combined_data, delimiter = ',')
		data = []
		zip_codes = []
		for row in csv_reader:
			cleaned_row = []
			zip_codes.append(row['FIPS'])
			cleaned_row.append(float(row['% Employment, Unemployed, 2018']))
			cleaned_row.append(float(row['Median Household Income, 2018']))
			data.append(np.array(cleaned_row))
		data = np.array(data)
	return data, zip_codes

################################################################

data, zip_codes = parse_data()
kmeans = sk_learn_cluster(data, 3)

# cluster centers available at kmeans.cluster_centers_
labels = kmeans.predict(data) # clusters each zip code is closest to
cluster1 = [zip_codes[i] for i in range(len(zip_codes)) if labels[i] == 0]
cluster2 = [zip_codes[i] for i in range(len(zip_codes)) if labels[i] == 1]
cluster3 = [zip_codes[i] for i in range(len(zip_codes)) if labels[i] == 2]
cluster4 = [zip_codes[i] for i in range(len(zip_codes)) if labels[i] == 3]

with open('./data/la_economic_health_cluster_data3.csv', mode='w') as food_access_file:
    writer = csv.writer(food_access_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    for i in cluster1:
    	writer.writerow([i, 0])
    for j in cluster2:
    	writer.writerow([j, 1])
    for k in cluster3:
    	writer.writerow([k, 2])
    for l in cluster4:
    	writer.writerow([l, 3])

################################################################

data, zip_codes = parse_food_access_data()
kmeans = sk_learn_cluster(data, 4)
labels = kmeans.predict(data)
cluster1 = [zip_codes[i] for i in range(len(zip_codes)) if labels[i] == 0]
cluster2 = [zip_codes[i] for i in range(len(zip_codes)) if labels[i] == 1]
cluster3 = [zip_codes[i] for i in range(len(zip_codes)) if labels[i] == 2]

with open('./data/food_access_cluster_data.csv', mode='w') as food_access_file:
    writer = csv.writer(food_access_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    for i in cluster1:
    	writer.writerow([i, 0])
    for j in cluster2:
    	writer.writerow([j, 1])
    for k in cluster3:
    	writer.writerow([k, 2])

################################################################

data, zip_codes = parse_health_data()
kmeans = sk_learn_cluster(data, 2)
labels = kmeans.predict(data)
cluster1 = [zip_codes[i] for i in range(len(zip_codes)) if labels[i] == 0]
cluster2 = [zip_codes[i] for i in range(len(zip_codes)) if labels[i] == 1]
cluster3 = [zip_codes[i] for i in range(len(zip_codes)) if labels[i] == 2]

with open('./data/health_cluster_data.csv', mode='w') as food_access_file:
    writer = csv.writer(food_access_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    for i in cluster1:
    	writer.writerow([i, 0])
    for j in cluster2:
    	writer.writerow([j, 1])
    for k in cluster3:
    	writer.writerow([k, 2])

################################################################

data, zip_codes = parse_health_data()
kmeans = sk_learn_cluster(data, 2)
labels = kmeans.predict(data)
cluster1 = [zip_codes[i] for i in range(len(zip_codes)) if labels[i] == 0]
cluster2 = [zip_codes[i] for i in range(len(zip_codes)) if labels[i] == 1]
cluster3 = [zip_codes[i] for i in range(len(zip_codes)) if labels[i] == 2]

with open('./data/economic_cluster_data.csv', mode='w') as food_access_file:
    writer = csv.writer(food_access_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    for i in cluster1:
    	writer.writerow([i, 0])
    for j in cluster2:
    	writer.writerow([j, 1])
    for k in cluster3:
    	writer.writerow([k, 2])

################################################################
# use 'clustering' model to generate areas of higher and lower fast food density

data, zip_codes = parse_food_access_ff()
kmeans = sk_learn_cluster(data, 3)
labels = kmeans.predict(data)
cluster1 = [zip_codes[i] for i in range(len(zip_codes)) if labels[i] == 0]
cluster2 = [zip_codes[i] for i in range(len(zip_codes)) if labels[i] == 1]
cluster3 = [zip_codes[i] for i in range(len(zip_codes)) if labels[i] == 2]

with open('./data/food_access_ff.csv', mode='w') as food_access_file:
    writer = csv.writer(food_access_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    for i in cluster1:
    	writer.writerow([i, 0])
    for j in cluster2:
    	writer.writerow([j, 1])
    for k in cluster3:
    	writer.writerow([k, 2])

buckets = {}
for i in range(len(labels)):
	cluster = labels[i]
	point = data[i][1]
	if cluster in buckets:
		buckets[cluster].append(point)
	else:
		buckets[cluster] = [point]

ranges = {}
for i in buckets:
	min_ = min(buckets[i])
	max_ = max(buckets[i])
	ranges[i] = (min_, max_)
print(ranges)

######################################################################
# use 'clustering' model to generate areas of higher and lower supermarket density

data, zip_codes = parse_food_access_sm()
kmeans = sk_learn_cluster(data, 3)
labels = kmeans.predict(data)
cluster1 = [zip_codes[i] for i in range(len(zip_codes)) if labels[i] == 0]
cluster2 = [zip_codes[i] for i in range(len(zip_codes)) if labels[i] == 1]
cluster3 = [zip_codes[i] for i in range(len(zip_codes)) if labels[i] == 2]

with open('./data/food_access_sm.csv', mode='w') as food_access_file:
    writer = csv.writer(food_access_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    for i in cluster1:
    	writer.writerow([i, 0])
    for j in cluster2:
    	writer.writerow([j, 1])
    for k in cluster3:
    	writer.writerow([k, 2])

buckets = {}
for i in range(len(labels)):
	cluster = labels[i]
	point = data[i][1]
	if cluster in buckets:
		buckets[cluster].append(point)
	else:
		buckets[cluster] = [point]

ranges = {}
for i in buckets.keys():
	min_ = min(buckets[i])
	max_ = max(buckets[i])
	ranges[i] = (min_, max_)
print(ranges)

