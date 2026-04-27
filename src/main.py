import subprocess
from interface import *
from dimac_coder import *

DIMAC_FOLDER_PATH = "dimac"
DIMAC_INPUT_FILENAME = "input_dimac"
DIMAC_OUTPUT_FILENAME = "output_dimac"

def execute_command(*cmd):
	print("\nExecuting : " + str(cmd))
	result = subprocess.run(cmd, capture_output=True, text=True)
	print("Exit Code:", result.returncode)
	print("Output:", result.stdout)
	print("Errors:", result.stderr)

#size = int(input("Enter board size : "))
size = 9

inputInterface = InputInterface(size)
inputInterface.run()
matrice = inputInterface.get_matrice()

execute_command("mkdir", DIMAC_FOLDER_PATH)
input_filepath = DIMAC_FOLDER_PATH + "/" + DIMAC_INPUT_FILENAME
output_filepath = DIMAC_FOLDER_PATH + "/" + DIMAC_OUTPUT_FILENAME
encode_dimac(matrice, input_filepath)

execute_command("minisat", input_filepath, output_filepath)
execute_command("cat", output_filepath)

result_matrice = decode_dimac(size, output_filepath)

outputInterface = OutputInterface(result_matrice)
outputInterface.run()