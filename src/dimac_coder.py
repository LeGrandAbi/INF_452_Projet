import sys

def encode_dimac(matrice, input_filepath):
	'''
	needs to be filled
	'''
	with open(input_filepath, "w") as f:
		f.write("p cnf 6 3\n")
		f.write("1 -5 6 4 0\n")
		f.write("-1 5 3 4 0\n")
		f.write("-3 -4 0\n")

def decode_dimac(size, filepath):
	'''
	needs to be filled
	'''
	matrice = [[0 for j in range(size)] for i in range(size)]
	return matrice