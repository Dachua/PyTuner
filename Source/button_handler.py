from GUI_Helper import *
from colors import *

#Buttons
butpos=31
#Tune Buttons
tupbutton=GUI_Helper(white, black, 10, 22)
tdobutton=GUI_Helper(white, black, 10, 66)
ctupbutton=GUI_Helper(green, mint, 10, 22)
ctdobutton=GUI_Helper(red, pink, 10, 66)
#Note Buttons
lebutton=GUI_Helper(white, red, 60+butpos, 73)
abutton=GUI_Helper(white, orange, 95+butpos, 73)
dbutton=GUI_Helper(white, yellow, 130+butpos, 73)
gbutton=GUI_Helper(white, green, 165+butpos, 73)
bbutton=GUI_Helper(white, cyan, 200+butpos, 73)
hebutton=GUI_Helper(white, blue, 235+butpos, 73)
clebutton=GUI_Helper(light_gray, dark_red, 60+butpos, 73)
cabutton=GUI_Helper(light_gray, brown, 95+butpos, 73)
cdbutton=GUI_Helper(light_gray, dark_yellow, 130+butpos, 73)
cgbutton=GUI_Helper(light_gray, dark_green, 165+butpos, 73)
cbbutton=GUI_Helper(light_gray, dark_cyan, 200+butpos, 73)
chebutton=GUI_Helper(light_gray, dark_blue, 235+butpos, 73)
#Misc Buttons
infobutton1=GUI_Helper(white, black, 336, 46)
infobutton2=GUI_Helper(white, black, 336, 63)
        
