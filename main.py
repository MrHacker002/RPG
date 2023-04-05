import pygame
import time
import random
import os
from classes import *
from settings import *
from map import *

pygame.init()

#--------------------------------------
sc = pygame.display.set_mode((sc_w, sc_h))
clock = pygame.time.Clock()
#-------------------------------------
#Создание экземпляров классов
button1 = Button(((sc_w//2)-150), 100, 300, 50,(255,0,0),(0,255,0), "Почати нову гру", 30, (0,0,0), sc)
button2 = Button(((sc_w//2)-150), 300, 300, 50,(255,0,0),(0,255,0), "Загрузити гру", 30, (0,0,0), sc)
button3 = Button(((sc_w//2)-150), 500, 300, 50,(255,0,0),(0,255,0), "Налаштування",30,(0,0,0), sc)
button4 = Button(((sc_w//4)-220), 500, 150, 50,(255,0,0),(0,255,0), "Людина", 25, (0,0,0), sc)
button5 = Button(((sc_w//4)*2-250), 500, 200, 50,(255,0,0),(0,255,0), "Темний ельф", 25, (0,0,0), sc)
button6 = Button(((sc_w//4)*3-220), 500, 150, 50,(255,0,0),(0,255,0), "Орк", 25, (0,0,0), sc)
button7 = Button(((sc_w//4)*4-220), 500, 185, 50,(255,0,0),(0,255,0), "Лісний ельф", 25, (0,0,0), sc)
camera = Camera(0,0)
hero = Player(800, 400, 100, 100, player_img, sc, 3)
#------------------------------------
menu1(sc,clock,fps, button1, button2, button3)
hero_choose(sc,clock,fps, button4, button5, button6, button7, hero)

#Цикл игры
while game:
    sc.fill(BLACK)
    map_drawing(world_map, plant_map, tileSize, camera, sc_w, sc_h, sc)
    hero.draw()
    hero.move(camera.mouse_x, camera.mouse_y)
    camera.movement(hero)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            game = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 3:
                mouse_pos_x, mouse_pos_y = event.pos
                camera.new_mouse_pos(mouse_pos_x, mouse_pos_y)
                hero.is_moving = True
    pygame.display.update()
    clock.tick()