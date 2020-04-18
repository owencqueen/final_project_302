import keras
from keras.layers import Activation
from keras.layers import Conv2D, BatchNormalization, Dense, Flatten, Reshape

def train_mod(x_train, y_train):
	model = keras.model.Sequential()

	model.add(Conv2D(, kernel_size = (2, 2), activation = "relu", padding = 'same', input_shape = (2, 12, 1)))
	model.add(BatchNormalization())
	
