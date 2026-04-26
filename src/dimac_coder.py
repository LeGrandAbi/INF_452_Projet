import sys

def encode_dimac(matrice, input_filepath):
clauses = []
var_map = {}
n = len(matrice)
var_id = 1
    for i in range(n):
        for j in range(n):
            var_map[(i, j)] = var_id
            var_id += 1
for i in range(n):
        for j in range(n):
            if matrice[i][j] == 1:  # white
                clauses.append([var_map[(i, j)]])
            elif matrice[i][j] == -1:  # black
                clauses.append([-var_map[(i, j)]])
	num_vars = n * n
    num_clauses = len(clauses)

	with open(input_filepath, "w") as f:
		f.write("p cnf 6 3\n")
		f.write("1 -5 6 4 0\n")
		f.write("-1 5 3 4 0\n")
		f.write("-3 -4 0\n")

def decode_dimac(filepath):
	'''
	needs to be filled
	'''
	matrice = [[]]
	return matrice
