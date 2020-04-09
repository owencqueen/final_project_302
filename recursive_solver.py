# Recursive solver for the cube
import template_class
from solver_helpers import moves
from solver_helpers import names_of_moves

mvs_ind = [] # Array for indices of the moves made

def rec_solve_master(rc, p = 0):

	turns = moves(rc)
	rec_solve(rc, 0, turns)

	if (p): # Prints all names of moves if specified
		names = names_of_moves()
		for i in range(0, len(mvs_ind)):
			print( names[ mvs_ind[i] ] )
	
	return mvs_ind
			

# Recursive procedure for the rec_solve_master
def rec_solve(rc, mvs, turns):
	
	if (rc.if_solved()):
		return "y"	

	if (mvs > 14): # From the internet - any combo of 2x2 can be solved in >= 14 moves
		return "n"

	for i in range(0, 12):                  # Iterate over 12 possible moves
		turns[i]                        # Make a move based on incrementing
		result = rec_solve(rc, mvs + 1) # Run recursion
		if ( result == "y" ):           # If we've reached a solution
			mvs_ind.insert(0, i)    # inserts at the front of the moves array
			return "y"              # Returns our positive solution value

	return "n"

# Main function that calls the recursive solver
def main():
	r = template_class.rubiks_cube()
	rec_solve_master()
	# May make this more robust later

main() # Run the main function
	
