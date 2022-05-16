import pygame as pg

class Entity:
	def __init__(self, name: str='unnamed', level:int=1, main_stat: str=None, modifier: float=1):
		self.name = name
		self.level = level
		self.main_stat = main_stat
		self.modifier = modifier
		
		# Stats
		self.intellect = 5 * level * modifier # Spell Power, Mana Pool, Resistance Chance
		self.strength = 5 * level * modifier # Melee Power, Stamina, Parry Chance
		self.agility = 5 * level  * modifier # Ranged Power, Crit Strike Chance, Dodge Change

		# main_stat can be 'int', 'str' or 'agi'
		if main_stat == 'intellect':
			self.intellect *= 1.45
			self.strength *= 0.5
			self.agility *= 0.65

		elif main_stat == 'strength':
			self.intellect *= 0.45
			self.strength *= 1.4
			self.agility *= 0.75

		elif main_stat == 'agility':
			self.intellect *= 0.45
			self.strength *= 0.8
			self.agility *= 1.35
		else:
			self.intellect *= 0.6
			self.strength *= 0.6
			self.agility *= 0.6


		# Intellect Modifiers
		self.mana_max = int(100 + (self.level*50) + (self.intellect*5))
		self.mana = self.mana_max
		self.spell_power = self.intellect
		self.spell_crit_chance = self.intellect/2000 + self.agility/4000
		self.spell_crit_damage = 1
		self.resistance_chance = 0


		# Strength Modifiers
		self.stamina = self.strength # add to health
		self.health_max = int(100 + (50*level) + (self.stamina*10))
		self.health = self.health_max
		self.melee_power = self.strength # add to melee damage
		self.parry_chance = self.strength/2000 # chance to parry in percentage
		

		# Agility Modifiers
		self.ranged_power = self.agility
		self.crit_chance = self.agility/2000 # chance in percentage
		self.crit_damage = 1 # multiply this by the damage

	def __str__(self):
		return f'''
[{self.name} - {self.level} - {self.main_stat} - {self.modifier}]

Intellect: {self.intellect}
Strength:  {self.strength}
Agility:   {self.agility}
Overall:   {(self.intellect + self.strength + self.agility) / 3}

Health: {self.health}
Mana:   {self.mana}'''

		

class Player(Entity):
	def __init__(self):
		pass


if __name__ == '__main__':
	a = Entity(name='Paulo', level=25, modifier=.7,  main_stat='intellect')
	b = Entity(name='Paulo', level=25, modifier=1,   main_stat='intellect')
	c = Entity(name='Paulo', level=25, modifier=1.3, main_stat='intellect')
	d = Entity(name='Paulo', level=25, modifier=2,   main_stat='intellect')
	print(a)
	print(b)
	print(c)
	print(d)