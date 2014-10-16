import pygame, sys, math
from pygame.locals import *
from colors import *

screen = pygame.display.set_mode((400,115))

class GUI_Helper():

    def __init__(self, color1, color2, butx, buty):
        self.color1 = color1
        self.color2 = color2
        self.butx = butx
        self.buty = buty

    def Standard_button_make(self, borsize, butsize):
        self.butbor = (borsize-butsize) / 2
        pygame.draw.rect(screen, self.color1, Rect((self.butx,self.buty), (borsize,borsize)))
        pygame.draw.rect(screen, self.color2, Rect((self.butx+self.butbor,self.buty+self.butbor), (butsize,butsize)))

    def Dot_button_make(self, color3, borsize, butsize, dotsize):
        self.butbor = (borsize-butsize) / 2
        self.dotbor = butsize-dotsize
        self.dotbor = (self.dotbor / 2) + dotsize / 3
        pygame.draw.rect(screen, self.color1, Rect((self.butx,self.buty), (borsize,borsize)))
        pygame.draw.rect(screen, self.color2, Rect((self.butx+self.butbor,self.buty+self.butbor), (butsize,butsize)))
        pygame.draw.rect(screen, color3, Rect((self.butx+self.dotbor,self.buty+self.dotbor), (dotsize,dotsize)))

    def Special_button_make(self, color3, color4, color5):
        pygame.draw.rect(screen, self.color1, Rect((self.butx,self.buty), (32,32)))
        pygame.draw.rect(screen, self.color2, Rect((self.butx+3,self.buty+3), (13,13)))
        pygame.draw.rect(screen, color3, Rect((self.butx+16,self.buty+3), (13,13)))
        pygame.draw.rect(screen, color4, Rect((self.butx+3,self.buty+16), (13,13)))
        pygame.draw.rect(screen, color5, Rect((self.butx+16,self.buty+16), (13,13)))
        
    def Standard_cbutton_make(self):
        pygame.draw.circle(screen, self.color1, (self.butx, self.buty), 16)
        pygame.draw.circle(screen, self.color2, (self.butx, self.buty), 13)

    def Dot_cbutton_make(self, color3):
        pygame.draw.circle(screen, self.color1, (self.butx, self.buty), 16)
        pygame.draw.circle(screen, self.color2, (self.butx, self.buty), 13)
        pygame.draw.circle(screen, color3, (self.butx,self.buty), 3)

        
