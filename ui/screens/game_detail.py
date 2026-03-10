import pygame
import config
from core.emulator import launch
from core.save_manager import save, load
class GameDetailScreen:
  def __init__(self, rom):
    self.rom = rom
    self.font = pygame.font.Font(None, 32)
    self.selected = 0
    self.options = ["LAUNCH", "BACK", "SAVE", "LOAD"]

  def handle_events(self, events):
      for event in events:
        if event.type == pygame.KEYDOWN:
          if event.key == pygame.K_RETURN:
            if self.options[self.selected] == "LAUNCH":
              launch(self.rom)
            elif self.options[self.selected] == "BACK":
              return "back"
            elif self.options[self.selected] == "SAVE":
              save(self.rom)
            elif self.options[self.selected] == "LOAD":
              load(self.rom)
          if event.key == pygame.K_ESCAPE:
            return "back"
          if event.key == pygame.K_UP:
            if self.selected > 0:
                self.selected -= 1
          if event.key == pygame.K_DOWN:
              if self.selected < len(self.options) - 1:
                  self.selected += 1
      return None


  def draw(self, screen):
      title = self.font.render(self.rom["name"], True, config.WHITE)
      screen.blit(title, (10, 10))

      for i, option in enumerate(self.options):
          color = config.GREEN if i == self.selected else config.WHITE
          text = self.font.render(option, True, color)
          screen.blit(text, (10, 50 + i * 40))