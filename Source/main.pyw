import pygame, sys, math, pygame.mixer, time
from pygame.locals import *
from GUI_Helper import *
from colors import *
from scales import *
from button_handler import *
from text_handler import *
pygame.init()

def Pre_Build():

    #GUI Building
    screen.fill(black)
    #Main Panels
    pygame.draw.rect(screen, gray, Rect((2,2), (396,111)))
    pygame.draw.rect(screen, light_gray, Rect((4,19), (392,92)))
    pygame.draw.rect(screen, dark_blue, Rect((4,4), (392, 15)))
    pygame.draw.rect(screen, bright_gray, Rect((334,21), (60,88)))
    pygame.draw.rect(screen, bright_gray, Rect((6,21), (50,88)))
    pygame.draw.rect(screen, med_gray, Rect((56,69), (278,40)))
    pygame.draw.rect(screen, med_gray, Rect((165,21),(64,46)))
    #Adding Buttons to Screen
    Button_Print()
    buttons=[lebutton, abutton, dbutton, gbutton, bbutton, hebutton,
             clebutton, cabutton, cdbutton, cgbutton, cbbutton, chebutton,
             tupbutton, tdobutton, ctupbutton, ctdobutton]
    #Window GUI Building
    pygame.display.set_caption('PyTuner v1.2 ~ Joshua Smith')
    #Adding Text to Screen
    screen.blit(titletext, (125, 7))
    screen.blit(infotext, (335, 23))
    screen.blit(insttext, (336, 100))
    screen.blit(infobut1, (353, 50))
    screen.blit(infobut2, (353, 66))
    #Other Variables
    clock = pygame.time.Clock()
    bh = Button_Handler(buttons, sfont, notes)
    
    
    pygame.display.update()
    Main(sfont, notes, tuning, tune, tunec, tunemax, buttons, clock, bh)

def Pressed_Handler(pressed, buttons):
    if pressed != '':
        if pressed =='red':
            buttons[0].Standard_button_make(32,28)
        elif pressed =='orange':
            buttons[1].Standard_button_make(32,28)
        elif pressed =='yellow':
            buttons[2].Standard_button_make(32,28)
        elif pressed =='green':
            buttons[3].Standard_button_make(32,28)
        elif pressed =='cyan':
            buttons[4].Standard_button_make(32,28)
        elif pressed =='blue':
            buttons[5].Standard_button_make(32,28)
        elif pressed =='tgreen':                    
            buttons[12].Dot_button_make(mint, 42, 38, 8)
        elif pressed =='tred':                   
            buttons[13].Dot_button_make(pink, 42, 38, 8)
    else:
        pressed = 'black'

def Button_Print():
    lebutton.Standard_button_make(32, 28)
    abutton.Standard_button_make(32, 28)
    dbutton.Standard_button_make(32, 28)
    gbutton.Standard_button_make(32, 28)
    bbutton.Standard_button_make(32, 28)
    hebutton.Standard_button_make(32, 28)
    tupbutton.Dot_button_make(mint, 42, 38, 8)
    tdobutton.Dot_button_make(pink, 42, 38, 8)
    infobutton1.Dot_button_make(mint, 15, 13, 3)
    infobutton2.Dot_button_make(pink, 15, 13, 3)

