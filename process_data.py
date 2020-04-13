#still researching on this
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split


def get_data(file):


	data = pd.read_csv(file)

	state = data['state']
	moves = data['moves']
