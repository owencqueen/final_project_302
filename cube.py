
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
		
		if (direction == "regular"):
			temp = []
			
			# Go to far right of r face

			for i in range(0, len(r[0])):
				temp.append(r[i][len(r[0])])
				

	elif (precedence == "f"):
		B = 0
	elif (precedence == "l"):
		R = 0
	elif (precedence == "r"):
		L = 0
	elif (precedence == "u"):
		D = 0
		
		temp = self.f[0]

		if (direction == "regular"):	
			for i in range(0, self.dim):
				self.f[0][i] = self.r[0][i]
				self.r[0][i] = self.b[0][i]
				self.b[0][i] = self.l[0][i]
				self.l[0][i] = temp[i]
		
		else:
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


