import pygame
import random

pygame.init()

# game constants
WIDTH, HEIGHT = 800, 800
BLACK = (0, 0, 0)
YELLOW = (255, 255, 0)
RED = (255, 0, 0)
FPS = 60
VEL = 5
RECT_WIDTH, RECT_HEIGHT = 50, 50

WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Collision Test")

red = pygame.Rect(0, 0, RECT_WIDTH//2, RECT_HEIGHT//2)

player = pygame.Rect(WIDTH - RECT_WIDTH, 0, RECT_WIDTH, RECT_HEIGHT)



def render(red, player): 
    WIN.fill(BLACK)
    pygame.draw.rect(WIN, RED, red)
    pygame.draw.rect(WIN, YELLOW, player)
    pygame.display.flip()


def main(): 
    running = True

    clock = pygame.time.Clock()
    while running: 
        for event in pygame.event.get(): 
            if event.type == pygame.QUIT: 
                print("X")
                running = False

        clock.tick(FPS)
        key_pressed = pygame.key.get_pressed()
        if key_pressed[pygame.K_UP] and player.y > 0: 
            player.y -= VEL
        elif key_pressed[pygame.K_DOWN] and player.y < HEIGHT - player.height: 
            player.y += VEL
        elif key_pressed[pygame.K_LEFT] and player.x > 0: 
            player.x -= VEL
        elif key_pressed[pygame.K_RIGHT] and player.x < WIDTH - player.width: 
            player.x += VEL

        if player.colliderect(red): 
            red.x = random.randint(0, WIDTH - player.width)
            red.y = random.randint(0, HEIGHT - player.height)
        
        render(red, player)

if __name__ == "__main__": 
    main()

pygame.quit()