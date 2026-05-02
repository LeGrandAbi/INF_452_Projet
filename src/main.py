import subprocess
from interface import *
from dimac_coder import *


def execute_command(*cmd):
	'''
	...
	'''
	# execute the given command
	print("\nExecuting : " + str(cmd))
	result = subprocess.run(cmd, capture_output=True, text=True)
	# outputs the result and/or the error returned
	print("Exit Code:", result.returncode)
	print("Output:", result.stdout)
	print("Errors:", result.stderr)


# ...
DIMAC_FOLDER_PATH = "dimac"
DIMAC_INPUT_FILENAME = "input_dimac"
DIMAC_OUTPUT_FILENAME = "output_dimac"

# ...
size = int(input("Enter board size : "))

# ...
inputInterface = InputInterface(size)
inputInterface.run()
matrice = inputInterface.get_matrice()

# ...
execute_command("mkdir", DIMAC_FOLDER_PATH)
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