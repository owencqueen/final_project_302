# John Greathouse
# This function is an attempt to farmiliarize myself with Python
# 
# What I'm aiming to do:
#    Make a string-math based input function

# This is probalby a really bad use of python, but it'll force me to learn how to write in this language!


def main():

	
	file = "data/inputs.txt"
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
			str_mult(arg[1:3])
		if arg[0] == '+':
		#call add
			str_add(arg[1:3])
		if arg[0] == '-':
		#call sub
			str_sub(arg[1:3])

		
		line = data.readline() # Continue reading in vals\



def str_mult(arg):
	
	val1 = arg[0]
	val2 = arg[1]


	if len(val1) > len(val2):
		val1 = '0' + val1
		sz = len(val1)
	else:
		val2 = '0' + val2
		sz = len(val1)

	for i in range( (sz-1),-1,-1):
		a = ''
#		print(i)

def str_add(arg):

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
	
	carry = 0

	tot = ''

	for i in range( (sz-1), -1,-1):
		
		a = int(val1[i])
		b = int(val2[i])
		
		a += b
		a += carry
		b = a%10
		
		if not(i == 0 and carry == 0):
			tot = str(b) + tot

		if a > 9:
			carry = 1
		else:
			carry = 0

	print(tot)

def str_sub(arg):
	print('sub ', arg)
	return



main()

