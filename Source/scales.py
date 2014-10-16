import pygame, pygame.mixer
from pygame.locals import *
pygame.init()

#Tuning Scales
E_Standard = ['Data\LowE.wav', 'Data\A.wav', 'Data\D.wav', 'Data\G.wav',
              'Data\B.wav', 'Data\HighE.wav']
Drop_D = ['Data\LowD.wav', 'Data\A.wav', 'Data\D.wav', 'Data\G.wav',
          'Data\B.wav', 'Data\HighE.wav']
C_Standard = ['Data\LowC.wav', 'Data\F.wav', 'Data\A#.wav', 'Data\D#.wav',
          'Data\HighG.wav', 'Data\HighC.wav']
Half_StepD = ['Data\LowEb.wav', 'Data\Ab.wav', 'Data\Db.wav', 'Data\Gb.wav',
          'Data\Bb.wav', 'Data\HighEb.wav']
DAE_AEE = ['Data\LowD.wav', 'Data\A.wav', 'Data\MidE.wav', 'Data\HighA.wav',
          'Data\HighE.wav', 'Data\HighE.wav']
Drop_C = ['Data\LowC.wav', 'Data\LowG.wav', 'Data\MidC.wav', 'Data\MidF.wav',
          'Data\MidA.wav', 'Data\HighD.wav']


tuning = [C_Standard, Drop_C, DAE_AEE, Drop_D, Half_StepD, E_Standard]
tune = tuning[5]
tunec = 5
tunemax = 5
#Drop D
noteLD = pygame.mixer.Sound(Drop_D[0])
#E Standard
noteLE = pygame.mixer.Sound(E_Standard[0])
noteA = pygame.mixer.Sound(E_Standard[1])
noteD = pygame.mixer.Sound(E_Standard[2])
noteG = pygame.mixer.Sound(E_Standard[3])
noteB = pygame.mixer.Sound(E_Standard[4])
noteHE = pygame.mixer.Sound(E_Standard[5])
#C Standard
noteLC = pygame.mixer.Sound(C_Standard[0])
noteF = pygame.mixer.Sound(C_Standard[1])
noteAs = pygame.mixer.Sound(C_Standard[2])
noteDs = pygame.mixer.Sound(C_Standard[3])
noteHG = pygame.mixer.Sound(C_Standard[4])
noteHC = pygame.mixer.Sound(C_Standard[5])
#1/2 Step Down
noteLEb = pygame.mixer.Sound(Half_StepD[0])
noteAb = pygame.mixer.Sound(Half_StepD[1])
noteDb = pygame.mixer.Sound(Half_StepD[2])
noteGb = pygame.mixer.Sound(Half_StepD[3])
noteBb = pygame.mixer.Sound(Half_StepD[4])
noteHEb = pygame.mixer.Sound(Half_StepD[5])
#DAE_AEE
noteME = pygame.mixer.Sound(DAE_AEE[2])
noteHA = pygame.mixer.Sound(DAE_AEE[3])
#Drop_C
noteLG = pygame.mixer.Sound(Drop_C[1])
noteMC = pygame.mixer.Sound(Drop_C[2])
noteMF = pygame.mixer.Sound(Drop_C[3])
noteMA = pygame.mixer.Sound(Drop_C[4])
noteHD = pygame.mixer.Sound(Drop_C[5])

notes = [noteLD, noteLE, noteA, noteD, noteG, noteB, noteHE, noteLC,
         noteF, noteAs, noteDs, noteHG, noteHC, noteLEb, noteAb, noteDb,
         noteGb, noteBb, noteHEb, noteME, noteHA, noteLG, noteMC, noteMF,
         noteMA, noteHD]
