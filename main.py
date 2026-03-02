import pygame
from constants import SCREEN_WIDTH, SCREEN_HEIGHT
from logger import log_state
from player import Player
from asteroidfield import AsteroidField
from asteroid import Asteroid

def main():
    pygame.init()                               # Initialising pygame
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT)) # Getting new instance of GUI window
    clock = pygame.time.Clock()                  # Creating the clock object

    # Creating group class to contain multiple game objects
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2) # Instantiating a player object
    asteroid = AsteroidField()

    dt = 0
    """
    Delta time is amount of time passed since the last frame was drawn
    Useful in decoupling the game's speed and the speed it's being drawn on screen
    
    """



    while True:                                  # Creating the infinite loop for the game loop
        log_state()

        for event in pygame.event.get():         # Processing pygame event queue
            if event.type == pygame.QUIT:        # Checks if the user closed the window and exit the game loop if they do
                return

        updatable.update(dt)

        screen.fill("black")                    # Filling the screen with a solid black color

        for obj in drawable:
            obj.draw(screen)

        pygame.display.flip()                   # Refreshing the screen

        
       # Limiting the frame rate to 60fps
       # Pauses the game loop until 1/60th of a second has passed and returns delta time(ms)
        dt = clock.tick(60)/1000                # Delta time in seconds


if __name__ == "__main__":
    main()
