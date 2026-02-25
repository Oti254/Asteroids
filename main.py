import pygame
from constants import SCREEN_WIDTH, SCREEN_HEIGHT
from logger import log_state

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT)) # Getting new instance of GUI window
    clock = pygame.time.Clock()                  # Creating the clock object
    dt = 0


    while True:                                  # Creating the infinite loop for the game loop
        log_state()

        for event in pygame.event.get():         # Processing pygame event queue
            if event.type == pygame.QUIT:        # Checks if the user closed the window and exit the game loop if they do
                return

        screen.fill("black")                    # Filling the screen with a solid black color
        pygame.display.flip()                   # Refreshing the screen

        
       # Limiting the frame rate to 60fps
       # Pauses the game loop until 1/60th of a second has passed and returns delta time(ms)
        dt = clock.tick(60)/1000                # Delta time in seconds

if __name__ == "__main__":
    main()
