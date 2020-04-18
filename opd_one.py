import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from solver_helpers import two_dim_data

def get_data(file):

	data = pd.read_csv(file)
	
	s = data['state']
	m = data['move']

	# Need to make a Python array of numpy arrays
	train_samples = []	

	for i in s:
		ind = two_dim_data(i)
		ind = np.array(ind).reshape((2,12,1))
		train_samples.append( ind )

	# Then make a numpy array of numpy arrays
	train_samples = np.array(train_samples)
	
	# Simple numpy array of strings of moves
	train_labels  = np.array(m)

	# Split the data for use in the keras model
	x_train, x_test, y_train, y_test = train_test_split(train_samples, train_labels, test_size = 0.2, random_state = 42)
	return x_train, x_test, y_train, y_test
