import array
import random
import sys
import pygame
import math
import socket
import numpy as np
import random as r

#initialize pygame
pygame.init()
size = 850
width = int(np.round(size * 1.45))
#sets the screen size
screen = pygame.display.set_mode((width + 200, size))
def map(array, size):
    for i in range(size):
        temp = []
        for j in range(width):
            temp.append(int(np.round((100*(z[i][j]+1))//2)))
        array.append(temp)
    return array

def speciesinit(array, size):
    for i in range(size//10):
        array.append([r.randint(0,size),r.randint(0,size)])
    return array

#2D Perlin Noise With Numpy
def perlin(x,y,seed=0):
    # permutation table
    np.random.seed(seed)
    p = np.arange(256,dtype=int)
    np.random.shuffle(p)
    p = np.stack([p,p]).flatten()
    # coordinates of the top-left
    xi = x.astype(int)
    yi = y.astype(int)
    # internal coordinates
    xf = x - xi
    yf = y - yi
    # fade factors
    u = fade(xf)
    v = fade(yf)
    # noise components
    n00 = gradient(p[p[xi]+yi],xf,yf)
    n01 = gradient(p[p[xi]+yi+1],xf,yf-1)
    n11 = gradient(p[p[xi+1]+yi+1],xf-1,yf-1)
    n10 = gradient(p[p[xi+1]+yi],xf-1,yf)
    # combine noises
    x1 = lerp(n00,n10,u)
    x2 = lerp(n01,n11,u) 
    return lerp(x1,x2,v) 
#linear interpolation
def lerp(a,b,x):
    return a + x * (b-a)
#6t^5 - 15t^4 + 10t^3
def fade(t):  
    return 6 * t**5 - 15 * t**4 + 10 * t**3
#grad converts h to the right gradient vector and return the dot product with (x,y)
def gradient(h,x,y):  
    vectors = np.array([[0,1],[0,-1],[1,0],[-1,0]])
    g = vectors[h%4]
    return g[:,:,0] * x + g[:,:,1] * y

#coloring functions and vars
def hextorgb(hexstring):
    return (tuple(int(Colors[hexstring].lstrip('#')[i:i+2], 16) for i in (0, 2, 4)))
def random_color():
    rgbl=[255,0,0]
    random.shuffle(rgbl)
    return tuple(rgbl)
def colorgenerator(array):
    array = []
    for i in range(1,25, 2):
        array.append(((25 - i)*10, 255, 255))
    for i in range(70):
        array.append((0, 255-(3*i), 255-(2*i)))
    return array
Colors = []
Colors = colorgenerator(Colors)
#initialize species
species = []
species = speciesinit(species, size)

def printText(txtText, Textfont, Textsize , Textx, Texty, Textcolor):
	# pick a font you have and set its size
	myfont = pygame.font.SysFont(Textfont, Textsize)
	# apply it to text on a label
	label = myfont.render(txtText, 1, Textcolor)
	# put the label object on the screen at point Textx, Texty
	screen.blit(label, (Textx, Texty))
	# show the whole thing
	pygame.display.flip()

#initializes terrain
terrain=[]
lin = np.linspace(0,2,width,endpoint=False)
x,y = np.meshgrid(4*lin,4*lin) #lin zoom out multiply
z = perlin(x,y,seed=r.randint(0,1000))
terrain = map(terrain, size)

mini = 100
for i in terrain:
    if min(i) < mini:
        mini = min(i)
print(mini)

day = 0
#pygame updates
while (1):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    pygame.display.set_caption('Evolv.io')
    x, y = 0, 0
    #terrain display
    for i in terrain:
        x=0
        for j in i:
            if 0<=(x)<width and 0<=(y)<size:
                pygame.draw.rect(screen, Colors[j],  pygame.Rect(x, y, 1,1))
            x+=1
        y+=1
    day +=1

    pygame.draw.rect(screen, 0,  pygame.Rect(int(850*1.45) + 10, 0, 200, size))
    printText("Day:" +" "+ str(day), "PROFONT",30, int(850*1.45) + 10, 10, (70,102,255))

    pygame.display.flip()
plt.show()

