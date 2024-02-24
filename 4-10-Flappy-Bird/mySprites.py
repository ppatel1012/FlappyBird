import pygame

class Bird(pygame.sprite.Sprite):
    '''Our Bird class inherits from the Sprite class'''
    def __init__(self):
        '''Initializer to set sprite image and position'''
        # Call the parent __init__() method
        pygame.sprite.Sprite.__init__(self)

        # Load 2 images into list, we will alternate in update()
        self.birdImages = [ pygame.image.load("myImages/Bird0.png"), pygame.image.load("myImages/Bird1.png") ]

        # Start with Bird0.png as our initial image
        self.imageNum = 0
        self.image = self.birdImages[self.imageNum]

        # Position image at middle-left of screen
        self.rect = self.image.get_rect()
        self.rect.left = 50
        self.rect.top = 220

        # dy is used to control vertical direction of bird
        # start by moving down +1 pixel per frame
        self.dy = 1

    def flapUp(self):
        '''Causes Bird to fly UP 15pixels / frame'''
        self.dy = -15

    def update(self):
        '''Called automatically during Refresh to update sprite's position.'''
        # Update vertical position of Bird
        self.rect.top += self.dy

        # Alternate between bird imageNum 0 and 1
        self.image = self.birdImages[self.imageNum]
        self.imageNum = (self.imageNum + 1) % 2

        # Increase gravity for next frame
        self.dy += 1

class CityBackground(pygame.sprite.Sprite):
    '''Our CityBackground class inherits from the Sprite class'''
    def __init__(self, screen):
        '''Initializer to set sprite image and position'''
        pygame.sprite.Sprite.__init__(self)
        # Keep copy of reference to game window, need get_width() in update()
        self.window = screen

        # Load our background image
        self.image = pygame.image.load("myImages/CityBackground.png")
        self.image = self.image.convert()

        # Position image at top-left of screen
        self.rect = self.image.get_rect()
        self.rect.left = 0
        self.rect.top = 0

    def update(self):
        '''Called automatically during Refresh to update sprite's position.'''
        # Move 1 pixel to the left on each frame
        self.rect.left -= 1

        # If we run out of image on the right, reset the left side again
        if self.rect.right <= self.window.get_width():
            self.rect.left = 0

class Ground(pygame.sprite.Sprite):
    '''Our Ground class inherits from the Sprite class'''
    def __init__(self, screen):
        '''Initializer to set sprite image and position'''
        pygame.sprite.Sprite.__init__(self)

        # Keep copy of reference to game window, need get_width() in update()
        self.window = screen

        # Load our background image
        self.image = pygame.image.load("myImages/Ground.png")
        self.image = self.image.convert()

        # Position image at bottom-left of screen
        self.rect = self.image.get_rect()
        self.rect.left = 0
        self.rect.top = 420


    def update(self):
        '''Called automatically during Refresh to update sprite's position.'''
        # Move 3 pixels to the left on each frame
        self.rect.left -= 3
        # If we run out of image on the right, reset the left side again
        if self.rect.right <= self.window.get_width():
            self.rect.left = 0

class Pipes(pygame.sprite.Sprite):
    def __init__(self, screen):
        '''Call the parent init class'''
        pygame.sprite.Sprite.__init__(self)

        #load the pipe picture
        self.image = pygame.image.load("myImages/UpPipe.png")
        self.image = self.image.convert()

        self.rect = self.image.get_rect()
        self.rect.left = 0
        self.rect.top = 0

