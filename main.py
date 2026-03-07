import pygame
import sys
import config
from core import game_scanner

def main():
    roms = game_scanner.get_roms()
    print(roms)
    pygame.init()
    
    screen = pygame.display.set_mode((config.WIDTH, config.HEIGHT))
    pygame.display.set_caption("pokemachine")
    clock = pygame.time.Clock()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()

        screen.fill(config.BLACK)

        font = pygame.font.Font(None, 32)
        text = font.render("gamename", True, (255, 255, 255))
        screen.blit(text, (10,10))
        pygame.display.flip()
        clock.tick(config.FPS)

if __name__ == "__main__":
    main()