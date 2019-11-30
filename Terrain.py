import array
import random
import sys
import pygame
import math
import socket
import numpy as np
print(np.__version__)


'''

#initializes video
pygame.init()
size = 450

#sets the screen size
screen = pygame.display.set_mode((900, 900))
def map(array, size):
    for i in range(size):
        temp = []
        for j in range(size):
            temp.append(0)
        array.append(temp)
    return array

def neighbors(terrain, i, j, L, C):
    possible_neigbors = [(i+di, j+dj) for di in [-1, 0, 1] for dj in [-1, 0, 1]]
    return [terrain[i2][j2] for (i2, j2) in possible_neigbors
              if i2 >= 0 and j2 >= 0 and i2 < L and j2 < C]

def generate_terrain(L, C):
    noisegrid = [[noise.pnoise2(j/C, i/L) for j in range(C)] for i in range(L)]
    terrain = [[int(noisegrid[i][j] > 0.12) for j in range(C)] for i in range(L)]

    for i in range(L):
        for j in range(C):
            if terrain[i][j] == 0:
                nb = neighbors(terrain, i, j, L, C)
                if 1 in nb:
                    terrain[i][j] = 2

    return terrain

terrain = generate_terrain(size, size)
for i in terrain:
    print(i)

biome1 = [(255, 255, 255), (240,248,255),(161,202,241),(153,186,221),(113,166,210),(100,149,237),(119,158,203),(91,146,229),(49,140,231),(0,127,255),(93,138,168),(96,130,182),(70,130,180),(21,96,189),x(83,104,120),(0,71,171),(15,77,146),(8,69,126),(54,69,79),(59,68,75),(0,51,102),(0,46,99),(0,33,71),(0,46,99),(0,33,71),(0,46,99),(0,33,71),(0,46,99),(0,46,99),(0,33,71)]
biome2 = [(255,250,250),(252,220,235),(244,194,194),(255,105,97),(255,92,92),(255,28,0),(255,8,0),(255,0,0),(205,92,92),(227,66,52),(215,59,62),(206,22,32),(204,0,0),(178,34,34),(179,27,27),(164,0,0),(128,0,0),(112,28,28),(60,20,20),(50,20,20), (112,28,28),(60,20,20),(50,20,20),(60,20,20),(50,20,20)]
biome3 = [(255,245,238),(247,231,206),(255,229,180),(245,222,179),(250,214,165),(251,206,177),(237,201,175),(255,179,71),(222,184,135),(255,168,18),(255,167,0),(229,170,112),(225,169,95),(227,168,87),(195,176,145),(255,140,0),(228,155,15),(237,145,33),(255,127,0),(242,133,0),(237,135,45),(255,117,24),(193,154,107),(255,103,0),(205,127,50),(204,119,34),(210,105,30),(184,115,51),(160,120,90),(204,85,0),(138,121,93),(153,101,21),(131,105,83),(130,102,68),(150,75,0),(123,63,0),(112,66,20),(101,67,33),(72,60,50),(61,43,31)]
movex = 50
movey = 60




while (1):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    color = (255, 255, 255)
    screen.fill(color)
    pygame.display.set_caption('Evolv.io')

    x, y = 0, 0
    counteri = 0
    counterj = 0
    up  = 0
    for i in terrain:
        counteri += 1
        counterj = 0
        x=0
        for j in i:
            if 0<=(counteri)<size and 0<=(counterj)<size:
               
                b = biomea[counteri][counterj]
                if b==0:
                    if 0<=(counteri+1)<size and 0<=(counterj+1)<size and 0<=(counteri-1)<size and 0<=(counterj-1)<size:
                        b = most_frequent([biomea[counteri+1][counterj+1], biomea[counteri+1][counterj-1],  biomea[counteri-1][counterj+1],  biomea[counteri-1][counterj-1]])
                        biomea[counteri][counterj] = b
                    
                    
                b = 1

                if b == 1:
                    pygame.draw.rect(screen, biome1[j],  pygame.Rect(x, y, 2,2))
                if b == 2:
                    pygame.draw.rect(screen, biome2[j],  pygame.Rect(x, y, 2,2))
                if b == 3:
                    pygame.draw.rect(screen, biome1[j],  pygame.Rect(x, y, 2,2))
                counterj +=1
            x+=2
        y+=2
    
    pygame.draw.circle(screen, (255, 0, 255), (movex + random.randint(-2,1), movey + random.randint(-1,1)),1)

        
    pygame.display.flip()


'''


"""Colors = ["#FAFAFA","#F7F7F7","#F5F5F5","#F2F2F2","#F0F0F0","#EDEDED","#EBEBEB","#E8E8E8","#E5E5E5","#E3E3E3","#E0E0E0","#DEDEDE","#DBDBDB","#D9D9D9","#D6D6D6","#D4D4D4","#D1D1D1","#CFCFCF","#CCCCCC","#C9C9C9","#C7C7C7","#C4C4C4","#C2C2C2","#BFBFBF","#BDBDBD","#BABABA","#B8B8B8","#B5B5B5","#B3B3B3","#B0B0B0","#ADADAD","#ABABAB","#A8A8A8","#A6A6A6","#A3A3A3","#A1A1A1","#9E9E9E","#9C9C9C","#999999","#969696","#949494","#919191","#8F8F8F","#8C8C8C","#8A8A8A","#878787","#858585","#828282","#7F7F7F","#7D7D7D","#7A7A7A","#787878","#757575","#737373","#707070","#6E6E6E","#6B6B6B","#696969","#666666","#636363","#616161","#5E5E5E","#5C5C5C","#595959","#575757","#545454","#525252","#4F4F4F","#4D4D4D","#4A4A4A","#474747","#454545","#424242","#404040","#3D3D3D","#3B3B3B","#383838","#333333","#303030","#2E2E2E","#2B2B2B","#292929","#262626","#242424","#212121","#1F1F1F","#1C1C1C","#1A1A1A","#171717","#141414","#121212","#0F0F0F","#0D0D0D","#0A0A0A","#080808","#050505","#030303","#080808","#050505","#030303"]
for j in Colors:
    h = j.lstrip('#')
    print(tuple(int(h[i:i+2], 16) for i in (0, 2, 4)))"""