class Button_Handler():

    def __init__(self, buttons, sfont, notes):
        self.buttons = buttons
        self.sfont = sfont
        self.notes = notes

    def Red_button(self, tune, tuning):
        self.buttons[6].Standard_button_make(32,28)
        pygame.display.update()
        if tune==tuning[5]:
            note = ' E  '
            notetext = self.sfont[1].render(note, 1, (black), (med_gray))
            screen.blit(notetext, (180, 31))
            self.notes[1].play()
        elif tune==tuning[4]:
            note = 'Eb'
            notetext = self.sfont[1].render(note, 1, (black), (med_gray))
            screen.blit(notetext, (180, 31))
            self.notes[13].play()
        elif tune==tuning[2] or tune==tuning[3]:
            note = ' D  '
            notetext = self.sfont[1].render(note, 1, (black), (med_gray))
            screen.blit(notetext, (180, 31))
            self.notes[0].play()
        elif tune==tuning[0] or tune==tuning[1]:
            note = ' C  '
            notetext = self.sfont[1].render(note, 1, (black), (med_gray))
            screen.blit(notetext, (180, 31))
            self.notes[7].play()
        return

    def Orange_button(self, tune, tuning):
        self.buttons[7].Standard_button_make(32,28)
        pygame.display.update()
        if tune == tuning[3] or tune == tuning[2] or tune == tuning[5]:
           note = ' A  '
           notetext = self.sfont[1].render(note, 1, (black), (med_gray))
           screen.blit(notetext, (180, 31))
           self.notes[2].play()
        elif tune==tuning[4]:
           note = 'Ab'
           notetext = self.sfont[1].render(note, 1, (black), (med_gray))
           screen.blit(notetext, (180, 31))
           self.notes[14].play()
        elif tune==tuning[0]:
           note = ' F  '
           notetext = self.sfont[1].render(note, 1, (black), (med_gray))
           screen.blit(notetext, (180, 31))
           self.notes[8].play()
        elif tune==tuning[1]:
           note = ' G  '
           notetext = self.sfont[1].render(note, 1, (black), (med_gray))
           screen.blit(notetext, (180, 31))
           self.notes[21].play()        
        return

    def Yellow_button(self, tune, tuning):
        self.buttons[8].Standard_button_make(32,28)
        pygame.display.update()
        if tune==tuning[3] or tune == tuning[5]:
            note = ' D  '
            notetext = self.sfont[1].render(note, 1, (black), (med_gray))
            screen.blit(notetext, (180, 31))
            self.notes[3].play()
        elif tune==tuning[4]:
            note = 'Db'
            notetext = self.sfont[1].render(note, 1, (black), (med_gray))
            screen.blit(notetext, (180, 31))
            self.notes[15].play()
        elif tune==tuning[0]:
            note = 'A#'
            notetext = self.sfont[1].render(note, 1, (black), (med_gray))
            screen.blit(notetext, (181, 31))
            self.notes[9].play()
        elif tune==tuning[2]:
            note = ' E  '
            notetext = self.sfont[1].render(note, 1, (black), (med_gray))
            screen.blit(notetext, (180, 31))
            self.notes[19].play()
        elif tune==tuning[1]:
           note = ' C  '
           notetext = self.sfont[1].render(note, 1, (black), (med_gray))
           screen.blit(notetext, (180, 31))
           self.notes[22].play()       
        return

    def Green_button(self, tune, tuning):
        self.buttons[9].Standard_button_make(32,28)
        pygame.display.update()
        if tune==tuning[3] or tune == tuning[5]:
            note = ' G  '
            notetext = self.sfont[1].render(note, 1, (black), (med_gray))
            screen.blit(notetext, (180, 31))
            self.notes[4].play()
        elif tune==tuning[4]:
            note = 'Gb'
            notetext = self.sfont[1].render(note, 1, (black), (med_gray))
            screen.blit(notetext, (180, 31))
            self.notes[16].play()
        elif tune==tuning[0]:
            note = 'D#'
            notetext = self.sfont[1].render(note, 1, (black), (med_gray))
            screen.blit(notetext, (181, 31))
            self.notes[10].play()
        elif tune==tuning[2]:
            note = ' A  '
            notetext = self.sfont[1].render(note, 1, (black), (med_gray))
            screen.blit(notetext, (180, 31))
            self.notes[20].play()
        elif tune==tuning[1]:
          note = ' F  '
          notetext = self.sfont[1].render(note, 1, (black), (med_gray))
          screen.blit(notetext, (180, 31))
          self.notes[23].play()       
        return

    def Cyan_button(self, tune, tuning):
        self.buttons[10].Standard_button_make(32,28)
        pygame.display.update()
        if tune==tuning[3] or tune == tuning[5]:
            note = ' B  '
            notetext = self.sfont[1].render(note, 1, (black), (med_gray))
            screen.blit(notetext, (180, 31))
            self.notes[5].play()
        elif tune==tuning[4]:
            note = 'Bb '
            notetext = self.sfont[1].render(note, 1, (black), (med_gray))
            screen.blit(notetext, (180, 31))
            self.notes[17].play()
        elif tune==tuning[0]:
            note = ' G  '
            notetext = self.sfont[1].render(note, 1, (black), (med_gray))
            screen.blit(notetext, (180, 31))
            self.notes[11].play()
        elif tune==tuning[2]:
            note = ' e  '
            notetext = self.sfont[1].render(note, 1, (black), (med_gray))
            screen.blit(notetext, (180, 28))
            self.notes[6].play()
        elif tune==tuning[1]:
            note = ' A  '
            notetext = self.sfont[1].render(note, 1, (black), (med_gray))
            screen.blit(notetext, (180, 31))
            self.notes[24].play()       
        return

    def Blue_button(self, tune, tuning):
        self.buttons[11].Standard_button_make(32,28)
        pygame.display.update()
        if tune==tuning[3] or tune == tuning[5] or tune == tuning[2]:
            note = ' e  '
            notetext = self.sfont[1].render(note, 1, (black), (med_gray))
            screen.blit(notetext, (180, 28))
            self.notes[6].play()
        elif tune==tuning[4]:
            note = 'eb '
            notetext = self.sfont[1].render(note, 1, (black), (med_gray))
            screen.blit(notetext, (180, 31))
            self.notes[18].play()
        elif tune==tuning[0]:
            note = ' c  '
            notetext = self.sfont[1].render(note, 1, (black), (med_gray))
            screen.blit(notetext, (180, 28))
            self.notes[12].play()
        elif tune==tuning[1]:
            note = ' d  '
            notetext = self.sfont[1].render(note, 1, (black), (med_gray))
            screen.blit(notetext, (180, 31))
            self.notes[25].play()       
        return

