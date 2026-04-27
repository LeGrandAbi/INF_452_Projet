import sys

def encode_dimac(matrice, input_filepath):
	file_content = ""

	# rajouter les l'entete
	n_clauses_unit = 0 # nb de cellules =/= 0
	n_var = len(matrice)**2
	n_clauses = (len(matrice) -1)**2 + n_clauses_unit
	file_content = f"p cnf {n_var} {n_clauses}\n"

	# rajouter les clauses unitaires
	

	# rajouter les clauses de voisinnage


	with open(input_filepath, "w") as f:
		f.write(file_content)
		f.close()


def decode_dimac(size, filepath):
	matrice = [[0 for j in range(size)] for i in range(size)]
	return matrice