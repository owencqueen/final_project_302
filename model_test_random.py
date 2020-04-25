import keras
from template_class import rubiks_cube
from solver_helpers import flatten_faces
from solver_helpers import two_dim_data
from solver_helpers import get_move
from solver_helpers import counter_move
from solver_helpers import names_of_moves
from solver_helpers import random_move
from solver_helpers import mv_num_to_char

def main():

	#create rubiks_cube object
	cube = rubiks_cube()

	mod_name = input("What model do you want to use? ")

	shuf_num = input("How many shuffles? ")
	cube.shuffle(int(shuf_num))


	model = keras.models.load_model("models/" + mod_name)

	last_move = -1  #keeps track of last move done
	rand_check = 0  #makes sure we don't keep calling random continuously
	repeat_same_move = 0  #keeps track of repeating the same move
	count = 0 #keeps track of all moves done
	
	mvs = names_of_moves()  #used for conversion to letter for comparison

	while(cube.if_solved() == 0) :

		#model reads in data and makes prediction
		flat = flatten_faces(cube)
		data = two_dim_data(flat)
		out = model.predict_classes(data.reshape(1,2,12,1))
		
		#if this move is the counter of the last move (model is repeating itself) or if model has repeated same move 4 times
		if((mvs[last_move] == counter_move(mvs[out[0]]) and rand_check != 1 and last_move != -1) or (repeat_same_move == 4)):
			#perform a random move on cube
			ranm = random_move(cube)
			ranm_out = mv_num_to_char(ranm) 
			p_out = mv_num_to_char(int(out[0]))
			print(p_out),
			print("Called random move:", ranm_out) 
		
			#rand_check makes sure we don't call random check multiple times in a row
			rand_check = 1

			#reset counter for repeated moves
			repeat_same_move = 0
		else:
			#perform model's predicted move
			p_out = mv_num_to_char(int(out[0]))
			print(p_out)
			mv = get_move(cube, out[0])
			mv()

			#reset counter for repeated moves to 0 if the last move was different than current move
			if(out[0] != last_move) :
				repeat_same_move = 0
			else:
				repeat_same_move+=1
	
			#keep track of last move
			last_move = out[0]

			rand_check = 0
	
		#while loop ends if we have done 50 moves
		count+=1
		if(count == 50) :
			print("No solve (in less than 50 moves)")
			break

	

	final_state = flatten_faces(cube)
	print(final_state)


main()
