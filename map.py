import random
from settings import *
import pygame
import os
import csv
from assets import tree_img, dirt_img, grass_img, rock_img, house_img

world_map = [[0 for x in range(87)] for y in range(87)]
world_map_w = len(world_map[0])*tileSize
world_map_h = len(world_map)*tileSize

house_map = [
    'h...h...h...h',
    '.............',
    '.............',
    '.............',
    '.............',
    'h...h...h...h',
    '.............',
    '.............',
    '.............',
    '.............',
    'h...h...h...h......h...h',
    '.............',
    '.............',
    '.............',
    '.............',
    '.............',
    '.............',
    'h...h...h...h......h...h']
house_array = []
rock_array = []
def read_csv(filename):
    map_tile = []
    with open(filename) as data:
        data = csv.reader(data, delimiter=',')
        for row in data:
            map_tile.append(list(row))
    return map_tile
def rock_drawing(GameSprite,filename,tileSize,camera, sc_w, sc_h, sc):
    map_tile = read_csv(filename)
    y = 0
    for row in map_tile:
        x = 0
        for tile in row:
            if tile == "44":
                rock = GameSprite(x*tileSize, y*tileSize,100,100,rock_img,sc)
                rock_array.append(rock)
            x += 1
        y += 1
def house_drawing(GameSprite,map_img,tileSize,camera, sc_w, sc_h, sc):
    y = 44
    for line in map_img:
        x = 3
        for block in line:
            if block == "h":
                house = GameSprite(x*tileSize,y*tileSize,200,300,house_img,sc)
                house_array.append(house)
            x += 1
        y += 1
        