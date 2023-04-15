import pygame
import time
import random
import os
from classes import *
from settings import *
from assets import path_img
from map import *

pygame.init()

#--------------------------------------
sc = pygame.display.set_mode((sc_w, sc_h))
pygame.display.set_caption("The Chronicles of Eldrivar")
clock = pygame.time.Clock()

map_tile_img = pygame.image.load_extended(os.path.join(path_img, "map_tile_img.png")).convert_alpha()
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
hero = Player(800, 400, 100, 100, player_img, sc, 10, 20, 20)
enemy = Enemy(200,200,100,100,enemy_img,sc,5,20,hero)
#------------------------------------
menu1(sc,clock,fps, button1, button2, button3)
hero_choose(sc,clock,fps, button4, button5, button6, button7, hero)

#Цикл игры
while game:
    sc.fill(BLACK)
    sc.blit(map_tile_img, (camera.rect.x*-1,camera.rect.y*-1))
    hero.draw()
    enemy.draw()
    map_drawing(plant_map, tileSize, camera, sc_w, sc_h, sc)
    hero.move(camera.mouse_x, camera.mouse_y)
    enemy.movement()
    hero.health(sc)
    camera.movement(hero,enemy)
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game = False
            pygame.quit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 3:
                mouse_pos_x, mouse_pos_y = event.pos
                camera.new_mouse_pos(mouse_pos_x, mouse_pos_y)
                hero.is_moving = True
    clock.tick()