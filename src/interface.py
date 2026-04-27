import pygame as pg
import misc_functions as mf
from settings import *
import sys


class InputInterface():
	def __init__(self, size):
		self.window = pg.display.set_mode((WINDOW_SIZE,WINDOW_SIZE))
		self.window_rect = self.window.get_rect()
		self.window_active = False
		self.size = size
		self.matrice = [[0 for j in range(size)] for i in range(size)]

	def handle_events(self):
		active = True
		for event in pg.event.get():
			if event.type == pg.QUIT:
				sys.exit()
			elif event.type == pg.KEYDOWN:
				if event.key == pg.K_RETURN:
					active = False
			elif event.type == pg.MOUSEBUTTONDOWN:
				self.switch_cell(event.pos)
		return active

	def update_window(self):
		self.window.fill("gray")
		self.draw_board()
		pg.display.flip()

	def get_matrice(self):
		return self.matrice

	def draw_board(self):
		mf.draw_grid(self.window, self.size)
		for y in range(self.size):
			for x in range(self.size):
				circle_x = x*self.window_rect.width/self.size + (self.window_rect.width/self.size/2)
				circle_y = y*self.window_rect.height/self.size + (self.window_rect.height/self.size/2)
				circle_r = self.window_rect.width/self.size/2
				if self.matrice[y][x] == 1:
					pg.draw.circle(self.window, "white", (circle_x, circle_y), circle_r)
				elif self.matrice[y][x] == -1:
					pg.draw.circle(self.window, "black", (circle_x, circle_y), circle_r)

	def switch_cell(self, pos):
		x, y = pos
		x = int(self.size * x / self.window_rect.width)
		y = int(self.size * y / self.window_rect.height)
		self.matrice[y][x] += 1
		if self.matrice[y][x] > 1:
			self.matrice[y][x] = -1

	def run(self):
		self.window_active = True
		while self.window_active:
			self.window_active = self.handle_events()
			self.update_window()


class OutputInterface():
	def __init__(self, matrice):
		self.window = pg.display.set_mode((WINDOW_SIZE,WINDOW_SIZE))
		self.window_rect = self.window.get_rect()
		self.window_active = False

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

	def run(self):
		self.window_active = True
		while self.window_active:
			self.window_active = self.handle_events()
			self.update_window()