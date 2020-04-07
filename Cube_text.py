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
		read_rotations(rots)
	else:
		print(unk_cm)
		return

def do_moves(move_list):
	pass

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

def read_rotations(rots):
	err = 0
	rot_list = []
	
	# Enter first command
	if is_rot(rots[0]):
		temp = [rots[0] ]
	else:
		return 0

	for i in rots[1:]:
		
		# Letter case
		if i.isalpha() and (i.lower() == 'l' or i.lower() == 'r' \
			or i.lower() == 'u' or i.lower() == 'd' or i.lower() == 'b'\
			or i.lower() == 'f'):
		
			# Add previous
			rot_list.append(temp)
			temp = []
			
			# Add current 
			temp.append[i]

		# Prime case
		elif i == "'" and temp != []:
			
			# Get character
			t = temp[0].lower()

			
			if not (t.isalpha() and (t == 'l' or t == 'r'\
				or t == 'u' or t == 'd' or t == 'b'  \
				or t == 'f') ):
				err = 1
			
			else:
				pass


		# Letter Number case
#		elif i == "'":
#			pass
#		# Letter Number Prime case
#		elif i == "":
#			pass
#		else:
#			err = 1
#		
#		if err:
#			print(unk_cm)
#			return

#	if rot_list != []:
#		do_moves(rot_list)

main()
