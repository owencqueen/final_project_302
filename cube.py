import random

def cube_upp(self):
	rotate(self, "u", "cw")
def cube_upp_p(self):
	rotate(self, "u", "ccw")
def cube_ri(self):
	rotate(self, "r", "cw")
def cube_ri_p(self):
	rotate(self, "r", "ccw")
def cube_fr(self):
	rotate(self, "f", "cw")
def cube_fr_p(self):
	rotate(self, "f", "ccw")
def cube_do(self):
	rotate(self, "d", "cw")
def cube_do_p(self):
	rotate(self, "d", "ccw")
def cube_le(self):
	rotate(self, "l", "cw")
def cube_le_p(self):
	rotate(self, "l", "ccw")
def cube_ba(self):
	rotate(self, "b", "cw")
def cube_ba_p(self):
	rotate(self, "b", "ccw")


# Rotate a specific face of the cube
# option is either "ccw" or "cw"
def rotate(self, face, option):
	
	if ((option != "ccw") and  (option != "cw")):
		print("Wrong option")
		return -1
	
	# Decide which face will be turned
	if   (face == "u"):
		self.u = move_around(self.u, option)
	elif (face == "r"):
		self.r = move_around(self.r, option)
	elif (face == "f"):
		self.f = move_around(self.f, option)
	elif (face == "d"):
		self.d = move_around(self.d, option)
	elif (face == "l"):
		self.l = move_around(self.l, option)
	elif (face == "b"):
		self.b = move_around(self.b, option)

	if (option == "ccw"):	
		self = check_cube(self, face, "regular")
	else:
		self = check_cube(self, face, "other") 
	
	return self
	
def move_around(face, option):
	if (option == "cw"):
		temp = face[0][0]
		face[0][0] = face[1][0]
		face[1][0] = face[1][1]
		face[1][1] = face[0][1]
		face[0][1] = temp
	else:
		temp = face[0][0]
		face[0][0] = face[0][1]
		face[0][1] = face[1][1]
		face[1][1] = face[1][0]
		face[1][0] = temp
	
	return face
	
