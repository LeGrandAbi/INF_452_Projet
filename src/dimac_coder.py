import sys

def var_from_coords(matrice_size, x, y):
	return y*matrice_size + x + 1


def connectvar_from_vars(matrice_size, x, y):
	size = matrice_size**2
	v = size + (x-1)*(size-1) + y - 1
	if x > y:
		v = v - 1
	return v

def get_n_clauses(matrice):
	l = len(matrice)

	n_clauses_unit = 0
	for y in range(l):
		for x in range(l):
			if matrice[y][x] != 0:
				n_clauses_unit = n_clauses_unit + 1 

	return 12*(l**5) - 24*(l**4) + (l**3) + 12*(l**2) - 2*l + 1 + n_clauses_unit


def encode_dimac(matrice, input_filepath):
	file_content = ""

	# rajouter l'entete

	n_var = len(matrice)**3
	n_clauses = get_n_clauses(matrice)
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
			# blanc
			file_content = file_content + str(-var_from_coords(size, x, y)) + " "
			file_content = file_content + str(-var_from_coords(size, x+1, y)) + " "
			file_content = file_content + str(-var_from_coords(size, x, y+1)) + " "
			file_content = file_content + str(-var_from_coords(size, x+1, y+1)) + " 0\n"
			# noir
			file_content = file_content + str(var_from_coords(size, x, y)) + " "
			file_content = file_content + str(var_from_coords(size, x+1, y)) + " "
			file_content = file_content + str(var_from_coords(size, x, y+1)) + " "
			file_content = file_content + str(var_from_coords(size, x+1, y+1)) + " 0\n"


	# rajouter les clauses de connectivite


	# rajouter les clauses de conditions de connectivite


	with open(input_filepath, "w") as f:
		f.write(file_content)
		f.close()


def decode_dimac(size, filepath):
	with open(filepath, "r") as f:
		content = f.readlines()[1]
		f.close()
	content = content.split()

	matrice = [[0 for j in range(size)] for i in range(size)]
	i = 0
	for y in range(size):
		for x in range(size):
			c = int(content[i])
			matrice[y][x] = c / abs(c)
			i = i + 1

	return matrice