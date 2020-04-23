# Definition of the rubiks_cube class

import cube
import solver_helpers

class rubiks_cube:
	
	dim = 2 # Defines the dimension of the cube 
		# (i.e., faces as dim x dim dimensions)

	def __init__(self): # Constructor
		
		# Initialize 2d matrices to be face colors
		# Based off of convention of page on documentation
		self.f = [ ['r', 'r'], ['r', 'r'] ]
		self.b = [ ['o', 'o'], ['o', 'o'] ]
		self.u = [ ['w', 'w'], ['w', 'w'] ]
		self.d = [ ['y', 'y'], ['y', 'y'] ]
		self.l = [ ['g', 'g'], ['g', 'g'] ]
		self.r = [ ['b', 'b'], ['b', 'b'] ]
		
	# Declaring all move functions from cube file
	# All of these take argument self in cube.py,
	# however, you don't have to call them w/ self
	# Ex: front()

	front       = cube.cube_fr
	front_prime = cube.cube_fr_p
	back        = cube.cube_ba
	back_prime  = cube.cube_ba_p
	up          = cube.cube_upp
	up_prime    = cube.cube_upp_p
	down        = cube.cube_do
	down_prime  = cube.cube_do_p
	left        = cube.cube_le
	left_prime  = cube.cube_le_p
	right       = cube.cube_ri
	right_prime = cube.cube_ri_p

	# Declarations of other helper functions:
		
	if_solved   = cube.cube_if_solved
		# Checks if the cube is solved (returns bool)
		# Fn call syntax: if_solved()
	shuffle     = cube.cube_shuffle
		# Shuffles the cube 
		# (calls random moves for given number of rotations)
		# Fn call syntax: shuffle(rotations)
	reset       = cube.cube_reset
		# Resets the cube to its original state
		# Changes nothing but the data in the face arrays
		# Fn call syntax: reset()
