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
    "reset"\n  Print:         "print"\n  Shuffle:       "shuffle"\n  Moves:         "some_face""num_turns"\
                 (eg: U\'2 or B or l\'2 or D2U1)\n'

intro = 'Welcome to a text-based Cube Interface!\nType "help" to see a list of commands.\n'

enter = " Enter a command:\n"

def main():
### Continuously Reads inputs  ###	

	cube = rubiks_cube()

	# Argument Check
	if len(sys.argv) != 2:
		print(usage)
		exit()

	# Help print Statement
	if sys.argv[1].lower() == 'help':
		print(help_arg)
		exit()
	# Supported Cubes	
	if sys.argv[1].lower().isnumeric:
		i = sys.argv[1]
		if int(i) < 2 or int(i) > 3:
			print(unsupp, '\n')
			print(usage)
			exit()


	# Print Intro Text
		print(intro)
	
	# Get initial Input
	usr_in = input(enter)

	# Handle inputs
	while(not usr_in.lower() == 'q' and not usr_in.lower() == 'quit' \
		and not usr_in.lower() == 'exit' and not usr_in.lower() == 'e'): 
	
		# Calls commands for cube
		in_handler(usr_in)
		
		# Gets the input
		usr_in = input(enter)

def in_handler(input):
	if input.lower() == 'help':
		print(help_cmd)
	#some

def print_cube():
	pass


main()
