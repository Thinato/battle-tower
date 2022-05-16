import pygame as pg
import os
from game.utils.colors import *

class Menu():
    def __init__(self, game):
        self.SELECT_SOUND = pg.mixer.Sound(os.path.join('game', 'assets', 'sfx', 'select.wav'))
        self.game = game
        self.mid_w, self.mid_h = self.game.WIDTH//2, self.game.HEIGHT//2
        self.buttons = []
        self.selected = 0

    def draw(self):
        c = 0
        for btn in self.buttons:
            btn.selected = False
            if self.selected == c:
                btn.selected = True
            btn.draw(self.game.WIN)
            c+=1

    def handle_event(self, event):
        if event.key == pg.K_RETURN:
            self.buttons[self.selected].action()
        if event.key == pg.K_BACKSPACE:
            pass
        if event.key == pg.K_DOWN:
            self.SELECT_SOUND.play()
            self.selected += 1
            if self.selected >= len(self.buttons):
                self.selected = 0
        if event.key == pg.K_UP:
            self.SELECT_SOUND.play()
            self.selected -= 1
            if self.selected <= -1:
                self.selected = len(self.buttons)-1

class MenuItem():
    def __init__(self, x: int, y: int, text: str, action, selected: bool=False):
        self.x = x
        self.y = y
        self.text = text
        self.selected = selected
        self.action = action

        self.FONT = pg.font.Font(os.path.join('game', 'assets', 'font', 'kongtext.ttf'), 20)
        self.text = self.FONT.render(text, True, WHITE)
        self.pointer = self.FONT.render('>', True, WHITE)
        self.rect = pg.Rect(x-3, y-3, self.text.get_width()+10, self.text.get_height()+5)

    def draw(self, screen):
        screen.blit(self.text, (self.x, self.y))
        if self.selected:
            screen.blit(self.pointer, (self.x-self.pointer.get_width(), self.y))
            #pg.draw.rect(screen, ORANGE, self.rect, 2)

class MenuProgressControl():
    def __init__(self, x: int, y: int, value: int=0, action=None, selected: bool=False):
        self.x = x
        self.y = y
        self.selected = selected
        self.value = value
        self.value_max = 20
        self.action = action
        self.img_back = pg.image.load(os.path.join('game', 'assets', 'img', 'progress_control.png')).convert_alpha()
        self.img_tick = pg.image.load(os.path.join('game', 'assets', 'img', 'progress_control_tick.png')).convert_alpha()

    def draw(self, screen):
        screen.blit(self.img_back, (self.x, self.y))
        for i in range(self.value):
            screen.blit(self.img_tick, (self.x+8 + 16*i, self.y+10))

    def increase_value(self) -> None:
        if value >= value_max:
            value = value_max
            return
        value += 1

    def decrease_value(self) -> None:
        if value <= 0:
            value = 0
            return
        value -= 1






class MainMenu(Menu):
    def __init__(self, game):
        Menu.__init__(self, game)
        self.options =    MenuItem(self.mid_w, self.mid_h + 55, 'Options',    self.options)
        self.start_game = MenuItem(self.mid_w, self.mid_h + 30, 'Start Game', self.start_game)
        self.credits =    MenuItem(self.mid_w, self.mid_h + 80, 'Credits',    self.credits)
        self.exit_game =  MenuItem(self.mid_w, self.mid_h +105, 'Exit',       self.exit_game)

        self.buttons = [self.start_game, self.options, self.credits, self.exit_game]

    def start_game(self):
        self.game.in_main_menu = False
        self.game.playing = True

    def options(self):
        print('options!')

    def credits(self):
        self.game.in_credits_menu = True
        self.game.in_main_menu = False

    def exit_game(self):
        self.game.running, self.game.in_main_menu = False, False
        pg.quit()



