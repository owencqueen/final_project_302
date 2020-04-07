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
	mvs = [ cube.front(), cube.front_prime(), cube.back(), cube.back_prime(), cube.up(), cube.up_prime(), cube.down(), cube.down_prime(), cube.left(), cube.left_prime(), cube.right(), cube.right_prime() ]
	return mvs
