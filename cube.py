import random


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

def shuffle():

	while(rotations > 0):

	    check = random.randint(1, 12)

		if(check == 1) {
			front()
		}
		elif (check == 2) {
			front_prime()
		}
		elif (check == 3) {
			back()
		}
		elif (check == 4) {
			back_prime()
		}
		elif (check == 5) {
			up()
		}
		elif (check == 6) {
			up_prime()
		}
		elif (check == 7) {
			down()
		}
		elif (check == 8) {
			down_prime()
		}
		elif (check == 9) {
			left()
		}
		elif (check == 10) {
			left_prime()
		}
		elif (check == 11) {
			right()
		}
		elif (check == 12) {
			right_prime()
		}

		rotations -= 1

def if_solved():

	check = 1

	for i in f:
		color = f[0]
		if(color != i):
			check = 0

	for i in b:
		color = b[0]
		if(color != i):
			check = 0

	for i in u:
		color = u[0]
		if(color != i):
			check = 0

	for i in d:
		color = d[0]
		if(color != i):
			check = 0

	for i in l:
		color = l[0]
		if(color != i):
			check = 0

	for i in r:
		color = r[0]
		if(color != i):
			check = 0

	if(check == 1):
		print("Solved")
	else:
		print("Not Solved")

def random_move():

	    check = random.randint(1, 12)

		if(check == 1) {
			front()
		}
		elif (check == 2) {
			front_prime()
		}
		elif (check == 3) {
			back()
		}
		elif (check == 4) {
			back_prime()
		}
		elif (check == 5) {
			up()
		}
		elif (check == 6) {
			up_prime()
		}
		elif (check == 7) {
			down()
		}
		elif (check == 8) {
			down_prime()
		}
		elif (check == 9) {
			left()
		}
		elif (check == 10) {
			left_prime()
		}
		elif (check == 11) {
			right()
		}
		elif (check == 12) {
			right_prime()
		}
	
	

