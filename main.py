import pygame
import sys

from asteroidfield import AsteroidField
from asteroid import Asteroid
from constants import SCREEN_WIDTH, SCREEN_HEIGHT
from logger import log_state, log_event
from player import Player
from shot import Shot

def main():
    pygame.init()                               # Initialising pygame
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT)) # Getting new instance of GUI window
    clock = pygame.time.Clock()                  # Creating the clock object

    # Creating group class to contain multiple game objects
    asteroids = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    updatable = pygame.sprite.Group()

    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    Player.containers = (updatable, drawable)
    Shot.containers = (shots, updatable, drawable)

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

        for astrd in asteroids:
            if astrd.collides_with(player):
                log_event("player_hit")
                print("Game over!")
                sys.exit()

        screen.fill("black")                    # Filling the screen with a solid black color

        for obj in drawable:
            obj.draw(screen)

        pygame.display.flip()                   # Refreshing the screen

        
       # Limiting the frame rate to 60fps
       # Pauses the game loop until 1/60th of a second has passed and returns delta time(ms)
        dt = clock.tick(60)/1000                # Delta time in seconds


if __name__ == "__main__":
    main()
