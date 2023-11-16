import pygame
import os

WHITE = (255, 255, 255)
BLACK = (0,0,0)

WIDTH, HEIGHT = 900, 500
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Spaceships")

BORDER = pygame.Rect(WIDTH/2 - 5, 0, 10, HEIGHT)

FPS = 60
spaceship_width, spaceship_height = 55, 40

yellow_spaceship_image = pygame.image.load(os.path.join('Assets', 'spaceship_yellow.png'))
yellow_spaceship = pygame.transform.rotate(pygame.transform.scale(yellow_spaceship_image, (spaceship_width, spaceship_height)), 90)

red_spaceship_image = pygame.image.load(os.path.join('Assets', 'spaceship_red.png'))
red_spaceship = pygame.transform.rotate(pygame.transform.scale(red_spaceship_image, (spaceship_width, spaceship_height)), 270)

def draw_window(red, yellow):
    WIN.fill(WHITE)
    pygame.draw.rect(WIN, BLACK, BORDER)
    WIN.blit(yellow_spaceship, (yellow.x, yellow.y))
    WIN.blit(red_spaceship, (red.x, red.y))
    pygame.display.update()

def yellow_handle_movement(keys_pressed, yellow):
    if keys_pressed[pygame.K_a] and yellow.x-5 > 0: #LEFT
        yellow.x-=5
    if keys_pressed[pygame.K_w] and yellow.y-5 > 0: #UP
        yellow.y -= 5
    if keys_pressed[pygame.K_d] and yellow.x+5+yellow.width < BORDER.x: #right
        yellow.x +=5
    if keys_pressed[pygame.K_s] and yellow.y+5+yellow.height < BORDER.height: #down
        yellow.y += 5

def red_handle_movement(keys_pressed, red):
    if keys_pressed[pygame.K_LEFT] and red.x-5 > BORDER.x: #LEFT
        red.x-=5
    if keys_pressed[pygame.K_UP] and red.y-5 > 0: #UP
        red.y -= 5
    if keys_pressed[pygame.K_RIGHT] and red.x+5+red.width < WIDTH: #right
        red.x +=5
    if keys_pressed[pygame.K_DOWN] and red.y+5+red.height < BORDER.height: #down
        red.y += 5

def main():
    red = pygame.Rect(700, 300, spaceship_width, spaceship_height)
    yellow = pygame.Rect(100, 300, spaceship_width, spaceship_height)
    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        keys_pressed = pygame.key.get_pressed()
        yellow_handle_movement(keys_pressed, yellow)
        red_handle_movement(keys_pressed, red)
        draw_window(red, yellow)
    pygame.quit()

if __name__ == "__main__":
    main()
