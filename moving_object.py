import pygame
import random

pygame.init()

WIDTH, HEIGHT = 800, 800
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
VEL = 8
pygame.display.set_caption("Moving")


def render_surface(rectangle, color): 
    WIN.fill((255, 255, 255))
    pygame.draw.rect(WIN, color, rectangle)
    pygame.display.flip()


def main(): 
    running = True
    clock = pygame.time.Clock()
    x, y = 0, 0
    border_collision = False

    while running: 
        clock.tick(60)
        for event in pygame.event.get(): 
            if event.type == pygame.QUIT: 
                running = False
        
        key_pressed = pygame.key.get_pressed()
        if key_pressed[pygame.K_UP] and y > 0: 
            y -= VEL
        elif key_pressed[pygame.K_DOWN] and y < HEIGHT - 150: 
            y += VEL 
        elif key_pressed[pygame.K_LEFT] and x > 0: 
            x -= VEL
        elif key_pressed[pygame.K_RIGHT] and x < WIDTH - 150: 
            x += VEL 

        # Check if rectangle hits the border
        if x <= 0 or x + 150 >= WIDTH or y <= 0 or y + 150 >= HEIGHT:
            if not border_collision: 
                # Update the color to a new random color
                color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
                border_collision = True
        else: 
            if border_collision: 
                color = (0, 0, 0)
                border_collision = False
        
        rectangle = pygame.Rect(x, y, 150, 150)
        render_surface(rectangle, color)



if __name__ == "__main__": 
    main()

pygame.quit()