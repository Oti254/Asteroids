import pygame
from constants import SCREEN_WIDTH, SCREEN_HEIGHT
from logger import log_state

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT)) # Getting new instance of GUI window
    running = True
    while True: # Creating the infinite loop for the game loop
        log_state()
        for event in pygame.event.get(): # Processing pygame event queue
            # Checks if the user closed the window and exit the game loop if they do
            if event.type == pygame.QUIT:
                return
        screen.fill("black") # Filling the screen with a solid black color
        pygame.display.flip() # Refreshing the screen

    print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")


if __name__ == "__main__":
    main()
