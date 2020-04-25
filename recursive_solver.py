# Recursive solver for the cube
from r_cube import template_class
from r_cube.solver_helpers import moves
from r_cube.solver_helpers import names_of_moves
from r_cube.solver_helpers import counter_move
from r_cube.solver_helpers import counter_move_f

mvs_ind = [] # Array for indices of the moves made
names = names_of_moves()

def rec_solve_master(rc, num_shuf = 14, p = 0):

	turns = moves(rc)
	rec_solve(rc, 0, turns, 'j', num_shuf) # 'j' dummy argument

	if (p): # Prints all names of moves if specified
		for i in range(0, len(mvs_ind)):
			print( names[ mvs_ind[i] ] )
	
	return mvs_ind
			

# Recursive procedure for the rec_solve_master
def rec_solve(rc, mvs, turns, prev_move, num_shuf = 14):
	
	if (rc.if_solved()):
		return "y"	

	# From the internet - any combo of 2x2 can be solved in >= 14 moves
	if (mvs > num_shuf):
		return "n"
	
	for i in range(0, 12):
		if (prev_move == counter_move( names[i] )):
			continue	
		turns[i]()
		if (rc.if_solved()):
			mvs_ind.insert(0, i)
			return "y"
		else:
			counter = counter_move_f(rc, names[i])
			counter()

	for i in range(0, 12):                  # Iterate over 12 possible moves
		# Makes recursion faster by skipping over move
                #    that makes last move redundant
		if (prev_move == counter_move( names[i] )):
			continue	
		#print(i)
		#print("Moves: %d" % mvs)
		turns[i]()                      # Make a move based on incrementing		
		result = rec_solve(rc, mvs + 1, turns, names[i]) # Run recursion
		if ( result == "y" ):           # If we've reached a solution
			mvs_ind.insert(0, i)    # inserts at the front of the moves array
			return "y"              # Returns our positive solution value

	return "n"



# Main function that calls the recursive solver
def main():
	r = template_class.rubiks_cube()
	r.front()
	r.back()
	r.down_prime()
	r.front_prime()
	rec_solve_master(r, 4, 1)
	# May make this more robust later

main() # Run the main function
	
