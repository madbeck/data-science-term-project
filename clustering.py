from sklearn.cluster import KMeans
import csv
import numpy as np

def sk_learn_cluster(X, K):
	"""
	TODO: Implement Sci-Kit Learn's kmeans functionality

	:param X: 2D np array containing features of the words
	:param Y: 1D np array containing labels 
	:param K: number of clusters
	"""
	kmeans = KMeans(n_clusters=K, random_state=0).fit(X)
	return kmeans

def parse_data():
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

################################################################

data, zip_codes = parse_data()
kmeans = sk_learn_cluster(data, 2)

# cluster centers available at kmeans.cluster_centers_
labels = kmeans.predict(data) # clusters each zip code is closest to
print(zip_codes)
print(labels)

cluster1 = [zip_codes[i] for i in range(len(zip_codes)) if labels[i] == 1]
cluster2 = [zip_codes[i] for i in range(len(zip_codes)) if labels[i] == 0]
print(len(cluster1))
print(len(cluster2))
print(cluster1)

