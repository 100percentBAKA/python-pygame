import pygame
import os # taking the help of OS to define the paths to game assets 

# game constants
WHITE = ((255, 255, 255))
BLACK = ((0, 0, 0))
RED = ((200, 0, 0)) ### darker shade of RED
YELLOW = ((255, 255, 0)) ### combining RED and GREEN to get YELLOW

WIDTH, HEIGHT = 1000, 700
FPS = 60
VEL = 5 ### velocity
BULLET_VEL = 7
MAX_BULLETS = 3
SPACESHIP_WIDTH, SPACESHIP_HEIGHT = 55, 40
SCREEN_SEPARATOR = pygame.Rect(WIDTH//2 - 5, 0, 10, HEIGHT)

YELLOW_SPACESHIP_IMAGE = pygame.image.load(os.path.join("python-shooter-game", "Assets", "spaceship_yellow.png"))
YELLOW_SPACESHIP = pygame.transform.rotate(pygame.transform.scale(YELLOW_SPACESHIP_IMAGE, (SPACESHIP_WIDTH, SPACESHIP_HEIGHT)), 90)
RED_SPACESHIP_IMAGE = pygame.image.load(os.path.join("python-shooter-game", "Assets", "spaceship_red.png"))
RED_SPACESHIP = pygame.transform.rotate(pygame.transform.scale(RED_SPACESHIP_IMAGE, (SPACESHIP_WIDTH, SPACESHIP_HEIGHT)), 270)

# creating custom user events 
RED_HIT = pygame.USEREVENT + 1
YELLOW_HIT = pygame.USEREVENT + 2

# creating screen
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Space Shooter")

def handle_bullet(yellow_bullets, red_bullets, yellow, red):
    for bullet in yellow_bullets: 
        bullet.x += BULLET_VEL

        if red.colliderect(bullet):
            pygame.event.post(pygame.event.Event(RED_HIT))
            yellow_bullets.remove(bullet)
    
    for bullet in red_bullets: 
        bullet.x -= BULLET_VEL

        if red.colliderect(bullet):
            pygame.event.post(pygame.event.Event(YELLOW_HIT))
            red_bullets.remove(bullet)


def yellow_handle_movement(keys_pressed, yellow): 
    
    if keys_pressed[pygame.K_a] and yellow.x - VEL > 0: ### a --> LEFT
        yellow.x -= VEL
    elif keys_pressed[pygame.K_d] and yellow.x + VEL < SCREEN_SEPARATOR.x - yellow.width: ### d --> RIGHT
        yellow.x += VEL
    elif keys_pressed[pygame.K_w] and yellow.y - VEL > 0: ### w --> DOWN
        yellow.y -= VEL
    elif keys_pressed[pygame.K_s] and yellow.y + VEL + yellow.height  < HEIGHT: ### s --> UP
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



def draw_window(red, yellow, red_bullets, yellow_bullets): 
    WIN.fill(WHITE)

    pygame.draw.rect(WIN, BLACK, SCREEN_SEPARATOR)

    ## use blit() for drawing surfaces (ex: text, images) onto screen
    WIN.blit(YELLOW_SPACESHIP, (yellow.x, yellow.y)) 
    WIN.blit(RED_SPACESHIP, (red.x, red.y))

    for bullet in red_bullets: 
        pygame.draw.rect(WIN, RED, bullet)
    
    for bullet in yellow_bullets:
        pygame.draw.rect(WIN, YELLOW, bullet)

    pygame.display.update() ### renders the screen components (surface)

# main game 
def main(): 

    ## co-ordinates of yellow and red Rect will be assigned to the co-ordinates of YELLOW and RED_SPACESHIP
    ## by modifying the co-ordinates of the rectangle, the spaceships move accordingly 
    yellow = pygame.Rect(100, 300, SPACESHIP_WIDTH, SPACESHIP_HEIGHT)
    red = pygame.Rect(700, 300, SPACESHIP_WIDTH, SPACESHIP_HEIGHT)

    yellow_bullets = []
    red_bullets = []

    clock = pygame.time.Clock()
    running = True

    # main game loop
    while running: 
        clock.tick(FPS) ### while loop never runs over 60/second 

        # handle event
        for events in pygame.event.get(): ### returns a list 
            if events.type == pygame.QUIT: 
                running = False
            
            if events.type == pygame.KEYDOWN:
                if events.key == pygame.K_LCTRL and len(yellow_bullets) < MAX_BULLETS: 
                    bullet = pygame.Rect(yellow.x + yellow.width, yellow.y + yellow.height//2, 10, 5)
                    yellow_bullets.append(bullet)

                if events.key == pygame.K_RCTRL and len(red_bullets) < MAX_BULLETS: 
                    bullet = pygame.Rect(red.x, red.y + red.height//2, 10, 5)
                    red_bullets.append(bullet)


        print(yellow_bullets, red_bullets)
        keys_pressed = pygame.key.get_pressed() ### pygame.key.get_pressed() returns a list  
        yellow_handle_movement(keys_pressed, yellow) ### handling keys_pressed event for YELLOW_SPACESHIP 
        red_handle_movement(keys_pressed, red) ### handling keys_pressed event for RED_SPACESHIP
        
        handle_bullet(yellow_bullets, red_bullets, yellow, red)
        draw_window(red, yellow, red_bullets, yellow_bullets)

# call the main game function
if __name__ == "__main__": 
    main()


pygame.quit()

