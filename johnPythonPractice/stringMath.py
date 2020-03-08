# John Greathouse
# This function is an attempt to farmiliarize myself with Python
# 
# What I'm aiming to do:
#    Make a string-math based program that can add, subtract and multiply nums of any size


def main():

	file = "data/inputs2.txt"
	data = open(file, 'r') # Open file of operations

	
	
	line = str(data.readline() ) # Read first line for loop

	while line != "": 
	# For all lines in file
		
		arg = [] # Declare new list

		for val in line.split(): 
		# Get arguments from file
			
			if val != '\n': # Ignores Newline
				arg.append(str(val) )

		
		""" Check which operation to call """
		if arg[0] == '*':
		#call mult
			print(str_mult(arg[1:3]) )
		if arg[0] == '+':
		#call add
			print(str_add(arg[1:3]) )
		if arg[0] == '-':
		#call sub
			print(str_sub(arg[1:3]) )

		
		line = data.readline() # Continue reading in vals



def str_mult(arg):
	
	val1 = arg[0]
	val2 = arg[1]
	# Get vals to mult
	
	tot = ''
	z = ''
	# Total and zero strings

	for i in range(len(val1),-1,-1):
	# Goes through all values in val1

		a = int(val1[i]) # Get value of ith number
		
		for j in range(0,a):
		# Add val2 to total val1[i] times
			
			b = [tot, val2 + z]
			tot = str_add(b)
		
		z += '0' # Update the i's place counter

	return tot


def str_add(arg):
	
	val1, val2, sz = string_assim(arg)
	# Get vals to add

	tot = ''
	carry = 0
	# Keeps track of addition

	for i in range( (sz-1), -1,-1):


		a = int(val1[i])
		b = int(val2[i])

		a += b
		a += carry
		b = a%10
		
		tot = str(b) + tot
		

		if a > 9:
			carry = 1
		else:
			carry = 0

	return snub_zer(tot)


def str_sub(arg):
	val1, val2, sz = string_assim(arg)

	borrow = 0

	tot = ''

	for i in range( (sz-1), -1, -1):
		
		a = int(val1[i])
		b = int(val2[i])

		a -= b
		a -= borrow
		b = a%10

		tot = str(b) + tot

		if a < 0:
			borrow = 1
		else:
			borrow = 0
		

	return snub_zer(tot)

def snub_zer(s_num):
	
	for i in range(len(s_num) ):	
		if s_num[i] != '0':
			s_num = s_num[i:len(s_num)]
			break
		if i == (len(s_num)-1):
			s_num = '0'

	return s_num
	

def string_assim(arg):
	
	val1 = arg[0]
	val2 = arg[1]


	if len(val1) > len(val2):
		val1 = '0' + val1
		sz = len(val1)
	else:
		val2 = '0' + val2
		sz = len(val2)
	
	while len(val1) != len(val2):
		if len(val1) > len(val2):
			val2 = '0' + val2
		else:
			val1 = '0' + val1

	return val1, val2, sz

main()

