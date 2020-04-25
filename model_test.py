import keras
import numpy as np
import r_cube.solver_helpers as sh

from r_cube.template_class import rubiks_cube


def test_obo(mod_name, num_shuf):

	model = keras.models.load_model("cnn_solver/models/" + mod_name)
	rc = rubiks_cube()

	rc.shuffle(num_shuf)

	i = 0

	while ( rc.if_solved() == 0 ):
		rc_flat = sh.flatten_faces(rc)                # into string
		rc_np   = sh.two_dim_data(rc_flat)            # np array
		rc_np   = np.array(rc_np).reshape((1,2,12,1)) # np reshape
		out     = model.predict_classes(rc_np) 
		out_p	= sh.mv_num_to_char(int(out[0]))
		print(out_p) # Print out prediction

		mv      = sh.get_move( rc, out[0] ) # Get the callable fn move
		mv()                                # Make the move
		i += 1
		if (i > 20):
			print("No solve")
			break

	rc_flat = sh.flatten_faces(rc)     # into string
	print(rc_flat)	


mod = input("Model to test: ")

ns  = input("Number of rotations for shuffle: ")
ns  = int(ns)

test_obo(mod_name = mod, num_shuf = ns)
