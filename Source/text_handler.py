import pygame, sys
from pygame.locals import *
from colors import *

pygame.init()

font = pygame.font.Font(None, 15)
font2 = pygame.font.Font(None, 45)
font3 = pygame.font.Font(None, 24)
sfont = [font, font2]
titletext = font.render('PyTuner v1.2 - Joshua Smith', 1, (white))
infotext = font.render('Tune:', 1, (black))
insttext = font.render('\'ESC\' - Exit' , 1, (black))
infobut1 = font.render(':Tune +', 1, (black))
infobut2 = font.render(':Tune -', 1, (black))
