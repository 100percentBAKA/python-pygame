import pygame 

# initializing pygame
pygame.init()

# game constants 
WIDTH, HEIGHT = 700, 700
FPS = 60
RECT_WIDTH, RECT_HEIGHT = 250, 250
YELLOW =(255, 255, 0)
RED = (255, 0, 0)

# creating surface
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Shapes")

def render_surface(yellow, red):
    WIN.fill((0, 0, 0))
    pygame.draw.rect(WIN, YELLOW, yellow)
    pygame.draw.rect(WIN, RED, red)
    pygame.display.flip() ### updates all the screen contents at once 
    

def main():

    running = True 
    ## main game loop
    clock = pygame.time.Clock()

    yellow_rectangle = pygame.Rect(100, 200, RECT_WIDTH, RECT_HEIGHT)
    red_rectangle = pygame.Rect(200, 300, RECT_WIDTH, RECT_HEIGHT)

    while running: 
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT: 
                running = False

        render_surface(yellow_rectangle, red_rectangle)

if __name__ == "__main__": 
    main()

pygame.quit()    
