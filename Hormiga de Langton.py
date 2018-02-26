import pygame, sys
from pygame.locals import *
import random
from random import randint
import time
from time import sleep
import colorsys
from colorsys import hsv_to_rgb
# set up pygame
cycle_num = 2
cicle = bin(cycle_num)[2:]
pygame.init()
pix_siz = 2
grid_x = 200
grid_y = 200
delay = 0
# pix_siz = input("pix_siz: ")
# grid_x = input("Columnas: ")
# grid_y = input("Filas: ")
# delay = float(input("delay: "))
del_r = delay
width = pix_siz*grid_x
height = pix_siz*grid_y
# set up the window
windowSurface = pygame.display.set_mode((width, height), 0, 32)
pygame.display.set_caption('Hormiga de Langton')

# set up the colors
BLACK = (0, 0, 0)
# WHITE = (255, 255, 255,255)
class ant():
    def __init__(self,pos_x,pos_y,dire,cicle):
        self.x = pos_x
        self.y = pos_y
        self.d = dire
        self.cicle = cicle
        self.step = 0
    def update(self):

        for i in range(len(self.cicle)):
            if windowSurface.get_at((self.x,self.y)) == BLACK:
                pygame.draw.rect(windowSurface,self.cicle[1][1],(self.x,self.y,pix_siz,pix_siz))
                if self.cicle[0][0] == "0":
                    self.d+= 1
                    if self.d > 3:
                        self.d = 0
                    self.move()
                else:
                    self.d-=1
                    if self.d <0:
                        self.d = 3
                    self.move()
                break
            if windowSurface.get_at((self.x,self.y)) == self.cicle[i][1]:
                # windowSurface.set_at((self.x,self.y),self.COLOR)
                try:
                    pygame.draw.rect(windowSurface,self.cicle[i+1][1],(self.x,self.y,pix_siz,pix_siz))
                except IndexError:
                    pygame.draw.rect(windowSurface,self.cicle[0][1],(self.x,self.y,pix_siz,pix_siz))
                if self.cicle[i][0] == "0":
                    self.d+= 1
                    if self.d > 3:
                        self.d = 0
                    self.move()
                else:
                    self.d-=1
                    if self.d <0:
                        self.d = 3
                    self.move()
                break

    def move(self):
        if self.d == 0:
            self.x += pix_siz
            if self.x >width-pix_siz:
                self.x = 0
                self.step = 10000000
        if self.d == 1:
            self.y -= pix_siz
            if self.y <0:
                self.y = height-pix_siz
                self.step = 10000000
        if self.d == 2:
            self.x -=pix_siz
            if self.x <0:
                self.x = width-pix_siz
                self.step = 10000000
        if self.d == 3:
            self.y+=pix_siz
            if self.y >height-pix_siz:
                self.y = 0
                self.step = 1000000

windowSurface.fill(BLACK)
color_inc = 1.0/(len(cicle))
# draw the window onto the screen

cicle_l = []
for l in range(len(cicle)):
    color_len = l*color_inc
    color_rgb = hsv_to_rgb(color_len,1.0,0.9)
    cicle_l.append([cicle[l],(color_rgb[0]*255,color_rgb[1]*255,color_rgb[2]*255)])
    # pob.append(ant(0,0,0,BLACK))
a = ant(width//2,height//2,1,cicle_l)
# run the game loop

while True:
    a.update()
    pygame.display.update()
    a.step+=1
    if a.step > 100000:
        cicle_l = []
        step = 0
        pygame.image.save(windowSurface,"codes/"+cicle+" - "+str(cycle_num)+".jpg")
        while True:
            cycle_num+=1
            cicle = bin(cycle_num)[2:]
            if cicle.count("1") == 0 or cicle.count("0") == 0:
                pass
            else:
                break
        color_inc = 1.0/(len(cicle))
        windowSurface.fill(BLACK)
        for l in range(len(cicle)):
            color_len = l*color_inc
            color_rgb = hsv_to_rgb(color_len,1.0,0.9)
            cicle_l.append([cicle[l],(color_rgb[0]*255,color_rgb[1]*255,color_rgb[2]*255)])
            # pob.append(ant(0,0,0,BLACK))
        a = ant(width//2,height//2,1,cicle_l)

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    keys=pygame.key.get_pressed()
    if keys[K_DOWN]:
        del_r = delay
    if keys[K_UP]:
        del_r = 0
    sleep(del_r)
