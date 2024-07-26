import random
import sys
import pygame 
from pygame.locals import *      # Basic pygame imports

# Global variables for the game
FPS = 32    # Frames per second
SCREENWIDTH = 289
SCREENHEIGHT = 511
SCREEN = pygame.display.set_mode((SCREENWIDTH,SCREENHEIGHT))
GROUNDY = SCREENHEIGHT * 0.8       # Ground/base in the game 
GAME_SPRITES = {}
GAME_SOUNDS = {}
PLAYER = '/Flappy_Bird_Game/Sprites/bird.png'
BACKGROUND = '/Flappy_Bird_Game/Sprites/bg.png'
PIPE = '/Flappy_Bird_Game/Sprites/pipe.png'

if __name__ == "__main__":
    # This will be the main point from where our game start
    pygame.init()  # used to initialize all imported PyGame modules
    FPSCLOCK = pygame.time.Clock()
    