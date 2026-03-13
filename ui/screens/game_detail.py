import pygame
import config
from core.emulator import launch
from core.save_manager import save, load
from pathlib import Path

class GameDetailScreen:
  def __init__(self, rom, rom_index=0):
    self.rom = rom
    self.rom_index = rom_index
    self.font_title = pygame.font.Font(None, 48)
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
      cover_path = Path("assets/covers") / f"{self.rom['name']}.jpg"
      cover_size = 300

      if cover_path.exists():
        image = pygame.image.load(str(cover_path))
        image = pygame.transform.scale(image, (cover_size, cover_size))
        screen.blit(image, (40, 40))
      else:
        color = config.PALETTE[self.rom_index % len(config.PALETTE)]
        pygame.draw.rect(screen, color, (40, 40, cover_size, cover_size))

      title = self.font_title.render(self.rom["name"], True, config.WHITE)
      system = self.font.render(self.rom["system"].upper(), True, config.GRAY)
      screen.blit(title, (380, 40))
      screen.blit(system, (380, 100))

      for i, option in enumerate(self.options):
        color = config.GREEN if i == self.selected else config.WHITE
        text = self.font.render(option, True, color)
        screen.blit(text, (380, 160 + i * 50))