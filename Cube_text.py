# John Greathouse
# Text-based User Interfacing

import sys
import template_class
import check_cube


# Commonly Used Strings
usage = 'usage: Cube_text.py cube_type\n\n(type "help" for argument info)'

help_arg = '\n    With cube_type, we read the dimensions\
 of\n    your cube such as a 2x2 cube or a 3x3 cube.\n\n   \
 Arguments "3" or "2" are allowed.\n    Arguments "3x3" or "2x2" are not.\n\n    Some sizes\
 are not supported.\n\n\nusage: Cube_text.py cube_type\n'

unsupp = 'That size of cube is not supported.'

help_cmd = '\n    Commands:\n  Quit:          "q" or "quit" or "e" or "exit"\n  Reset cube:\
    "reset"\n  Print:         "print"\n  Shuffle:       "shuffle"\n  Rotations:     "rotate"\
      (Rotation examples: U\'2 or B or l\'2 or D2U1)\n  Check solved:  "solved"\n'

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

	# Handle inputs
	while(not usr_in.lower() == 'q' and not usr_in.lower() == 'quit' \
		and not usr_in.lower() == 'exit' and not usr_in.lower() == 'e'): 
	
		# Calls commands for cube
		in_handler(cube, usr_in)
		
		# Gets the input
		usr_in = input(enter)
	
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
		i = input("\n How many rotations for shuffle?\n")
		print()
		if i.isnumeric():
#			cube.shuffle(i)
			pass
		else:
			print("\n Can't shuffle", i, "amount of times.\n")	

	elif cmmd.lower() == "solved":
#		cube.if_solved()
		pass
	elif cmmd.lower() == "rotate":
		rots = input("\n List your rotations:\n")
		print()
		read_rotations(rots)
	else:
		print(unk_cm)
		return

def do_moves(move_list):
	pass

def print_cube(cube):
	pass

def read_rotations(rots):
		err = 0

#		for i in cmmd:
#			curr = char(i)
#			
#			# Letter case
#			if i.isalpha():
#				pass
#
#			# Letter Prime case
#			elif i == "'":
#				pass
#			# Letter Number case
#			elif i == "'":
#				pass
#			# Letter Number Prime case
#			elif i == "":
#				pass
#			else:
#				err = 1
#			
#			if err:
#				print(unk_cm)
#				return

#	if rot_list != []:
#		do_moves(rot_list)

main()
