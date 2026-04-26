import pygame as pg
import misc_functions as mf
from settings import *
import sys

class Interface:
	def __init__(self):
		self.window = pg.display.set_mode((WINDOW_SIZE,WINDOW_SIZE))
		self.window_active = False

	def run(self):
		self.window_active = True
		while self.window_active:
			self.window_active = self.handle_events()
			self.update()
			self.update_window()

	def handle_events(self):
		active = True
		for event in pg.event.get():
			if event.type == pg.QUIT:
				sys.exit()
			elif event.type == pg.KEYDOWN:
				if event.key == pg.K_RETURN:
					active = False
		return active

	def update_window(self):
		self.window.fill(0)
		pg.display.flip()
		

	def update(self):
		pass


class InputInterface(Interface):
	def __init__(self):
		super().__init__()

	def update(self):
		pass

	def get_matrice(self):
		return None


class OutputInterface(Interface):
	def __init__(self, matrice):
		super().__init__()

	def update(self):
		pass
		