import pygame
import config
from core.emulator import launch

class GameDetailScreen:
  def __init__(self, rom):
    self.rom = rom
    self.font = pygame.font.Font(None, 32)
  
  def handle_events(self, events):
      for event in events:
        if event.type == pygame.KEYDOWN:
          if event.key == pygame.K_RETURN:
            launch(self.rom)
          if event.key == pygame.K_ESCAPE:
            return "back"
      return None


  def draw(self, screen):
    text =  self.font.render(self.rom["name"], True, config.WHITE)
    screen.blit(text, (10, 10))