import cube

class rubiks_cube:
	
	def __init__(self):
		self.check_cube = cube.check_cube
		dim = 2 # Defines the dimension of the cube; need it for check_cube

	f = []
	b = []
	u = []
	d = []
	l = []
	r = []

	def check_cube( precedence ):
		pass
		# Does the brunt of the work
		# Reorders the cubes to move where they need to 

	def rotate(face, direction):
		pass
		# Math of reordering the cube - alters face
		# Calls check_cube(face)

	# Types of rotations
	#    Simple functions that just call rotate on given face
	def front():
		pass
	def front_prime():
		pass
	def back():
		pass
	def back_prime():
		pass
	
	def up():
		pass
	def up_prime():
		pass
	def down():
		pass
	def down_prime():
		pass

	def left():
		pass
	def left_prime():
		pass
	def right():
		pass
	def right_prime():
		pass

	# Other functions
	def shuffle(rotations):
		pass
	def if_solved():
		pass
