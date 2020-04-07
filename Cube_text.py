# John Greathouse
# Text-based User Interfacing

import sys
#import template_class
import check_cube


# Commonly Used Strings
usage = 'usage: Cube_text.py cube_size\n\n(type "help" for argument info)'

help_arg = '\n    With cube_type, we read the dimensions\
 of\n    your cube such as a 2x2 cube or a 3x3 cube.\n\n   \
 Arguments "3" or "2" are allowed.\n    Arguments "3x3" or "2x2" are not.\n\n    Some sizes\
 are not supported.\n\n\nusage: Cube_text.py cube_size\n'

unsupp = 'That size of cube is not supported.'

help_cmd = '\n    Commands:\n  Quit:          "q" or "quit" or "e" or "exit"\n  Reset cube:\
    "reset"\n  Print:         "print"\n  Shuffle:       "shuffle"\n  Rotations:     "rotate"\
      (Rotation examples: U\'2 or B or l\'2 or D2U1)\n  Check solved:  "solved"\n\n'

intro = 'Welcome to a text-based Cube Interface!\nType "help" to see a list of commands.\n'

enter = " Enter a command:\n"

unk_cm = '\n Unknown command.\n Type "help" to see a list of commands.\n'




def main():
### Continuously Reads inputs  ###	

# Error Checking:
	# Argument Check
	if len(sys.argv) != 2:
		print(usage)
		exit()

	# Help print Statement
	if sys.argv[1].lower() == 'help':
		print(help_arg)
		exit()

	arg = str(sys.argv[1])

	# Supported Cubes	
	if arg.lower().isnumeric():
		i = int(arg)
		# If cube dim within bounds (only 2 right now)
		if i < 2 or i > 2:
			print(unsupp, '\n')
			print(usage)
			exit()
	else:
		print(usage)
		exit()

# Program Start
	# Declare Cube
#	cube = rubiks_cube()
	cube = 0

	# Print Intro Text
	print(intro)
	
	# Get initial Input
	usr_in = input(enter)
	print()

	# Handle inputs
	while(not usr_in.lower() == 'q' and not usr_in.lower() == 'quit' \
		and not usr_in.lower() == 'exit' and not usr_in.lower() == 'e'): 
	
		# Calls commands for cube
		in_handler(cube, usr_in)
		
		# Gets the input
		usr_in = input(enter)
		print()
	
	print("\n~Exiting interface~")



def in_handler(cube, cmmd):
	
	if cmmd.lower() == 'help':
		print(help_cmd)
	
	elif cmmd.lower() == "reset":
#		cube.clear()
		print(" Cube reset.\n")
		pass
	
	elif cmmd.lower() == "print":
#		print_cube(cube)
		pass
	
	elif cmmd.lower() == "shuffle":	
		i = input(" How many rotations for shuffle?\n")
		print()
		
		if i.isnumeric():
#			cube.shuffle(i)
			print('\n Shuffled' + i + 'amount of times. \n')
		else:
			print("\n Can't shuffle", i, "amount of times.\n")	

	elif cmmd.lower() == "solved":
#		cube.if_solved()
		pass
	elif cmmd.lower() == "rotate":
		rots = input(" List your rotations:\n")
		
		if len(rots) == 0:
			print(" You didn't enter any rotations.\n")
			return

		print()
		if read_rotations(cube, rots):
			print(" Rotations read.\n")
			return
		else:
			print(" Couldn't read rotation command(s).\n")
	else:
		print(unk_cm)
		return

def do_moves(cube, move_list):

	rot = 0

	for i in move_list:
		
		try:
			num_rot = int(i[2])
		except:
			num_rot = 1

		try:
			t = i[1]
			if t == "'":
				isP = 1
			else:
				num_rot = int(t)
				isP = 0
		except:
			isP = 0


		if i[0] == 'l':
			if isP:
#				rot = cube.left_prime
				pass
			else:
#				rot = cube.left
				pass
		
		elif i[0] == 'r':
			if isP:
#				rot = cube.right_prime
				pass
			else:
#				rot = cube.right
				pass

		elif i[0] == 'u':
			if isP:
#				rot = cube.up_prime
				pass
			else:
#				rot = cube.up
				pass
		
		elif i[0] == 'd':
			if isP:
#				rot = cube.down_prime
				pass
			else:
#				rot = cube.down
				pass
	
		elif i[0] == 'b':
			if isP:
#				rot = cube.back_prime
				pass
			else:
#				rot = cube.back
				pass

		elif i[0] == 'f':
			if isP:
#				rot = cube.front_prime
				pass
			else:
#				rot = cube.front
				pass

		while num_rot > 0:
			if rot != 0:
				rot()
			num_rot -= 1
	
	return 1

def print_cube(cube):
	pass

def is_rot(letter):

	i = letter.lower();
	
	if i.isalpha() and (i == 'l' or i == 'r'\
		or i == 'u' or i == 'd' or i == 'b' \
		or i == 'f'):
		
		return 1
	else:
		return 0

def read_rotations(cube, rots):
	err = 0
	rot_list = []
	

	# Enter first command
	if is_rot(rots[0]):
		temp = [rots[0] ]
	else:
		return 0
	


	if len(rots) < 2:
		if do_moves(cube, temp):
			return 1


	for i in rots[1:]:
		
		# Letter case
		if is_rot(i):
			# Add previous
			rot_list.append(temp)
			temp = []	
			# Add current 
			temp.append(i)

		# Prime case
		elif i == "'" and temp != []:
			# Get character
			try:
				t = temp[0].lower()
			except:
				return 0
			# Check command in temp
			if not is_rot(t):
				err = 1
			else:
				temp.append(i)

		# Number case
		elif i.isnumeric():
			# Get rotation
			try:
				t1 = temp[0].lower()
			except:
				return 0
			# Get prime
			try:
				t2 = temp[1].lower()
				can_t2 = 1
			except:
				can_t2 = 0
			# Check commands in temp
			if not is_rot(t1) or (can_t2 and t2 != "'"):
				err = 1
			else:
				temp.append(i)
		
		elif i == ' ':
			pass
		else:
			err = 1
		
		if err:
			return 0

	# Add last rotation to list
	if temp != []:
		rot_list.append(temp)

	# Call commands
	if rot_list != []:
		if do_moves(cube, rot_list):
			return 1
	else:
		return 0


# Call Main
main()
