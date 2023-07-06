import pygame
import os # taking the help of OS to define the paths to game assets 

# game constants
WIDTH, HEIGHT = 1000, 700
FPS = 60
VEL = 5 ### velocity
WHITE = ((255, 255, 255))
BLACK = ((0, 0, 0))
SPACESHIP_WIDTH, SPACESHIP_HEIGHT = 55, 40
SCREEN_SEPARATOR = pygame.Rect(WIDTH//2 - 5, 0, 10, HEIGHT)

YELLOW_SPACESHIP_IMAGE = pygame.image.load(os.path.join("python-shooter-game", "Assets", "spaceship_yellow.png"))
YELLOW_SPACESHIP = pygame.transform.rotate(pygame.transform.scale(YELLOW_SPACESHIP_IMAGE, (SPACESHIP_WIDTH, SPACESHIP_HEIGHT)), 90)
RED_SPACESHIP_IMAGE = pygame.image.load(os.path.join("python-shooter-game", "Assets", "spaceship_red.png"))
RED_SPACESHIP = pygame.transform.rotate(pygame.transform.scale(RED_SPACESHIP_IMAGE, (SPACESHIP_WIDTH, SPACESHIP_HEIGHT)), 270)

# creating screen
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Space Shooter")

def yellow_handle_movement(keys_pressed, yellow): 
    
    if keys_pressed[pygame.K_a] and yellow.x - VEL > 0: ### a --> LEFT
        yellow.x -= VEL
    elif keys_pressed[pygame.K_d] and yellow.x + VEL < SCREEN_SEPARATOR.x - yellow.width: ### d --> RIGHT
        yellow.x += VEL
    elif keys_pressed[pygame.K_w] and yellow.y - VEL > 0: ### w --> DOWN
        yellow.y -= VEL
    elif keys_pressed[pygame.K_s] and yellow.y + VEL + yellow.height + 5 < HEIGHT: ### s --> UP
        yellow.y += VEL

def red_handle_movement(keys_pressed, red):

    if keys_pressed[pygame.K_LEFT] and red.x - VEL > SCREEN_SEPARATOR.x + 25:
        red.x -= VEL
    elif keys_pressed[pygame.K_RIGHT] and red.x + VEL < WIDTH - (red.width - 15):
        red.x += VEL
    elif keys_pressed[pygame.K_UP] and red.y - VEL > 0:
        red.y -= VEL
    elif keys_pressed[pygame.K_DOWN] and red.y + VEL + red.height < HEIGHT:
        red.y += VEL



def draw_window(red, yellow): 
    WIN.fill(WHITE)

    pygame.draw.rect(WIN, BLACK, SCREEN_SEPARATOR)

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
        
        keys_pressed = pygame.key.get_pressed() ### pygame.key.get_pressed() returns a list  
        yellow_handle_movement(keys_pressed, yellow) ### handling keys_pressed event for YELLOW_SPACESHIP 
        red_handle_movement(keys_pressed, red) ### handling keys_pressed event for RED_SPACESHIP
        
        ### red.x -= 1
        draw_window(red, yellow)

# call the main game function
if __name__ == "__main__": 
    main()


pygame.quit()

