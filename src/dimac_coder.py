import sys

def encode_dimac(matrice, input_filepath):
	file_content = ""

	# rajouter l'entete
	n_clauses_unit = 0
	for y in range(len(matrice)):
		for x in range(len(matrice)):
			if matrice[y][x] != 0:
				n_clauses_unit = n_clauses_unit + 1 

	n_var = len(matrice)**2
	n_clauses = (len(matrice) -1)**2 + n_clauses_unit
	file_content = f"p cnf {n_var} {n_clauses}\n"

	# rajouter les clauses unitaires


	# rajouter les clauses de voisinnage


	with open(input_filepath, "w") as f:
		f.write(file_content)
		f.close()


def decode_dimac(size, filepath):
	with open(filepath, "r") as f:
		content = f.readlines()[1]
		f.close()
	content = content.split()

	matrice = [[0 for j in range(size)] for i in range(size)]
	return matrice