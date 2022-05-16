import pygame as pg
from game.utils.colors import *
from game.menu import *
from game.battle_tower import *
import os

class Game():
	def __init__(self):
		pg.init()
		pg.mixer.init()
		self.FONT_TITLE = pg.font.Font(os.path.join('game', 'assets', 'font', 'WayfarersToyBox.ttf'), 76)
		self.FONT = pg.font.Font(os.path.join('game', 'assets', 'font', 'kongtext.ttf'), 20)
		self.WIDTH, self.HEIGHT = 800, 600
		self.WIN = pg.display.set_mode((self.WIDTH, self.HEIGHT))
		self.display = pg.Surface((self.WIDTH, self.HEIGHT))
		self.CLOCK = pg.time.Clock()
		self.FPS = 30

		self.selected_btn = 0

		self.running = True
		self.in_main_menu = True
		self.in_options_menu = False
		self.in_credits_menu = False
		self.playing = False

		self.main_menu = MainMenu(self)

	def draw_main_menu(self):
		self.WIN.fill(BLACK)
		self.main_menu.draw()
		title = [self.FONT_TITLE.render('Battle', True, WHITE), self.FONT_TITLE.render('Tower', True, WHITE)]
		self.WIN.blit(title[0], (self.WIDTH//2 - title[0].get_width()//2,70))
		self.WIN.blit(title[1], (self.WIDTH//2 - title[1].get_width()//2,70+title[0].get_height()))


		pg.display.flip()

	def draw_credits_menu(self):
		self.WIN.fill(BLACK)
		title = self.FONT_TITLE.render('Credits', True, WHITE)
		self.WIN.blit(title, (self.WIDTH//2 - title.get_width()//2,70))
		credits = [self.FONT.render('Created by Thinato', True, WHITE), self.FONT.render('@paulo.lisecki', True, WHITE)]
		self.WIN.blit(credits[0], (self.WIDTH//2 - credits[0].get_width()//2,self.HEIGHT//2))
		self.WIN.blit(credits[1], (self.WIDTH//2 - credits[1].get_width()//2,self.HEIGHT//2+credits[0].get_height()))

		footer = self.FONT.render('Press \'backspace\' to go back', True, WHITE)
		self.WIN.blit(footer, (self.WIDTH//2 - footer.get_width()//2,self.HEIGHT - footer.get_height()))

		pg.display.flip()

	def draw_options_menu(self):
		self.WIN.fill(BLACK)
		title = self.FONT_TITLE.render('Options', True, WHITE)
		self.WIN.blit(title, (self.WIDTH//2 - title.get_width()//2,70))



		pg.display.flip()

	def draw(self):
		self.WIN.fill(BLACK)
		pg.display.flip()

	def draw_text(self, text, x, y ):
		text_surface = self.FONT.render(text, True, WHITE)
		text_rect = text_surface.get_rect()
		text_rect.center = (x, y)
		self.display.blit(text_surface,text_rect)


	def check_events(self, event):
		if event.type == pg.QUIT:
			self.running = False
			self.in_main_menu = False
			self.in_options_menu = False
			self.in_credits_menu = False
			self.playing = False
		if event.type == pg.KEYDOWN:
			self.main_menu.handle_event(event)
			if event.key == pg.K_BACKSPACE:
				if self.in_credits_menu or self.in_options_menu:
					self.in_credits_menu, self.in_options_menu = False, False
					self.in_main_menu = True
				
				
			



	def start(self) -> None:

		while self.running:
			while self.in_main_menu:
				self.CLOCK.tick(self.FPS)
				self.draw_main_menu()
				for event in pg.event.get():
						self.check_events(event)

			while self.in_options_menu:
				pass

			while self.in_credits_menu:
				self.CLOCK.tick(20)
				self.draw_credits_menu()
				for event in pg.event.get():
						self.check_events(event)

			while self.playing:
				self.CLOCK.tick(20)
				bt = BattleTower(self)
				bt.start()

		pg.quit()


