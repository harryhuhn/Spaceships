import pygame
import os
pygame.font.init()

WHITE = (255, 255, 255)
BLACK = (0,0,0)
RED = (255,0,0)
YELLOW=(0,0,255)

WIDTH, HEIGHT = 900, 500
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Spaceships")

BORDER = pygame.Rect(WIDTH//2 - 5, 0, 10, HEIGHT)

HEALTH_FONT = pygame.font.SysFont('comicsans', 40)
WINNER_FONT = pygame.font.SysFont('comicsans', 100)
SPACE = pygame.transform.scale(pygame.image.load(os.path.join('Assets', 'space.png')), (WIDTH, HEIGHT))
FPS = 60

BULLET_VEL = 15
MAX_BULLETS = 3
spaceship_width, spaceship_height = 55, 40

YELLOW_HIT = pygame.USEREVENT + 1
RED_HIT = pygame.USEREVENT + 2

red_health=10
yellow_health=10

yellow_spaceship_image = pygame.image.load(os.path.join('Assets', 'spaceship_yellow.png'))
yellow_spaceship = pygame.transform.rotate(pygame.transform.scale(yellow_spaceship_image, (spaceship_width, spaceship_height)), 90)

red_spaceship_image = pygame.image.load(os.path.join('Assets', 'spaceship_red.png'))
red_spaceship = pygame.transform.rotate(pygame.transform.scale(red_spaceship_image, (spaceship_width, spaceship_height)), 270)

def draw_window(red, yellow, red_bullets, yellow_bullets, red_health, yellow_health):
    WIN.blit(SPACE, (0,0))
    pygame.draw.rect(WIN, BLACK, BORDER)
    red_health_text = HEALTH_FONT.render("Health: " + str(red_health), 1, WHITE)
    yellow_health_text = HEALTH_FONT.render("Health: " + str(yellow_health), 1, WHITE)
    WIN.blit(yellow_spaceship, (yellow.x, yellow.y))
    WIN.blit(red_spaceship, (red.x, red.y))
    WIN.blit(red_health_text, (WIDTH - red_health_text.get_width() - 10, 10))
    WIN.blit(yellow_health_text, (10,10))
    for bullet in red_bullets:
        pygame.draw.rect(WIN, RED, bullet)
    for bullet in yellow_bullets:
        pygame.draw.rect(WIN, YELLOW, bullet)
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

def handle_bullets(yellow_bullets, red_bullets, yellow, red):
    for bullet in yellow_bullets:
        bullet.x += BULLET_VEL
        if red.colliderect(bullet):
            pygame.event.post(pygame.event.Event(RED_HIT))
            yellow_bullets.remove(bullet)
        if bullet.x > WIDTH:
            yellow_bullets.remove(bullet)
    for bullet in red_bullets:
        bullet.x -= BULLET_VEL
        if yellow.colliderect(bullet):
            pygame.event.post(pygame.event.Event(YELLOW_HIT))
            red_bullets.remove(bullet)
        if bullet.x < 0:
            red_bullets.remove(bullet)

def draw_winner(text):
    draw_text = WINNER_FONT.render(text, 1, WHITE)
    WIN.blit(draw_text, (WIDTH/2 - draw_text.get_width()/2, HEIGHT/2 - draw_text.get_height()/2))
    pygame.display.update()
    pygame.time.delay(5000)

def main():
    red_health=10
    yellow_health=10
    red = pygame.Rect(700, 300, spaceship_width, spaceship_height)
    yellow = pygame.Rect(100, 300, spaceship_width, spaceship_height)
    red_bullets=[]
    yellow_bullets=[]
    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LCTRL and len(yellow_bullets)<MAX_BULLETS:
                    bullet = pygame.Rect(yellow.x + yellow.width, yellow.y + yellow.height//2 - 2, 10, 5)
                    yellow_bullets.append(bullet)
                if event.key == pygame.K_RCTRL and len(red_bullets)<MAX_BULLETS:
                    bullet = pygame.Rect(red.x, red.y + red.height//2 - 2, 10, 5)
                    red_bullets.append(bullet)
            if event.type==RED_HIT:
                red_health-=1
            if event.type==YELLOW_HIT:
                yellow_health-=1
        winner_text=""
        if red_health<=0:
            winner_text="Yellow wins"
        if yellow_health<=0:
            winner_text="Red wins"
        if winner_text != "":
            draw_winner(winner_text)
            break
        keys_pressed = pygame.key.get_pressed()
        yellow_handle_movement(keys_pressed, yellow)
        red_handle_movement(keys_pressed, red)
        handle_bullets(yellow_bullets, red_bullets, yellow, red)
        draw_window(red, yellow, red_bullets, yellow_bullets, red_health, yellow_health)
    main()

if __name__ == "__main__":
    main()
