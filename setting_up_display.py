import pygame

# initializing pygame
pygame.init()

# setting up the display window 
WIDTH, HEIGHT = 700, 700
FPS = 60

WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Hello PyGame")

def render_surface():
    WIN.fill((0,0,0)) ### black
    pygame.display.flip()

# main game loop
def main():
    run = True
    
    clock = pygame.time.Clock()
    while run: 
        clock.tick(FPS) ### setting the frame rate
        ## handling events 
        for events in pygame.event.get(): ### pygame.event.get() returns a list 
            if events.type == pygame.QUIT: 
                run = False
    
        render_surface()


# calling the main function to start the game
main()

# quit the game
pygame.quit()

            



