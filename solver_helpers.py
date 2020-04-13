import random

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

# Returns an array of the move functions in the rubiks_cube object passed to arg
def moves(cube):
	mvs = [ cube.front, cube.front_prime, cube.back, cube.back_prime, cube.up, cube.up_prime, cube.down, cube.down_prime, cube.left, cube.left_prime, cube.right, cube.right_prime ]
	return mvs

def names_of_moves():
	mvs = [ "F", "F`", "B", "B`", "U", "U`", "D", "D`", "L", "L`", "R", "R`" ]
	return mvs

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

