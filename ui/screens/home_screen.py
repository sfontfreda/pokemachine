import pygame
import config
from pathlib import Path
import math

class HomeScreen:
  def __init__(self, roms):
    self.roms = roms
    self.selected_index = 0
    self.font = pygame.font.Font(None, 24)
    
    total = len(self.roms)
    self.top_count = math.ceil(total / 2)
    self.bottom_count = math.floor(total / 2)
    
    self.margin = 20
    biggest_row = self.top_count
    max_width = (config.WIDTH - (biggest_row + 1) * self.margin) // biggest_row
    max_height = (config.HEIGHT - self.margin * 3) // 2

    self.card_size = min(max_width, max_height)

  def handle_events(self, events):
    for event in events:
      if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_RETURN:
          return ("detail", self.roms[self.selected_index])
        if event.key == pygame.K_ESCAPE:
          pygame.quit()
          import sys
          sys.exit()
        if event.key == pygame.K_LEFT:
          if self.selected_index > 0:
            self.selected_index -= 1
        if event.key == pygame.K_RIGHT:
          if self.selected_index < len(self.roms) - 1:
            self.selected_index += 1
    return None

  def draw(self, screen):
    rows = [
      self.roms[:self.top_count],
      self.roms[self.top_count:]
    ]

    for row_index, row in enumerate(rows):
      num_cards = len(row)
      total_width = num_cards * self.card_size + (num_cards - 1) * self.margin
      start_x = (config.WIDTH - total_width) // 2
      y = self.margin + row_index * (self.card_size + self.margin)

      for col_index, rom in enumerate(row):
        i = row_index * self.top_count + col_index
        x = start_x + col_index * (self.card_size + self.margin)

        cover_path = Path("assets/covers") / f"{rom['name']}.png"
        
        if cover_path.exists():
          image = pygame.image.load(str(cover_path))
          image = pygame.transform.scale(image, (self.card_size, self.card_size))
          screen.blit(image, (x, y))
        else:
          color = config.PALETTE[i % len(config.PALETTE)]
          pygame.draw.rect(screen, color, (x, y, self.card_size, self.card_size))

        if i == self.selected_index:
          pygame.draw.rect(screen, config.WHITE, (x, y, self.card_size, self.card_size), 4)

        overlay = pygame.Surface((self.card_size, 60), pygame.SRCALPHA)
        overlay.fill((0, 0, 0, 160))
        screen.blit(overlay, (x, y + self.card_size - 60))
        
        name_text = rom["name"][:40] + "..." if len(rom["name"]) > 30 else rom["name"]
        name = self.font.render(name_text, True, config.WHITE)
        screen.blit(name, (x + 8, y + self.card_size - 30))
        