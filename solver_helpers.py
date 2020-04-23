import random
import numpy as np

# Makes a random move on the cube
def random_move(cube):

	check = random.randint(1, 12)

	if(check == 1):
		cube.front()
	elif (check == 2):
		cube.front_prime()
	elif (check == 3):
		cube.back()
	elif (check == 4):
		cube.back_prime()
	elif (check == 5):
		cube.up()
	elif (check == 6):
		cube.up_prime()
	elif (check == 7):
		cube.down()
	elif (check == 8):
		cube.down_prime()
	elif (check == 9):
		cube.left()
	elif (check == 10):
		cube.left_prime()
	elif (check == 11):
		cube.right()
	elif (check == 12):
		cube.right_prime()	

	return (check - 1)

# Returns an array of the move functions in the rubiks_cube object passed to arg
def moves(cube):
	mvs = [ cube.front, cube.front_prime, cube.back, cube.back_prime, cube.up, cube.up_prime, cube.down, cube.down_prime, cube.left, cube.left_prime, cube.right, cube.right_prime ]
	return mvs


# Returns an array of the names of moves
def names_of_moves():
	mvs = [ "F", "F`", "B", "B`", "U", "U`", "D", "D`", "L", "L`", "R", "R`" ]
	return mvs


# Given the number of a move, returns the character representation
def mv_num_to_char(mv_num):
	
	mvs = names_of_moves()
	
	if (mv_num == 12):
		return "None"

	return mvs[mv_num]


# Flattens all of the face data into one array
# Must remain consistent for each flatten
def flatten_faces(rc):
	flat = ""
	around_arr = [ rc.f, rc.r, rc.b, rc.l ]

	for i in around_arr:
		flat += i[0][0]
		flat += i[0][1]

	for i in around_arr:
		flat += i[1][0]
		flat += i[1][1]
	
	around_arr = [ rc.u, rc.d ]
	
	for i in around_arr:
		for j in range(0, 2):
			for k in range(0, 2):
				flat += i[j][k]

	return flat


# Gives the counter move of a given move
# char_name is character representation of a move
def counter_move(char_name):
	
	mvs = names_of_moves()
	if char_name not in mvs:
		print("Name is not a valid move")
		return 0
	ind = mvs.index(char_name)
	
	if ( ind % 2 == 1 ):
		return mvs[ ind - 1 ]
	else:
		return mvs[ ind + 1 ] 		


# 'f' denotes a function return
# Returns the function to counter a given character representation of a move
def counter_move_f(r, char_name):

	if (char_name == "F"):
		return r.front_prime
	elif (char_name == "F`"):
		return r.front	
	elif (char_name == "B"):
		return r.back_prime	
	elif (char_name == "B`"):
		return r.back	
	elif (char_name == "U"):
		return r.up_prime	
	elif (char_name == "U`"):
		return r.up	
	elif (char_name == "D"):
		return r.down_prime
	elif (char_name == "D`"):
		return r.down
	elif (char_name == "L"):
		return r.left_prime
	elif (char_name == "L`"):
		return r.left
	elif (char_name == "R"):
		return r.right_prime
	elif (char_name == "R`"):
		return r.right
	
def get_move(r, char_name):
	if (char_name == "F"):
		return r.front
	elif (char_name == "F`"):
		return r.front_prime	
	elif (char_name == "B"):
		return r.back	
	elif (char_name == "B`"):
		return r.back_prime	
	elif (char_name == "U"):
		return r.up	
	elif (char_name == "U`"):
		return r.up_prime	
	elif (char_name == "D"):
		return r.down
	elif (char_name == "D`"):
		return r.down_prime
	elif (char_name == "L"):
		return r.left
	elif (char_name == "L`"):
		return r.left_prime
	elif (char_name == "R"):
		return r.right
	elif (char_name == "R`"):
		return r.right_prime

	elif (char_name == 0):
		return r.front
	elif (char_name == 1):
		return r.front_prime	
	elif (char_name == 2):
		return r.back	
	elif (char_name == 3):
		return r.back_prime	
	elif (char_name == 4):
		return r.up	
	elif (char_name == 5):
		return r.up_prime	
	elif (char_name == 6):
		return r.down
	elif (char_name == 7):
		return r.down_prime
	elif (char_name == 8):
		return r.left
	elif (char_name == 9):
		return r.left_prime
	elif (char_name == 10):
		return r.right
	elif (char_name == 11):
		return r.right_prime
	


# Changes characters into numbers centered about 0
def ch_to_num(ch):

	if (ch == 'w'):
		return -1.5

	elif (ch == 'r'):
		return -1

	elif (ch == 'b'):
		return -0.5

	elif (ch == 'o'):
		return 0.5

	elif (ch == 'g'):
		return 1

	elif (ch == 'y'):
		return 1.5
	

# Two dimensionalize the data from flatten_faces
# Returns a numpy array of dimension 2row x 12col
def two_dim_data(ring):

	top_side = ring[0:8]   # Top of the side faces
	bot_side = ring[8:16]  # Bottom of the side faces
	
	top_up   = ring[16:18] # Upper part of the top
	top_d    = ring[18:20] # Lower part of the top

	bot_up   = ring[20:22] # Upper part of the bottom
	bot_d    = ring[22:24] # Lower part of the bottom

	tp = top_up + top_side + bot_up # Concatenating substrings
	dn = top_d + bot_side +  bot_d

	whole = tp + dn
	whole_mat = []

	for i in range(0, len(whole)): # Change each character into number
		whole_mat.append(ch_to_num( whole[i] ))

	whole_mat = np.array(whole_mat)            # Convert to numpy array
	whole_mat = np.reshape(whole_mat, (2, 12)) # Fix dimension into 2x12 matrix

	return whole_mat


# Converts the solution into the form that the ML model can read
# If op == 1, this means that sol argument is only one character i.e. one move
# If into_num = 1, returns the numerical value of the move 
#    ( as based off of names_of_moves() convention in solver_helpers ) 
def convert_sol(sol, op = 0, into_num = 0):

        s = ''

        if (into_num == 1):
                mvs = sh.names_of_moves()
                s = mvs.index(sol)


        else:
                if (op == 1):
                        if (len(sol) > 1):
                                s = sol[0].lower()
                        else:
                                s = sol
                else:
                        for i in range(0, len(sol)):
                                if (len(sol[i]) > 1):
                                        s += sol[i][0].lower()
                                else:
                                        s += sol[i]
        return s
