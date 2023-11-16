import pygame
import os

WHITE = (255, 255, 255)

WIDTH, HEIGHT = 900, 500
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Spaceships")

FPS = 60
spaceship_width, spaceship_height = 55, 40

yellow_spaceship_image = pygame.image.load(os.path.join('Assets', 'spaceship_yellow.png'))
yellow_spaceship = pygame.transform.rotate(pygame.transform.scale(yellow_spaceship_image, (spaceship_width, spaceship_height)), 90)

red_spaceship_image = pygame.image.load(os.path.join('Assets', 'spaceship_red.png'))
red_spaceship = pygame.transform.scale(red_spaceship_image, (spaceship_width, spaceship_height))

def draw_window():
    WIN.fill(WHITE)
    WIN.blit(yellow_spaceship, (300, 100))
    pygame.display.update()

def main():
    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        draw_window()
    pygame.quit()

if __name__ == "__main__":
    main()
