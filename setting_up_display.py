# initializing pygame
pygame.init()

# setting up the display window 
# setting up the display window/surface 
WIDTH, HEIGHT = 700, 700
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Hello PyGame")

# main game loop
# main game
def main():

    run = True
    # main game loop
    while run: 
        ## handling events 
        for events in pygame.event.get(): ### pygame.event.get() returns a list 
@ -21,11 +22,14 @@ def main():

        # screen rendering 
        WIN.fill((0, 0, 0))
        pygame.display.update() ### updates the screen
        ## pygame.display.fill() ### renders the entire display surface at once 
        pygame.display.update() ### renders the screen component by component 


# calling the main function to start the game
main()
# calling the main function (from this file and not from any other files or modules) to start the game
if __name__ == "__main__":
    main()


# quit the game
pygame.quit()
