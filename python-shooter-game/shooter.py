import pygame
import os # taking the help of OS to define the paths to game assets 

# game constants
WIDTH, HEIGHT = 1000, 1000
FPS = 60
SPACESHIP_WIDTH, SPACESHIP_HEIGHT = 55, 40

YELLOW_SPACESHIP_IMAGE = pygame.image.load(os.path.join("python-shooter-game", "Assets", "spaceship_yellow.png"))
YELLOW_SPACESHIP = pygame.transform.rotate(pygame.transform.scale(YELLOW_SPACESHIP_IMAGE, (SPACESHIP_WIDTH, SPACESHIP_HEIGHT)), 90)
RED_SPACESHIP_IMAGE = pygame.image.load(os.path.join("python-shooter-game", "Assets", "spaceship_red.png"))
RED_SPACESHIP = pygame.transform.rotate(pygame.transform.scale(RED_SPACESHIP_IMAGE, (SPACESHIP_WIDTH, SPACESHIP_HEIGHT)), 270)

# creating screen
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Space Shooter")


def draw_window(red, yellow): 
    WIN.fill((255, 245, 255))
    ## use blit() for drawing surfaces (ex: text, images) onto screen
    WIN.blit(YELLOW_SPACESHIP, (yellow.x, yellow.y)) 
    WIN.blit(RED_SPACESHIP, (red.x, red.y))
    pygame.display.update() ### renders the screen components (surface)

# main game 
def main(): 

    ## co-ordinates of yellow and red Rect will be assigned to the co-ordinates of YELLOW and RED_SPACESHIP
    ## by modifying the co-ordinates of the rectangle, the spaceships move accordingly 
    yellow = pygame.Rect(100, 300, SPACESHIP_WIDTH, SPACESHIP_HEIGHT)
    red = pygame.Rect(700, 300, SPACESHIP_WIDTH, SPACESHIP_HEIGHT)

    clock = pygame.time.Clock()
    running = True

    # main game loop
    while running: 
        clock.tick(FPS) ### while loop never runs over 60/second 

        # handle event
        for events in pygame.event.get(): ### returns a list 
            if events.type == pygame.QUIT: 
                running = False

        red.x -= 1
        draw_window(red, yellow)

# call the main game function
if __name__ == "__main__": 
    main()


pygame.quit()