def Main(sfont, notes, tuning, tune, tunec, tunemax, buttons, clock, bh):
    tunelevel = 'EStandard'
    pressed = 'black'
    while True:
        clock.tick(60)
        mouseX, mouseY = pygame.mouse.get_pos()
        coords=(mouseX, mouseY)
        tunetext = sfont[0].render(tunelevel, 1, (black), (bright_gray))
        screen.blit(tunetext, (336, 35))
        #coordstext = sfont[0].render(str(mouseX) + ',' + str(mouseY) + '   ', 1, (black), (bright_gray))
        #screen.blit(coordstext, (336,82))
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    pygame.quit() 
                    sys.exit()
                elif event.key == K_z:
                    pressed = 'red'
                    bh.Red_button(tune, tuning)
                elif event.key == K_x:
                    pressed = 'orange'
                    bh.Orange_button(tune, tuning)
                elif event.key == K_c:
                    pressed = 'yellow'
                    bh.Yellow_button(tune, tuning)
                elif event.key == K_v:
                    pressed = 'green'
                    bh.Green_button(tune, tuning)
                elif event.key == K_b:
                    pressed = 'cyan'
                    bh.Cyan_button(tune, tuning)
                elif event.key == K_n:
                    pressed = 'blue'
                    bh.Blue_button(tune, tuning)
                elif event.key == K_UP:
                    pressed = 'tgreen'
                    buttons[14].Dot_button_make(green, 42, 38, 8)
                    pygame.display.update()
                    if tunec < tunemax:
                        tunec = tunec + 1
                        if tunec == 1:
                            tunelevel = 'DropC       ' 
                        elif tunec == 2:
                            tunelevel = 'DAEAEE     ' 
                        elif tunec == 3:
                            tunelevel = 'DropD       '
                        elif tunec == 4:
                            tunelevel = '1/2StepDn '
                        elif tunec == 5:
                            tunelevel = 'EStandard'
                        tune=tuning[tunec]
                elif event.key == K_DOWN:
                    pressed = 'tred'
                    buttons[15].Dot_button_make(red, 42, 38, 8)
                    pygame.display.update()
                    if tunec == tunemax or tunec > 0:
                        tunec = tunec - 1
                        if tunec == 0:
                            tunelevel = 'CStandard' 
                        elif tunec == 1:
                            tunelevel = 'DropC       '
                        elif tunec == 2:
                            tunelevel = 'DAEAEE     '
                        elif tunec == 3:
                            tunelevel = 'DropD       '
                        elif tunec == 4:
                            tunelevel = '1/2StepDn '
                        tune=tuning[tunec]
                    

            elif event.type == KEYUP:
                Pressed_Handler(pressed, buttons)
                    
            elif event.type == MOUSEBUTTONDOWN:
                #Tune Buttons
                if mouseY < 65 and mouseY > 21:
                    if coords >= (10,22) and coords <= (51,63):
                        pressed = 'tgreen'
                        buttons[14].Dot_button_make(green, 42, 38, 8)
                        pygame.display.update()
                        if tunec < tunemax:
                            tunec = tunec + 1
                            if tunec == 1:
                                tunelevel = 'CStandard'
                            elif tunec == 2:
                                tunelevel = 'DAEAEE      '
                            elif tunec == 3:
                                tunelevel = 'DropD       '
                            elif tunec == 4:
                                tunelevel = '1/2StepDn'
                            elif tunec == 5:
                                tunelevel = 'EStandard'
                elif mouseY < 108 and mouseY > 66:
                    if coords >= (10,66) and coords <= (51,107):
                        pressed = 'tred'
                        buttons[15].Dot_button_make(red, 42, 38, 8)
                        pygame.display.update()
                        if tunec == tunemax or tunec > 0:
                            tunec = tunec - 1
                            if tunec == 0:
                                tunelevel = 'DropC       '
                            elif tunec == 1:
                                tunelevel = 'CStandard'
                            elif tunec == 2:
                                tunelevel = 'DAEAEE      '
                            elif tunec == 3:
                                tunelevel = 'DropD       '
                            elif tunec == 4:
                                tunelevel = '1/2StepDn'
                tune=tuning[tunec]

                #Note Buttons
                if mouseY >= 73 and mouseY <= 105: 
                    if coords >= (91,73) and coords <= (122,105):
                        pressed = 'red'
                        bh.Red_button(tune, tuning)
                    elif coords >= (126,73) and coords <= (157,105):
                        pressed = 'orange'
                        bh.Orange_button(tune, tuning)
                    elif coords >= (161,73) and coords <= (192,105):
                        pressed = 'yellow'
                        bh.Yellow_button(tune, tuning)    
                    elif coords >= (196,73) and coords <= (227,105):
                        pressed = 'green'
                        bh.Green_button(tune, tuning)             
                    elif coords >= (231,73) and coords <= (262,105):
                        pressed = 'cyan'
                        bh.Cyan_button(tune, tuning)               
                    elif coords >= (266,73) and coords <= (297,105):
                       pressed = 'blue'
                       bh.Blue_button(tune, tuning)      

            elif event.type == MOUSEBUTTONUP:
                Pressed_Handler(pressed, buttons)
                    
        pygame.display.update()


Pre_Build()

