from misc_functions import *
from interface import *
from dimac_coder import *

inputInterface = InputInterface()
inputInterface.run()
matrice = inputInterface.get_matrice()

execute_command("mkdir", "../dimac")
input_filepath = "../dimac/input_dimac"
output_filepath = "../dimac/output_dimac"
encode_dimac(matrice, input_filepath)

execute_command("minisat", input_filepath, output_filepath)