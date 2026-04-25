import pygame as pg
import subprocess

def fit_surf_in_rect(surf, rect):
	surf_rect = surf.get_rect()
	fitted_rect = surf_rect.fit(rect)
	fitted_surf = pg.transform.scale(surf, (fitted_rect.width, fitted_rect.height))
	return fitted_surf

def execute_command(*cmd):
	print("\nExecuting : " + str(cmd))
	result = subprocess.run(cmd, capture_output=True, text=True)
	print("Exit Code:", result.returncode)
	print("Output:", result.stdout)
	print("Errors:", result.stderr)