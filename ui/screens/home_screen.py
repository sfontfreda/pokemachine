import pygame
import sys
from core import game_scanner
from core.emulator import launch
import config


class HomeScreen: 
  def __init__(self, roms):
    self.roms = roms
    self.selected_index = 0
    self.font = pygame.font.Font(None, 32)

  def handle_events(self, events):
    for event in events:
      if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_RETURN:
          return ("detail", self.roms[self.selected_index])
        if event.key == pygame.K_ESCAPE:
          pygame.quit()
          sys.exit()
        if event.key == pygame.K_UP:
          if self.selected_index > 0: 
              self.selected_index -= 1
        if event.key == pygame.K_DOWN:
          if self.selected_index < len(self.roms) -1:
            self.selected_index += 1

  def draw(self, screen):
    for i, rom in enumerate(self.roms):
        color = config.GREEN if i == self.selected_index else config.WHITE
        text =  self.font.render(rom["name"], True, color)
        screen.blit(text, (10, 10 + i * 40))