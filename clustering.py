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

def main():
	with open('./data/combined_data_by_zip_code/LA_Ranking_2019-04-04_21-54-40.csv') as combined_data:
		csv_reader = csv.DictReader(combined_data, delimiter = ',')
		data = []
		for row in csv_reader:
			cleaned_row = []
			cleaned_row.append(float(row['% Employment, Unemployed, 2018']))
			cleaned_row.append(float(row['Median Household Income, 2018'])) # maybe flip this one?
			cleaned_row.append(float(row['% Body mass index - Obese, 2018']))
			cleaned_row.append(float(row['% Diabetes, 2018']))
			data.append(np.array(cleaned_row))
		data = np.array(data)

	kmeans = sk_learn_cluster(data, 4)
	return kmeans


################################################################

kmeans = main()
# cluster centers available at kmeans.cluster_centers_
labels = kmeans.predict(data) # clusters each zip code is closest to
print(labels)