# Changes all the values around a rotated face after rotation
def check_cube(self, precedence, direction):
	
	# Numeric variable for each face
	F = 1
	B = 1
	L = 1
	R = 1
	U = 1
	D = 1

	# Codes:
	#	1 = Adjacent
	#   0 = Don't change

	#Need some math to determine which faces to turn

	if   (precedence == "b"):
		F = 0
		
		# Our line of faces is: u l d r
		
		# To be rotated:
		#  1. Top of u
		#  2. Bottom of d
		#  3. Left of l
		#  4. Right of r

		if (direction == "regular"):
			for i in range(0, self.dim):
				temp_val = self.r[i][self.dim - 1]
				self.r[i][self.dim - 1] = self.d[self_dim - 1][self.dim - i - 1]
				self.d[self.dim - 1][self.dim - i - 1] = self.l[self.dim - i - 1][0]
				self.l[self.dim - i - 1][0] = self.u[0][i]
				self.u[0][i] = temp_val
			
		else:
			for i in range(0, self.dim):
				temp_val = self.r[i][self.dim - 1]
				self.r[i][self.dim - 1] = self.u[0][i]
				self.u[0][i] = self.l[self.dim - i - 1][0]
				self.l[self.dim - i - 1][0] = self.d[self.dim - 1][self.dim - i - 1]
				self.d[self.dim - 1][i] = temp_val
			
				

	elif (precedence == "f"):
		B = 0
		# To be rotated:	
		#  1. Bottom of u	
		#  2. Left of r
		#  3. Top of d
		#  4. Right of l

		if (direction == "regular"):
			for i in range(0, self.dim):
				temp_val = self.r[i][0]
				self.r[i][0] = self.u[self.dim - 1][i]
				self.u[self.dim - 1][i] = self.l[self.dim - i - 1][self.dim]
				self.l[self.dim - i - 1][self.dim - 1] = self.d[0][self.dim - i - 1]
				self.d[0][self.dim - i - 1] = temp_val
		else:
			for i in range(0, self.dim):
				temp_val = self.r[i][0]
				self.r[i][0] = self.d[0][self.dim - i - 1]
				self.d[0][self.dim - i - 1] = self.l[self.dim - i - 1][self.dim - 1]
				self.l[self.dim - i - 1][self.dim - 1] = self.u[self.dim - 1][i]
				self.u[self_dim - 1][i] = temp_val


	elif (precedence == "l"):
		R = 0

		if (direction == "regular"):
			for i in range(0, self.dim):
				temp_val = self.u[i][0]
				self.u[i][0] = self.b[i][self.dim - 1]
				self.b[i][self.dim - 1] = self.d[self.dim - i - 1][0]
				self.d[self.dim - i - 1][0] = self.f[i][0]
				self.f[i][0] = temp_val

		else:
			for i in range(0, self.dim):
				temp_val = self.u[i][0]
				self.u[i][0] = self.f[i][0]
				self.f[i][0] = self.d[self.dim - i - 1][0]
				self.d[self.dim - i - 1][0] = self.b[i][self.dim - 1]
				self.b[i][self.dim - 1] = temp_val
				

	elif (precedence == "r"):
		L = 0
		if (direction == "regular"):
			for i in range(0, self.dim):
				temp_val = u[self.dim - 1][i]
				self.u[self.dim - 1][i] = self.f[self.dim - 1][i]
				self.f[self.dim - 1][i] = self.d[self.dim - 1][i]
				self.d[self.dim - 1][i] = self.b[0][self.dim - i - 1]
				self.b[0][self.dim - i - 1] = temp_val
			
		else:
			for i in range(0, self.dim):
				temp_val = self.u[self.dim - 1][i]
				self.u[self.dim - 1][i] = self.b[0][self.dim - i - 1]
				self.b[0][self.dim - i - 1] = self.d[self.dim - 1][i]
				self.d[self.dim - 1][i] = self.f[self.dim - 1][i]
				self.f[self.dim - 1][i] = temp_val
				

	elif (precedence == "u"):
		D = 0
		
		temp = self.f[0]

		# We're moving the top ccw
		if (direction == "regular"):	
			for i in range(0, self.dim):
				self.f[0][i] = self.r[0][i]
				self.r[0][i] = self.b[0][i]
				self.b[0][i] = self.l[0][i]
				self.l[0][i] = temp[i]
		
		else: # We're moving the top cw
			for i in range(0, self.dim):
				self.f[0][i] = self.l[0][i]
				self.l[0][i] = self.b[0][i]
				self.b[0][i] = self.r[0][i]
				self.r[0][i] = temp[i]


	elif (precedence == "d"):
		U = 0
		ind = self.dim - 1
		temp = self.f[ind]

		if (direction == "regular"):	
			for i in range(0, self.dim):
				self.f[ind][i] = self.r[ind][i]
				self.r[ind][i] = self.b[ind][i]
				self.b[ind][i] = self.l[ind][i]
				self.l[ind][i] = temp[i]
		
		else:
			for i in range(0, self.dim):
				self.f[ind][i] = self.l[ind][i]
				self.l[ind][i] = self.b[ind][i]
				self.b[ind][i] = self.r[ind][i]
				self.r[ind][i] = temp[i]

		return self

# Shuffles the cube (calls random moves repeatedly)
def cube_shuffle(self, rotations):

	while(rotations > 0):

		check = random.randint(1, 12)

		if (check == 1):
			self.front()
		elif (check == 2):
			self.front_prime()
		elif (check == 3):
			self.back()
		elif (check == 4):
			self.back_prime()
		elif (check == 5):
			self.up()
		elif (check == 6):
			self.up_prime()
		elif (check == 7):
			self.down()
		elif (check == 8):
			self.down_prime()
		elif (check == 9):
			self.left()
		elif (check == 10):
			self.left_prime()
		elif (check == 11):
			self.right()
		elif (check == 12):
			self.right_prime()

		rotations -= 1

# Checks if the cube has been solved
def cube_if_solved(self):

	check = 1

	if(self.f[0][0] != self.f[0][1] or self.f[0][1] != self.f[1][0] or self.f[1][0] != self.f[1][1]) {
		check = 0
	}


	if(self.b[0][0] != self.b[0][1] or self.b[0][1] != self.b[1][0] or self.b[1][0] != self.b[1][1]) {
		check = 0
	}

	if(self.u[0][0] != self.u[0][1] or self.u[0][1] != self.u[1][0] or self.u[1][0] != self.u[1][1]) {
		check = 0
	}

	if(self.d[0][0] != self.d[0][1] or self.d[0][1] != self.d[1][0] or self.d[1][0] != self.d[1][1]) {
		check = 0
	}

	if(self.l[0][0] != self.l[0][1] or self.l[0][1] != self.l[1][0] or self.l[1][0] != self.l[1][1]) {
		check = 0
	}

	if(self.r[0][0] != self.r[0][1] or self.r[0][1] != self.r[1][0] or self.r[1][0] != self.r[1][1]) {
		check = 0
	}

	if(check == 1):
		print("Solved")
		return 1
	else:
		print("Not Solved")
		return 0

