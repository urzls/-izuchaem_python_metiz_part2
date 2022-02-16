import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
	"""Один инопланетный класс"""
	def __init__(self,ai_settings,screen):
		"""Начальная позиция пришельца"""
		super(Alien,self).__init__()
		self.screen = screen
		self.ai_settings = ai_settings
		
		# Загрузить инопланетное изображение и установить атрибут rect
		self.image = pygame.image.load('images/alien.bmp')
		self.rect = self.image.get_rect()
		
		# Каждый пришелец изначально находится в левом верхнем углу
		self.rect.x = self.rect.width
		self.rect.y = self.rect.height
		
		# Сохранить точное местоположение инопланетян
		self.x = float(self.rect.x)
	
	def blitme(self):
		"""Рисование инопланетян на указанных позициях"""
		self.screen.blit(self.image,self.rect)
	
	def check_edges(self):
		"""Обнаруживает, что инопланетянин находится на краю экрана, и возвращает True"""
		screen_rect = self.screen.get_rect()
		if self.rect.right >= screen_rect.right:
			return True
		elif self.rect.left <= 0:
			return True
	
	def update(self):
		"""Переместить инопланетян вправо"""
		self.x += (self.ai_settings.alien_speed_factor * self.ai_settings.fleet_direction)
		self.rect.x = self.x


