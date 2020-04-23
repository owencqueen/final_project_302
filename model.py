# Function that creates, formats, and trains the neural network

import keras
from keras.layers import Activation
from keras.layers import Conv2D, BatchNormalization, Dense, Flatten, Reshape

# x_train: training data
# y_train: training labels
# bs: batch size for .fit
# ep: epoch for .fit

def train_obo(x_train, y_train, bs = 20, ep = 2, mod_name = 'obo.model'):

	model = keras.models.Sequential() # Initialize sequential mopdel for keras network
	
	# See notes on documentation for description of below
	model.add(Conv2D(50, kernel_size = (2,2), activation='relu', padding='same', input_shape = (2, 12, 1 )))
	model.add(BatchNormalization())
	model.add(Conv2D(50, kernel_size = (2,2), activation='relu', padding='same'))
	model.add(BatchNormalization())
	model.add(Conv2D(100, kernel_size = (1,1), activation='relu', padding='same'))

	model.add(Flatten())             # Necessay before dense layer
	model.add(Dense(13))             # Number of possible outputs is 13
	model.add(Activation('softmax')) # Activation function for output layer

	adam = keras.optimizers.adam(lr=0.001)            # Optimization function
	model.compile(loss = 'sparse_categorical_crossentropy', optimizer = adam, metrics = ['accuracy'])
	# spare_categorical_crossentropy: function to calculate loss
	# Using adam optimizer function
	# Measuring our model by 'accuracy' of predictions

	model.fit(x_train, y_train, batch_size = bs, epochs = ep, shuffle = True, verbose = 2)
	# Batch size: how many batches of samples do you want to train at a time
	#   Somewhat arbitrary number
	# Epoch: how many times do you want to run through the data?
	# shuffle: if you want to shuffle the data for every epoch
	# verbose: How much output do you want the .fit function to show over each epoch?

	model.save(mod_name) # Saves the model in local directory
