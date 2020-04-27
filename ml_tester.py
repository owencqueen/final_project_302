# Tests the validity of the model on solving cubes for given number-of-rotation shuffles
import csv
import keras
import numpy as np
from r_cube.template_class import rubiks_cube
from r_cube import solver_helpers as sh

# Counts the proportion of correct guesses at each 
# Outputs a csv file in the current directory
def ml_test(model_name, f_name, ub = 20, each = 100, max_allow = 20):
	
	model = keras.models.load_model("cnn_solver/models/" + model_name)
	rc = rubiks_cube()

	with open(f_name, 'w', newline='') as file:

		writer = csv.writer(file)
		writer.writerow( ['rotations', 'solve_prop', 'solve_rotations'] )

		for i in range(1, ub + 1): # 1 - ub rotations 
					
			solve_sum = 0 # Reset sum variables before another iteration
			rot_sum   = 0
			
			for k in range(0, each): # Counts the number of times
				
				rc.shuffle(i)
				solve = 0
				j = 0
				while ( rc.if_solved() == 0 ):
					
				# If we reach the maximum number of rotations allowed for the model
					if (j > max_allow):
						solve = 0
						break
				
					rc_flat = sh.flatten_faces(rc)                # into string
					rc_np   = sh.two_dim_data(rc_flat)            # np array
					rc_np   = np.array(rc_np).reshape((1,2,12,1)) # np reshape
					out     = model.predict_classes(rc_np)        # prediction from model
	
					if (out[0] != 12):
						mv      = sh.get_move( rc, out[0] ) # Get the callable fn move	
						mv()                                # Make the move
					j += 1

					# If we solve the cube
					if (rc.if_solved() == 1):
						solve = 1
						break


				if (solve == 1): # If the model solved the cube
					solve_sum += 1
					rot_sum   += j
	
				rc.reset() # Reset the cube before next trial
				progress = 100 * ((k + (each * (i - 1))) / (each * ub))
 
				print("Progres:", progress, "%")
		
			solve_prop = (solve_sum) / (each)    # Proportion of times the model solved the cube
			
			if (solve_sum > 0):
				rot_prop   = (rot_sum) / (solve_sum) # Number of rotations per each solve trial
	
			else:
				rot_prop = 0
			r = [i, solve_prop, rot_prop]        # Input into the csv file
			
			writer.writerow( r ) # Write to csv file

# Same as above, just for random tester
def ml_test_random(model_name, f_name, ub = 20, each = 100, max_allow = 20):
	
	model = keras.models.load_model("cnn_solver/models/" + model_name)
	rc = rubiks_cube()

	mvs = sh.names_of_moves() # used for conversion to letter for comparison

	with open(f_name, 'w', newline='') as file:

		writer = csv.writer(file)
		writer.writerow( ['rotations', 'solve_prop', 'solve_rotations'] )

		for i in range(1, ub + 1): # 1 - ub rotations 
					
			solve_sum = 0 # Reset sum variables before another iteration
			rot_sum   = 0
			
			for k in range(0, each): # Counts the number of times
				
				rc.shuffle(i)
				solve = 0     # Checks if we have a solve or not
				j = 0         # Keeps track of all moves done

				last_move = -1       # Keeps track of last move done
				rand_check = 0       # Makes sure we don't keep calling random
				repeat_same_move = 0 # Keeps track of repeating the same move
			
				while ( rc.if_solved() == 0 ):
					
				
					rc_flat = sh.flatten_faces(rc)                # into string
					rc_np   = sh.two_dim_data(rc_flat)            # np array
					rc_np   = np.array(rc_np).reshape((1,2,12,1)) # np reshape
					out     = model.predict_classes(rc_np)        # prediction from model

					if (out[0] == 12):
						if (rc.if_solved() == 1):
							solve = 1
							break
						else:
							solve = 0
							break
	
					if ((mvs[last_move] == sh.counter_move( mvs[out[0]] ) and rand_check != 1 and last_move != -1) or (repeat_same_move == 4)):
						ranm = random_move(cube) # Calls random move
						rand_check = 1
						repeat_same_move = 0


					else:
						if (out[0] != 12):
							#Get the callable function move
							mv      = sh.get_move( rc, out[0] ) 
							mv()  # Make the move
					
						if (out[0] != last_move): # Reset counter if different move
							repeat_same_move = 0
						else:
							repeat_same_move += 1
					
					j += 1

					# If we solve the cube
					if (rc.if_solved() == 1):
						solve = 1
						break
				
					# If we reach the maximum number of rotations allowed for the model
					if (j > max_allow):
						solve = 0
						break


				if (solve == 1): # If the model solved the cube
					solve_sum += 1
					rot_sum   += j
	
				rc.reset() # Reset the cube before next trial
				progress = 100 * ((k + (each * (i - 1))) / (each * ub))
 
				print("Progres:", progress, "%")
		
			solve_prop = (solve_sum) / (each)    # Proportion of times the model solved the cube
			
			if (solve_sum > 0):
				rot_prop   = (rot_sum) / (solve_sum) # Number of rotations per each solve trial
	
			else:
				rot_prop = 0
			r = [i, solve_prop, rot_prop]        # Input into the csv file
			
			writer.writerow( r ) # Write to csv file

# Input for the model
mn = input("Name of model to test?: ")

upper_bound = input("Upper bound of shuffles for tests?: ")
upper_bound = int(upper_bound)

nt = input("Number of times for each test?: ")
nt = int(nt)

mxa = input("Maximum number of rotations the model is allowed?: ")
mxa = int(mxa)

data = input("Name of csv file to write to?: ")

which_test = input("Which tester to use? (model_test or model_test_random): ")

# Error checking to make sure we run the right tester
while (which_test != "model_test" and which_test != "model_test_random"):
	which_test = input("Which tester to use? (model_test or model_test_random): ")

if (which_test == "model_test"):
	ml_test( model_name = mn, ub = upper_bound, f_name = data, each = nt)

else:
	ml_test_random( model_name = mn, ub = upper_bound, f_name = data, each = nt)
