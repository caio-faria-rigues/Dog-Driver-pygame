import pygame
import sys


def main():
    pygame.init()

    screen = pygame.display.set_mode((720, 1280))

    x, y = screen.get_size()

    background = pygame.image.load(r"assets/asfalto.png")
    scenario = pygame.image.load(r"assets/fundo_andante2parado.png")

    scenario_y_pos = -1000
    scenario_fall = 16

    while True:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        scenario_y_pos += scenario_fall if scenario_y_pos <= 0 else -1200

        screen.blit(background, (0, 0))
        screen.blit(scenario, (0, scenario_y_pos))
        pygame.display.update()


main()
