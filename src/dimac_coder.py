def var_from_coords(matrice_size, x, y):
	'''
	returns the index of the variable representing the status of the cell matrice[y][x]

	in the modelisation:
	this variable is true if white
					false if black
	'''
	return y*matrice_size + x + 1


def connectvar_from_vars(matrice_size, x, y):
	'''
	returns the index of the variable representing the connectivity of two cells of index x and y
	x and y are not coords, they are the index value of each cell

	if x = (xa, xb) and y = (ya, yb)
	to get the connectivity variable between x and y
	we need to get the variable index of both x and y,
	with var_from_coords(matrice_size, xa, xb) and var_from_coords(matrice_size, ya, yb)
	'''
	size = matrice_size**2
	v = size + (x-1)*(size-1) + y
	if x < y:
		v = v - 1
	return v

def get_n_clauses(matrice):
	'''
	returns the number of clauses necessary to the resolution of the yin-yang problem

	n_clauses = n_squares + 2*nb_connect + nb_unit
	
	with l being the width/height of the board:
		n_squares = "the number of possible 2x2 squares on the board" = (l - 1)^2
		nb_connect = "the number of possible connection between cells" = l^2 * (l^2 - 1)
		nb_unit = "the quantity of unitary clauses / cells that need be stay intact"
	'''
	l = len(matrice)

	# a unitary clause is when a cell is defined (=/= 0)
	# since matrice[y][x] is white if it equals 1
	# 	and matrice[y][x] is black if it equals -1
	n_clauses_unit = 0
	for y in range(l):
		for x in range(l):
			if matrice[y][x] != 0:
				n_clauses_unit = n_clauses_unit + 1 

	return 2*(l**4) - 4*l + 2 + n_clauses_unit


def encode_dimac(matrice, input_filepath):
	'''
	Write in a given filepath the dimac file associated with the given board (matrice)

	in order:
		write the header in a string called "file_content"
		append in the same string the unitary constraints
		append in the same string the no_square constraints
		append in the same string the connectivity constraints
		append in the same string the connectivity_conditions constraints (what it means for two cells to be connected)
		writes into the given filename the produced string
	'''

	file_content = ""

	# produce and append to file_content the header
	n_var = len(matrice)**4 
	n_clauses = get_n_clauses(matrice)
	file_content = f"p cnf {n_var} {n_clauses}\n"

	# produce and append to file_content the unitary constraints
	i = 1
	for y in range(len(matrice)):
		for x in range(len(matrice)):
			# for each cell, if its defined (different from 0) we add a unitary clause 
			#notice we don't use var_from_coords() since its a linear path through the matrice
			if matrice[y][x] == 1:
				file_content = file_content + str(i) + " 0\n"
			elif matrice[y][x] == -1:
				file_content = file_content + str(-i) + " 0\n"
			i = i + 1

	size = len(matrice)

	# produce and append to file_content the no_square constraints
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


	# produce and append to file_content the connectivity constraints
	for xb in range(size):
		for xa in range(size):
			# for each cell x = (xa, xb)
			for yb in range(size):
				for ya in range(size):
					# for each cell y = (ya, yb)
					if (xa != ya) or (xb != yb):
						# if x != y
						x = var_from_coords(size, xa, xb)
						y = var_from_coords(size, ya, yb)
						C_xy = connectvar_from_vars(size, x, y)

						# both are white and need to be connected
						file_content = file_content + str(-x) + " "
						file_content = file_content + str(-y) + " "
						file_content = file_content + str(C_xy) + " 0\n"

						# both are black and need to be connected
						file_content = file_content + str(x) + " "
						file_content = file_content + str(y) + " "
						file_content = file_content + str(C_xy) + " 0\n"


	# produce and append to file_content the connectivity_conditions constraints

	# write into the given filename the produced header and constraints
	with open(input_filepath, "w") as f:
		f.write(file_content)
		f.close()


def decode_dimac(size, filepath):
	'''
	Returns a filled matrice if the dimac output is satisfiable, Nonetype if it is not
	'''
	# extract the content of the given file
	with open(filepath, "r") as f:
		content = f.readlines()
		f.close()

	satisfiability = content[0]
	if satisfiability == "SAT\n":
		result = content[1]
		result = result.split()
	
		# ...
		matrice = [[0 for j in range(size)] for i in range(size)]
		i = 0
		for y in range(size):
			for x in range(size):
				c = int(result[i])
				matrice[y][x] = c / abs(c)
				i = i + 1
	else:
		print("This board is UNSATISFIABLE")
		matrice = None

	return matrice