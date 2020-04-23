from model import train_obo
import opd_one as opd
import solver_helpers as sh
from template_class import rubiks_cube


def main(in_csv, batch_size, eps, mn):
	x_train, x_test, y_train, y_test = opd.get_data(in_csv)

#	print(len(x_train))	

#	for i in range(0, len(x_train)):
#		print(x_train[i])

	train_obo(x_train, y_train, bs = batch_size, ep = eps, mod_name = "models/" + mn)
	# Put the new model in "models" directory
		

# Prompting the user for parameters	
mod_name = input("Name of new model: ")

n_csv   = input("Data to be trained on: ")

bs = input("Batch size: ")
bs = int(bs)

ep = input("Num epochs (times data is passed through model): ")
ep = int(ep)

main(in_csv = n_csv, batch_size = bs, eps = ep, mn = mod_name)
