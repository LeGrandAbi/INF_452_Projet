import pygame as pg
import misc_functions as mf

class Interface:
	def __init__(self):
		self.window = pg.display.set_mode((800,800), pg.RESIZABLE)
		self.window_active = False

		self.image = pg.Surface((1000,1000))
		self.matrice = None

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
				active = False
		return active

	def update_window(self):
		self.window.fill(0)
		window_rect = self.window.get_rect()
		fit_image = mf.fit_surf_in_rect(self.image, window_rect)
		self.window.blit(fit_image, fit_image.get_rect(center=window_rect.center))
		pg.display.flip()
		

	def update(self):
		pass


class InputInterface(Interface):
	def __init__(self):
		super().__init__()

	def update(self):
		self.image.fill((0,255,0))

	def get_matrice(self):
		return self.matrice


class OutputInterface(Interface):
	def __init__(self, matrice):
		super().__init__()
		self.matrice = matrice

	def update(self):
		self.image.fill((0,0,255))
		