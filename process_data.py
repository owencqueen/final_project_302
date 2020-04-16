#still researching on this
import numpy as np
import pandas as pd


def get_data(file):


	data = pd.read_csv(file)

	state = data['state']
	moves = data['moves']

	state = np.array(state)
	moves = np.array(moves)

	#thinking we convert each string of 24 letters into 6x2x2
	#have numbers represent the colors and normalize around 0?
	#similar thing with moves possibly
