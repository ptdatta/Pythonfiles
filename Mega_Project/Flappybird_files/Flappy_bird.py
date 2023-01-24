import random
import sys
import pygame
from pygame.locals import *

# Global Variables for the game
FPS=32
SCREENWIDTH=289
SCREENHEIGHT=511
SCREEN=pygame.display.set_mode((SCREENWIDTH,SCREENHEIGHT))
GROUNDY=SCREENHEIGHT*0.8
GAME_SPRITS={}
GAME_SOUNDS={}
PLAYER='pngkey.com-flappy-bird-png-8781424.png'
BACKGROUND='87879565-game-background.jpg'
PIPE='pngkey.com-flappy-bird-pipe-png-1831473.png'

def welcomeScreen():
    """
     Shows image on welcome screen
    """
    playerx=int(SCREENWIDTH/5)
    playery=int((SCREENHEIGHT-GAME_SPRITS['player'].get_height())/2)
    messagex=int((SCREENHEIGHT-GAME_SPRITS['message'].get_width())/2)
    messagey=int(SCREENHEIGHT*0.13)
    basex=0
    while True:
        for event in pygame.event.get():
            if event.type==QUIT or (event.type==KEYDOWN and event.key==K_ESCAPE):
                pygame.quit()
                sys.exit()

            elif event.type==KEYDOWN and (event.key==K_SPACE or event.key==K_UP):
                return
            else:
                SCREEN.blit(GAME_SPRITS['background'],(0,0))
                SCREEN.blit(GAME_SPRITS['player'],(playerx,playery))
                SCREEN.blit(GAME_SPRITS['message'],(messagex,messagey))
                SCREEN.blit(GAME_SPRITS['base'],(basex,GROUNDY))
                pygame.display.update()
                FPSCLOCK.tick(FPS)

def mainGame():
    score=0
    playerx=int(SCREENWIDTH/5)
    playery=int(SCREENWIDTH/2)

if __name__ == '__main__':
    pygame.init()
    FPSCLOCK=pygame.time.Clock()
    pygame.display.set_caption('FlappyBird by Parthib')
    GAME_SPRITS['numbers']=(
        # pygame.image.load('E:\Pycharm\Projects\Mega_Project\Flappybird_files\0.png').convert_alpha(),
        # pygame.image.load('E:\Pycharm\Projects\Mega_Project\Flappybird_files\1.png').convert_alpha(),
        # pygame.image.load('E:\Pycharm\Projects\Mega_Project\Flappybird_files\2.png').convert_alpha(),
        # pygame.image.load('E:\Pycharm\Projects\Mega_Project\Flappybird_files\3.png').convert_alpha(),
        # pygame.image.load('E:\Pycharm\Projects\Mega_Project\Flappybird_files\4.png').convert_alpha(),
        # pygame.image.load('E:\Pycharm\Projects\Mega_Project\Flappybird_files\5.png').convert_alpha(),
        # pygame.image.load('E:\Pycharm\Projects\Mega_Project\Flappybird_files\6.png').convert_alpha(),
        # pygame.image.load('E:\Pycharm\Projects\Mega_Project\Flappybird_files\7.png').convert_alpha(),
        # pygame.image.load('E:\Pycharm\Projects\Mega_Project\Flappybird_files\8.png').convert_alpha(),
        # pygame.image.load('E:\Pycharm\Projects\Mega_Project\Flappybird_files\9.png').convert_alpha(),
    )

    GAME_SPRITS['message']=pygame.image.load('pngkey.com-flappy-bird-pipe-png-1831473.png').convert_alpha()
    GAME_SPRITS['base']=pygame.image.load('pngkey.com-flappy-bird-pipe-png-1831473.png').convert_alpha()
    GAME_SPRITS['pipe']=(pygame.transform.rotate(pygame.image.load(PIPE).convert_alpha(),180),
                         pygame.image.load(PIPE).convert_alpha()
    )

#     game sounds
#     GAME_SOUNDS['die']=pygame.mixer.Sound('')
#     GAME_SOUNDS['hit']=pygame.mixer.Sound('')
#     GAME_SOUNDS['point']=pygame.mixer.Sound('')
#     GAME_SOUNDS['swoosh']=pygame.mixer.Sound('')
#     GAME_SOUNDS['wing']=pygame.mixer.Sound('')
#     GAME_SOUNDS['die']=pygame.mixer.Sound('')

    GAME_SPRITS['background']=pygame.image.load(BACKGROUND).convert()
    GAME_SPRITS['player']=pygame.image.load(PLAYER).convert_alpha()

while True:
    welcomeScreen()              #shows welcome screen
    mainGame()

