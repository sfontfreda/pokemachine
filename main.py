import pygame
import config
from ui.screens.game_detail import GameDetailScreen
from ui.screens.home_screen import HomeScreen
from core import game_scanner

def main():
  pygame.init()
  screen = pygame.display.set_mode((config.WIDTH, config.HEIGHT), pygame.FULLSCREEN)
  pygame.display.set_caption("pokemachine")
  clock = pygame.time.Clock()
  roms = game_scanner.get_roms()
  home = HomeScreen(roms)
  current_screen = home

  while True:
    events = pygame.event.get()
    action = current_screen.handle_events(events)
    
    if action and action[0] == "detail":
      current_screen = GameDetailScreen(action[1])
    if action == "back":
      current_screen = home
    
    screen.fill(config.BLACK)
    current_screen.draw(screen)
    pygame.display.flip()
    clock.tick(config.FPS)

if __name__ == "__main__":
  main()