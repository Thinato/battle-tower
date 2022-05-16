import pygame as pg
from game.utils.colors import *

class BattleTower:
	def __init__(self, game):
		self.game = game


		self.running = True
		self.selecting_character = True



	def draw(self, screen):
		screen.fill(RED)
		pg.display.flip()

	def handle_event(self, event):
		if event.type == pg.QUIT:
			self.running = False
			self.game.running = False
			self.game.playing = False

	def start(self):
		while self.running:
			while self.selecting_character:
				c = CharacterSelection(self.game)
				c.start()
			self.game.CLOCK.tick(self.game.FPS)
			self.draw(self.game.WIN)
			for event in pg.event.get():
				self.handle_event(event)

class CharacterSelection:
	def __init__(self, game):
		self.game = game
		self.selecting = True

		self.ui_rects = [pg.Rect(5,5, game.WIDTH//3, game.HEIGHT-5)]

	def draw(self, screen):
		for rect in self.ui_rects:
			pg.draw.rect(screen, WHITE, rect)

		pg.display.flip()
		pass

	def handle_event(self, event):
		if event.type == pg.QUIT:
			self.running = False
			self.game.running = False
			self.game.playing = False
			
	def start(self):
		while self.selecting:
			self.draw(self.game.WIN)
			for event in pg.event.get():
				self.handle_event(event)
		pass
