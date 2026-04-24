import subprocess

from misc_functions import *
from interface import *
from dimac_coder import *

inputInterface = InputInterface()
inputInterface.run()
matrice = inputInterface.get_matrice()

input_filepath = "../dimac/input_dimac"
output_filepath = "../dimac/output_dimac"
encode_dimac(matrice, input_filepath)

#result = subprocess.run(["minisat", input_filepath, output_filepath], capture_output=True, text=True)
#print("Exit Code:", result.returncode)
#print("Output:", result.stdout)
#print("Errors:", result.stderr)