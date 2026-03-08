import pygame
import sys
import config
from core import game_scanner
from core.emulator import launch

def main():
    roms = game_scanner.get_roms()
    print(roms)
    pygame.init()
    
    screen = pygame.display.set_mode((config.WIDTH, config.HEIGHT))
    pygame.display.set_caption("pokemachine")
    clock = pygame.time.Clock()
    selected_index = 0

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    launch(roms[selected_index])
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()
                if event.key == pygame.K_UP:
                    if selected_index > 0: 
                        selected_index -= 1
                if event.key == pygame.K_DOWN:
                    if selected_index < len(roms) -1:
                        selected_index += 1

        screen.fill(config.BLACK)

        font = pygame.font.Font(None, 32)
       
        
        for i, rom in enumerate(roms):
            color = config.GREEN if i == selected_index else config.WHITE
            text = font.render(rom["name"], True, color)
            screen.blit(text, (10, 10 + i * 40))

        pygame.display.flip()
        clock.tick(config.FPS)

if __name__ == "__main__":
    main()