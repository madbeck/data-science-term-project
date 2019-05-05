import numpy as np
import pandas as pd
import random
import csv
from sklearn import linear_model
from sklearn.metrics import r2_score
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
from scipy import stats
import matplotlib.pyplot as plt

def split_data(data, prob):
	"""Split data into fractions [prob, 1 - prob]"""
	results = [], []
	for row in data:
		results[0 if random.random() < prob else 1].append(row)
	return results

def train_test_split(x, y, test_pct):
	"""Split the features X and the labels y into x_train, x_test and y_train, y_test
	designated by test_pct. A common convention in data science is to do a 80% training
	data 20% test data split"""
	data = zip(x, y)								# pair corresponding values
	train, test = split_data(data, 1 - test_pct)    # split the data set of pairs
	x_train, y_train = zip(*train)					# magical un-zip trick
	x_test, y_test = zip(*test)
	return x_train, x_test, y_train, y_test

features = ['unemployed', 'income', 'obesity', 'diabetes', 'one_km_sm', 'three_km_sm', 'one_km_ff', 'three_km_ff']
label = 'zip_code'

def MultipleLinearRegression(X, y, linear_model):

	lm = linear_model
	### DO NOT TOUCH THIS PORTION OF THE CODE###
	params = np.append(lm.intercept_,lm.coef_)
	predictions = lm.predict(X)

	newX = np.append(np.ones((len(X),1)), X, axis=1)
	MSE = (sum((y-predictions)**2))/(len(newX)-len(newX[0]))

	var_b = MSE*(np.linalg.inv(np.dot(newX.T,newX)).diagonal())
	sd_b = np.sqrt(var_b)
	ts_b = params/ sd_b

	p_values =[2*(1-stats.t.cdf(np.abs(i),(len(newX)-1))) for i in ts_b]

	myDF3 = pd.DataFrame()
	myDF3["Coefficients"],myDF3["Standard Errors"],myDF3["t values"],myDF3["Probabilites"] = [params,sd_b,ts_b,p_values]
	print(myDF3)


if __name__=='__main__':
	# Do not change this seed. It guarantees that all students perform the same train and test split
	random.seed(1)
	# Setting p to 0.2 allows for a 80% training and 20% test split
	p = 0.2
	X = []
	y = []
	#############################################
	# TODO: open csv and read data into X and y #
	#############################################
	def load_file(file_path):
		X = []
		y = []
		with open(file_path, 'r', encoding='latin1') as file_reader:
			reader = csv.reader(file_reader, delimiter=',', quotechar='"')
			next(reader)
			for row in reader:
				if row == []:
					continue
				explanatory_var = []

				##Obesity, 3km FF
				explanatory_var.append(float(row[9]))
				cnt = float(row[3])

				# explanatory_var.append(float(row[7]))
				# cnt = float(row[3])


				# ### Obesity, 1km, 1km
				# explanatory_var.append(float(row[6]))
				# explanatory_var.append(float(row[8]))
				# cnt = float(row[3])

				### Obesity, 3km, 3km
				# explanatory_var.append(float(row[7]))
				# explanatory_var.append(float(row[9]))
				# cnt = float(row[3])

				#Diabetes, 1km SM
				# explanatory_var.append(float(row[6]))
				# cnt = float(row[4])

				# ### Diabetes, 1km, 1km
				# explanatory_var.append(float(row[6]))
				# explanatory_var.append(float(row[8]))
				# cnt = float(row[4])

				# ### Diabetes, 3km, 3km
				# explanatory_var.append(float(row[6]))


				# explanatory_var.append(float(row[7]))
				# cnt = float(row[4])


				# ### FF, Unemployment, Income
				# explanatory_var.append(float(row[1]))



				# explanatory_var.append(float(row[2]))
				# explanatory_var.append(float(row[9]))
				# cnt = float(row[3])

				# ### SM, Unemployment, Income
				# explanatory_var.append(float(row[1]))
				# # explanatory_var.append(float(row[2]))
				# cnt = float(row[6])
				
				# explanatory_var = explanatory_var[explanatory_var != 0]
				# cnt = cnt[cnt != 0]

				X.append(explanatory_var)
				y.append(cnt)
		
		#X = X[X!=0]
		#y = y[y!=0]
		return np.array(X, dtype='float64'), np.array(y, dtype='float64')

	#X, y = load_file("/course/cs1951a/pub/stats/data/bike_sharing.csv")
	X, y = load_file("/Users/shehryarhasan/Desktop/out.csv")

	##################################################################################
	# TODO: use train test split to split data into x_train, x_test, y_train, y_test #
	#################################################################################
	x_train, x_test, y_train, y_test = train_test_split(X,y, p)
	x_train = np.array(x_train)
	x_test = np.array(x_test)
	y_train = np.array(y_train)
	y_test = np.array(y_test)

	# x_train = x_train[x_train != 0]
	# y_train = y_train[y_train != 0]
	# x_train = x_train[_train != 0]
	# x_train = x_train[x_train != 0]

	##################################################################################
	# TODO: Use Sci-Kit Learn to create the Linear Model and Output R-squared
	#################################################################################
	linear_model = LinearRegression().fit(x_train, y_train)
	tr_preds = linear_model.predict(x_train)
	preds = linear_model.predict(x_test)
	r2 = r2_score(y_train, tr_preds)
	mse_train = mean_squared_error(y_train, tr_preds)
	mse_test = mean_squared_error(y_test, preds)
	print("Training R-squared:" + str(r2))
	print("Training MSE:" + str(mse_train))
	print("Testing MSE:" + str(mse_test))
	plt.scatter(x_train, y_train)
	plt.plot(x_train, linear_model.predict(x_train),color='k')
	plt.ylim(-2)
	plt.title("Obesity vs Fast Foods")
	plt.legend(['P = 0.087691'], loc='upper right')
	plt.xlabel('Number of Fast Food Restaurants in 3KM')
	plt.ylim(22)
	plt.ylabel('Obesity rate')
	plt.show()
	
	MultipleLinearRegression(x_train, y_train, linear_model)
