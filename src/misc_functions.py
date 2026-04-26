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

def draw_grid(surf, size):
	surf_rect = surf.get_rect()
	for i in range(size):
		y = i*surf_rect.height/size
		pg.draw.line(surf, "black", (0, y), (surf_rect.right, y))
		x = i*surf_rect.width/size
		pg.draw.line(surf, "black", (x, 0), (x, surf_rect.bottom))