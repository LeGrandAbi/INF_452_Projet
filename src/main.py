import subprocess
from interface import *
from dimac_coder import *


def execute_command(*cmd):
	# execute the given command
	print("\nExecuting : " + str(cmd))
	result = subprocess.run(cmd, capture_output=True, text=True)
	# outputs the result and/or the error returned
	if result.stdout != "":
		print("Output:", result.stdout)
	if result.stderr != "":
		print("Errors:", result.stderr)


def load_matrice(filename):
	'''
	...
	'''
	with open(filename, "r") as f:
		matrice = json.load(f)
	return matrice

# ...
DIMAC_FOLDER_PATH = "dimac"
DIMAC_INPUT_FILENAME = "input_dimac"
DIMAC_OUTPUT_FILENAME = "output_dimac"
execute_command("mkdir", DIMAC_FOLDER_PATH)
execute_command("mkdir", "custom_matrices")

# ...
prompt = input("Enter board size : ")
prompt = prompt.split()
matrice = None
if prompt[0].lower() == "load":
	filename = "custom_matrices/" + prompt[1]
	matrice = load_matrice(filename)
	size = len(matrice)
else:
	size = int(prompt[0])

# ...
inputInterface = InputInterface(size, matrice)
inputInterface.run()
matrice = inputInterface.get_matrice()

# ...
input_filepath = DIMAC_FOLDER_PATH + "/" + DIMAC_INPUT_FILENAME
output_filepath = DIMAC_FOLDER_PATH + "/" + DIMAC_OUTPUT_FILENAME
encode_dimac(matrice, input_filepath)

# ...
execute_command("minisat", input_filepath, output_filepath)

# ...
result_matrice = decode_dimac(size, output_filepath)

# ...
if result_matrice != None:
	outputInterface = OutputInterface(result_matrice)
	outputInterface.run()