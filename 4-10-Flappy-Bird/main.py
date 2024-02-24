'''
     AUTHOR: Pooja Patel
     

DESCRIPTION: FlapPyBird Remake. 

DEMO FEATURES:
             -- Images and Sound organized into folders
             -- Simple animated Bird sprite + <SPACE> Event
             -- Infinite Scrolling City Background
             -- Infinite Scrolling Foreground + Collisions

Yet to do:
  1. Add Pipe Sprites
  2. Add Pipe Collisions  
  3. Add Score Keeper
'''

# I - Import and Initialize
import pygame
import mySprites

            
def main():
    '''This function defines the 'mainline logic' for our game.'''
    # Intialize
    pygame.init()
    pygame.mixer.init()

    # Display
    screen = pygame.display.set_mode((284, 480))
    pygame.display.set_caption("FlapPyBird Demo")
    
    # Entities
    background = pygame.Surface(screen.get_size())
    background = background.convert()
    background.fill((255, 255, 255))
    screen.blit(background, (0,0))
    
    bird = mySprites.Bird()
    # create CityBackground and Ground sprite objects from our mySprites module
    city = mySprites.CityBackground(screen)
    ground = mySprites.Ground(screen)
    
    # add our sprites to an OrderedUpdates Sprite Group to keep Refresh section simple
    allSprites = pygame.sprite.OrderedUpdates(city, ground, bird)
    
    # Background Music and Sound Effect(s)
    pygame.mixer.music.load("mySounds/DuckSong.ogg")
    pygame.mixer.music.set_volume(0.3)
    pygame.mixer.music.play(-1)

    quack = pygame.mixer.Sound("mySounds/Quack.ogg")
    quack.set_volume(0.5)
        
    # ACTION
    
    # Assign 
    clock = pygame.time.Clock()
    keepGoing = True
    
    # Loop
    while keepGoing:
    
        # Time
        clock.tick(30)
    
        # Events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                keepGoing = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    bird.flapUp()

        # Collision Detection: Bird with Ground
        if bird.rect.colliderect(ground.rect):
            quack.play()
            pygame.mixer.music.fadeout(2000)
            keepGoing = False

        # Refresh screen
        allSprites.clear(screen, background)
        allSprites.update()
        allSprites.draw(screen)
    
        pygame.display.flip()

    # Close the game window after 2 second delay
    pygame.time.delay(2000)
    pygame.quit()        

# Call the main function
main()
