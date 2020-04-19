import keras
from template_class import rubiks_cube
from solver_helpers import flatten_faces
from solver_helpers import two_dim_data

def main():

	#create rubiks_cube object
	cube = rubiks_cube()


	shuf_num = input("How many shuffles? ")
	cube.shuffle(int(shuf_num))

	#turning cube data into numpy array
	flat = flatten_faces(cube)
	data = two_dim_data(flat)
	
	#put cube into model
	model = keras.models.load_model('models/jared_model')

	#predict needs 4dimensions, not sure if this is right?
	out = model.predict(data.reshape(1,2,12,1))
	#don't know what squeeze does
	out = out.squeeze()

main()
