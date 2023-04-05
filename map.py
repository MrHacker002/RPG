import random
from settings import *
import pygame
import os
from assets import tree_img, dirt_img, grass_img

world_map = [[random.choice(["g", "d"]) for x in range(50)] for y in range(50)]
world_map_w = len(world_map[0])*tileSize
world_map_h = len(world_map)*tileSize

plant_map = [
    "................................................",
    '....t.........t.......t.......t.......t.........',
    ".....t.......t.....t.....t.........t......t.t.t.",
    '................t............t..........t.....t.',
    '........t.t.t.........t.....t.....t...t..t..t...',
    '.t....t..t.t.t.t............t.....t....t.....t..',
    '........t..t..t.t...t........t.........t....t...',
    '....t.........t.......t.......t.......t.........',
    ".....t.......t.....t.....t.........t......t.t.t.",
    '................t............t..........t.....t.',
    '........t..t.........t......t.....t...t..t..t...',
    '.t....t..t...t.t............t.....t....t.....t..',
    '........t..t..t.t...t........t.........t....t...',
    '....t.........t.......t.......t.......t.........',
    ".....t.......t.....t.....t.........t......t.t.t.",
    '................t............t..........t.....t.',
    '........t.........t.....t.....t...t..t..t.......',
    '.t....t..t.t.t............t.....t....t.....t....',
    '........t..t...t...t........t.........t....t....',
    '....t.........t.......t.......t.......t.........',
    ".....t.......t.....t.....t.........t......t.t.t.",
    '................t............t..........t.....t.',
    '........t.t.t.........t.....t.....t...t..t..t...',
    '.t....t..t............t.....t....t.....t........',
    '........t...t.t...t........t.........t....t.....',
    '....t.........t.......t.......t.......t.........',
    ".....t.......t.....t.....t.........t......t.t.t.",
    '................t............t..........t.....t.',
    '.......t.........t.....t.....t...t..t..t........',
    '.t....t..t.t.t............t.....t....t.....t....',
    '........t..t..t.t...t...............t....t......',
    '....t.........t.......t.......t.......t.........',
    ".....t.......t.....t.....t.........t......t.t.t.",
    '................t............t..........t.....t.',
    '........t.t.t.........t.....t.....t...t..t..t...',
    '.t.t.t............t.....t....t.....t............',
    '........t...t........t.........t....t...........',
    '....t.........t.......t.......t.......t.........',
    ".....t.......t.....t.....t.........t......t.t.t.",
    '................t............t..........t.....t.',
    '........t.t.t.........t.....t.....t...t..t..t...',
    '.t....t.............t.....t....t.....t..........',
    '..........t........t.........t....t.............',
    '...........t................t..............t....',
    '........t...t........t.........t....t...........',
    '....t.........t.......t.......t.......t.........',
    ".....t.......t.....t.....t.........t......t.t.t.",
    '................t............t..........t.....t.',
    '........t.t.t.........t.....t.....t...t..t..t...',
    '.t....t.............t.....t....t.....t..........',
    '..........t........t.........t....t.............',
    '................................................'
]

def map_drawing(world_map, plant_map, tileSize, camera, sc_w, sc_h, sc):
    y = 0
    for line in world_map:
        x = 0
        for block in line:
            if (x*tileSize+camera.rect.x*-1 <= sc_w+100 and y*tileSize+camera.rect.y*-1 <= sc_h+100):
                if (x*tileSize+camera.rect.x*-1 >= 0-tileSize and y*tileSize+camera.rect.y*-1 >= 0-tileSize):
                    if block == "d":
                        sc.blit(pygame.transform.scale(dirt_img, (tileSize, tileSize)), (x*tileSize+camera.rect.x*-1,y*tileSize+camera.rect.y*-1))
                    if block == "g":
                        sc.blit(pygame.transform.scale(grass_img, (tileSize, tileSize)), (x*tileSize+camera.rect.x*-1,y*tileSize+camera.rect.y*-1))
            x+=1
        y+= 1
    y = 0
    for line in plant_map:
        x = 0
        for block in line:
            if (x*tileSize+camera.rect.x*-1 <= sc_w+100 and y*tileSize+camera.rect.y*-1 <= sc_h+100):
                if (x*tileSize+camera.rect.x*-1 >= 0-tileSize and y*tileSize+camera.rect.y*-1 >= 0-tileSize):
                    if block == "t":
                        sc.blit(pygame.transform.scale(tree_img, (100, 200)), (x*tileSize+camera.rect.x*-1,y*tileSize-100+camera.rect.y*-1))
            x+=1
        y+= 1
