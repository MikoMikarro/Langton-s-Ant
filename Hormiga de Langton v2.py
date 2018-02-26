import pygame, sys
from pygame.locals import *
import random
from random import randint
import time
from time import sleep
import colorsys
from colorsys import hsv_to_rgb
# set up pygame
cycle_num = 733

pygame.init()
pix_siz = 1
delay = 0
# pix_siz = input("pix_siz: ")
# grid_x = input("Columnas: ")
# grid_y = input("Filas: ")
# delay = float(input("delay: "))
del_r = delay
# set up the window



# set up the colors
BLACK = (0, 0, 0)
# WHITE = (255, 255, 255,255)
class ant():
    def __init__(self,cicle):
        self.x = 0
        self.y = 0
        self.d = 1
        self.cicle = cicle
        color_inc = 1.0/(len(cicle))
        self.cicle_col = []
        for l in range(len(cicle)):
            color_len = l*color_inc
            color_rgb = hsv_to_rgb(color_len,1.0,0.9)
            self.cicle_col.append((color_rgb[0]*255,color_rgb[1]*255,color_rgb[2]*255))
        self.step = 0
        self.cord = [(self.x,self.y)]
        self.col = [self.cicle_col[0]]
    def update(self):
        if self.d == 0:
            new_x = self.x
            new_y = self.y-1
        if self.d == 1:
            new_x = self.x+1
            new_y = self.y
        if self.d == 2:
            new_x = self.x
            new_y = self.y+1
        if self.d == 3:
            new_x = self.x-1
            new_y = self.y

        if (new_x,new_y) in self.cord:
            pos = self.cord.index((new_x,new_y))
            try:
                self.col[pos] = self.cicle_col[self.cicle_col.index(self.col[pos])+1]
            except:
                self.col[pos] = self.cicle_col[0]
        else:
            self.cord.append((new_x,new_y))
            self.col.append(self.cicle_col[0])
        pos = self.cord.index((new_x,new_y))
        self.x = new_x
        self.y = new_y
        change = self.cicle[self.cicle_col.index(self.col[self.cord.index(self.cord[pos])])]
        if change == "0":
            self.d += 1
            if self.d > 3:
                self.d = 0
        else:
            self.d -=1
            if self.d < 0:
                self.d = 3
        a.step+=1
# color_inc = 1.0/(len(cicle))
# # draw the window onto the screen
#
# cicle_l = []
# for l in range(len(cicle)):
#     color_len = l*color_inc
#     color_rgb = hsv_to_rgb(color_len,1.0,0.9)
#     cicle_l.append([cicle[l],(color_rgb[0]*255,color_rgb[1]*255,color_rgb[2]*255)])
#     # pob.append(ant(0,0,0,BLACK))
a = ant(bin(cycle_num)[2:])
# run the game loop
def draw():
    print a.cicle
    x_cords = []
    y_cords = []
    for i in a.cord:
        x_cords.append(i[0])
        y_cords.append(i[1])
    x_cords.sort()
    y_cords.sort()
    x_max = x_cords[-1]
    x_min = x_cords[0]
    y_max = y_cords[-1]
    y_min = y_cords[0]
    width = x_max-x_min
    height = y_max-y_min
    windowSurface = pygame.Surface((width, height))
    windowSurface.fill(BLACK)
    for i in range(len(a.cord)):
        pygame.draw.rect(windowSurface,a.col[i],(a.cord[i][0]-x_min,a.cord[i][1]-y_min,1,1))
    pygame.image.save(windowSurface, "codes/"+a.cicle+" - "+str(cycle_num)+".bmp")
    a.step = 0
def test():
    x_cords = []
    y_cords = []
    for i in a.cord:
        x_cords.append(i[0])
        y_cords.append(i[1])
    x_cords.sort()
    y_cords.sort()
    x_max = x_cords[-1]
    x_min = x_cords[0]
    y_max = y_cords[-1]
    y_min = y_cords[0]
    width = x_max-x_min
    height = y_max-y_min
    if width > 100 or height > 100 or a.step >50000:
        return True
    else:
        return False
test_step = 0
while True:
    a.update()
    test_step+=1
    if test_step > 1000:
        if test() == True:
            draw()
            while True:
                    cycle_num+=1
                    cicle = bin(cycle_num)[2:]
                    if cicle.count("1") == 0 or cicle.count("0") == 0:
                        pass
                    else:
                        break
            a = ant(cicle)
        test_step = 0
    # if a.step > 100000:
    #     cicle_l = []
    #     step = 0
    #     pygame.image.save(windowSurface,"codes/"+cicle+" - "+str(cycle_num)+".jpg")
    #     while True:
    #         cycle_num+=1
    #         cicle = bin(cycle_num)[2:]
    #         if cicle.count("1") == 0 or cicle.count("0") == 0:
    #             pass
    #         else:
    #             break
    #     color_inc = 1.0/(len(cicle))
    #     windowSurface.fill(BLACK)
    #     for l in range(len(cicle)):
    #         color_len = l*color_inc
    #         color_rgb = hsv_to_rgb(color_len,1.0,0.9)
    #         cicle_l.append([cicle[l],(color_rgb[0]*255,color_rgb[1]*255,color_rgb[2]*255)])
    #         # pob.append(ant(0,0,0,BLACK))
    #     a = ant(width//2,height//2,1,cicle_l)

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
