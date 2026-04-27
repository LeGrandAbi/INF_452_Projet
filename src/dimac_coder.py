import sys

def var_from_coords(matrice_size, x, y):
	return y*matrice_size + x + 1


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
	i = 1
	for y in range(len(matrice)):
		for x in range(len(matrice)):
			if matrice[y][x] == 1:
				file_content = file_content + str(i) + " 0\n"
			elif matrice[y][x] == -1:
				file_content = file_content + str(-i) + " 0\n"
			i = i + 1


	# rajouter les clauses de voisinnage
	size = len(matrice)
	for y in range(size - 1):
		for x in range(size - 1):
			file_content = file_content + str(-var_from_coords(size, x, y)) + " "
			file_content = file_content + str(var_from_coords(size, x+1, y)) + " "
			file_content = file_content + str(var_from_coords(size, x, y+1)) + " "
			file_content = file_content + str(var_from_coords(size, x+1, y+1)) + " 0\n"


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