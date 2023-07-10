import pygame 
import os 

pygame.init()

WIDTH, HEIGHT = 800, 800
FPS = 60

JUMP_HEIGHT = 20
Y_VELOCITY = JUMP_HEIGHT
Y_GRAVITY = 1.0

X_POSITION, Y_POSITION = 400, 660

CLOCK = pygame.time.Clock()

is_jumping = False

BACKGROUND = pygame.image.load(os.path.join("jumping_logic", "background.png"))
STANDING_SURFACE = pygame.transform.scale(pygame.image.load(os.path.join("jumping_logic", "mario_standing.png")), (48, 64))
JUMPING_SURFACE = pygame.transform.scale(pygame.image.load(os.path.join("jumping_logic", "mario_jumping.png")), (48, 64))

WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Mario Jumping")

def render(surface, mario_rect): 
    WIN.blit(BACKGROUND, (0, 0))
    WIN.blit(surface, mario_rect)
    pygame.display.flip()

def main(): 
    running = True 

    global is_jumping
    global X_POSITION
    global Y_POSITION
    global Y_VELOCITY

    while running :
        for event in pygame.event.get(): 
            if event.type == pygame.QUIT: 
                running = False 
        
        key_pressed = pygame.key.get_pressed()
        if key_pressed[pygame.K_SPACE]: 
            is_jumping = True 
        
        if is_jumping: 
            Y_POSITION -= Y_VELOCITY
            Y_VELOCITY -= Y_GRAVITY

            if Y_VELOCITY < -JUMP_HEIGHT: 
                Y_VELOCITY = JUMP_HEIGHT
                is_jumping = False 

            mario_rect = JUMPING_SURFACE.get_rect(center=(X_POSITION, Y_POSITION))
            render(JUMPING_SURFACE, mario_rect)
        else: 
            mario_rect = STANDING_SURFACE.get_rect(center=(X_POSITION, Y_POSITION))
            render(STANDING_SURFACE, mario_rect)
        
        CLOCK.tick(FPS)


if __name__ == "__main__": 
    main()


pygame.quit()