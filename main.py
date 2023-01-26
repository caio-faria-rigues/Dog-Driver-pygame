import pygame
import sys
from random import randint
import csv
import unidecode


alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u",
            "v", "w", "x", "y", "z"]


def hangman():
    """
    return random words from words.csv, with a version that hasn't accents; both in a list.
    """
    with open("words.csv", "r", encoding="utf-8") as words:
        reader = csv.reader(words)

        num = randint(1, 52)
        for row in reader:
            word_original = row[num]
            word_no_accent = unidecode.unidecode(word_original)

    return [word_original, word_no_accent]


def falling_letters():
    """
    return a dict with 5 random letters and their respective X-axis position on screen.
    """
    global alphabet
    letter_list = []
    for n in range(5):
        letter_list.append(alphabet[randint(0, 24)])

    letter_objects = {letter_list[0]: randint(50, 640), letter_list[1]: randint(50, 640),
                      letter_list[2]: randint(50, 640), letter_list[3]: randint(50, 640),
                      letter_list[4]: randint(50, 640)}
    return letter_objects


def main():
    global alphabet

    pygame.init()

    screen = pygame.display.set_mode((720, 1280))
    timer = pygame.time.Clock()

    timer.tick(60)

    x, y = screen.get_size()

    background = pygame.image.load(r"assets/asfalto.png")
    scenario = pygame.image.load(r"assets/fundo_andante2parado.png")

    taxi = pygame.image.load(r"assets/dog driver 1-1.png.png")
    taxi_hitbox = taxi.get_rect()

    font = pygame.font.Font("Retro Gaming.ttf", 64)

    scenario_y_pos = -1000
    scenario_fall = 16

    letter_y_pos = 800
    letter_fall = 26

    while True:

        # quit the game
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()

        scenario_y_pos += scenario_fall if scenario_y_pos <= 0 else -1200
        # letter_y_pos += letter_fall

        letter = alphabet[randint(0, 25)]
        letter = font.render(letter, True, "white")

        mouse_x, mouse_y = pygame.mouse.get_pos()

        taxi_x, taxy_y = mouse_x, mouse_y

        screen.blit(background, (0, 0))
        screen.blit(scenario, (0, scenario_y_pos))
        screen.blit(taxi, (taxi_x, taxy_y))
        screen.blit(letter, (randint(50, 670), letter_y_pos))

        pygame.display.update()


hangman()
falling_letters()
main()
