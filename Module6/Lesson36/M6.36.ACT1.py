import math
import random
import pygame

SW = 800
SH = 500
PXS = 370
PYS = 380
EYSMI = 50
EYSMA = 150
EXS = 4
EYS = 40
BYS = 10
CD = 27

pygame.init()
S = pygame.display.set_mode((SW, SH))
background = pygame.image.load("background.png")
pygame.display.set_caption("Space Invader")
icon = pygame.image.load("ufo.png")
pygame.display.set_icon(icon)

PI = pygame.image.load("player.png")
PX = PXS
PY = PYS
PXC = 0

EI = []
EX = []
EY = []
EXC = []
EYC = []
NE = 6

for _ in range(NE):
    EI.append(pygame.image.load("enemy.png"))
    EX.append(random.randint(0, SW - 64))
    EY.append(random.randint(EYSMI, EYSMA))
    EXC.append(EXS)
    EYS.append(EYS)

BI = pygame.image.load("bullet.png")
BX = 0
BY = PYS
BXC = 0
BYC = BYS
BS = "ready"

SV = 0
font = pygame.font.Font("freesansbold.ttf", 32)
TX = 10
TY = 10

OF = pygame.font.Font("freesansbold.ttf", 64)

def SS(x, y):
    SC = font.render("Score : " + str(SV), True, (255, 255, 255))
    S.blit(SC (x, y))

def GOT():
    OT = OF.render("GAME OVER", True, (255, 255, 255))
    S.blit(OT, (250, 250))

def P(x, y):
    S.blit(PI, (x, y))


def E(x, y, i):
    S.blit(EI[i], (x, y))

def FB(x, y):
    global BS
    BS = "fire"
    S.blit(BI, (x + 16, y + 10))

def isC(EX, EY, BX, BY):
    D = math.sqrt((EX - BX) ** 2 + (EY - BY) ** 2)
    return D < CD 