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
		# Does the brunt of the work
		# Reorders the cubes to move where they need to 

	def rotate(face, direction):
		# Math of reordering the cube - alters face
		# Calls check_cube(face)

	# Types of rotations
	#    Simple functions that just call rotate on given face
	def front():
	def front_prime():
	def back():
	def back_prime():
	
	def up():
	def up_prime():
	def down():
	def down_prime():

	def left():
	def left_prime():
	def right():
	def right_prime():

	# Other functions
	def shuffle(rotations):
	def if_solved():
