import pygame

# initializing pygame
pygame.init()

# setting up the display window 
WIDTH, HEIGHT = 700, 700
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Hello PyGame")

# main game loop
def main():

    run = True
    while run: 
        ## handling events 
        for events in pygame.event.get(): ### pygame.event.get() returns a list 
            if events.type == pygame.QUIT: 
                run = False
        

        # screen rendering 
        WIN.fill((0, 0, 0))
        pygame.display.flip() ### updates the screen


# calling the main function to start the game
main()

# quit the game
pygame.quit()

            



