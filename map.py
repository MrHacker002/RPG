import random
from settings import *
import pygame
import os
from assets import tree_img, dirt_img, grass_img, rock_img

world_map = [[random.choice(["g", "d"]) for x in range(50)] for y in range(50)]
world_map_w = len(world_map[0])*tileSize
world_map_h = len(world_map)*tileSize

# plant_map = [
#     "...................r.........r.......r..........",
#     '....t....r....t..r....t.......t...r...tr........',
#     ".....t....r..t.....t.....t..r....r.t......t.t.t.",
#     '................t.r..........t..........t.....t.',
#     'r....r..t.t.t....r....t.r...t...r.t.r.t..t..t...',
#     '.t.r..t..t.t.t.t...r.....r..t.....tr...t.....t..',
#     '.....r..t..t..t.tr..t....r...t..r...r..t....t...',
#     '....t.........t.r.....t.r.....t.r.....tr...r....',
#     ".....t.......t.....t.....t.........t......t.t.t.",
#     '........r...r...t.....r...r..t...r....r.t.....t.',
#     '....r...t..t......r..t..r...t.....t...t..t..t...',
#     '.t..r.t..t...t.t....r.......t.....t....t.....t..',
#     '........t..t..t.tr..t.....r..t..r......t....t...',
#     '....t.........t.......t.......t.......t.........',
#     ".....t.......t.....tr....t...r...r..t.r....t.t.t",
#     '...r...r...r....t............t......r...t.....t.',
#     '........t.r....r..t.....t..r..t...t..t..t....r..',
#     '.t....t..t.t.t.....r......t.....t....t.....t....',
#     '.....r..t..t...t...t....r...t.......r.t....t....',
#     '....t.....r...t.......t...r...t.......tr........',
#     ".....t.......t.....t.....t.........t......t.t.t.",
#     '.............r..t............t..........t.....t.',
#     '........t.t.t.........t.....t.....t...t..t..t...',
#     '.t....t..t...r....r...t.....t....t.....t........',
#     '........t...t.t...t...r....t...r.....t....t.....',
#     '....t.........t.......t.......t.......t.........',
#     ".....t...r...t.....t.....t.....r...t......t.t.t.",
#     '...........r....t....r.......t..........t.....t.',
#     '.......t.........t.....t.....t...t..t..t........',
#     '.t....t..t.t.t............t.....t....t.....t....',
#     '........t..t..t.t...t..r..r.........t....t......',
#     '....t.....r...t....r..t.......t..r....t.........',
#     ".....t....r..t..r..t.....t....r....t......t.t.t.",
#     '....r...........t.r....r.....t.....r....t.....t.',
#     '.....r..t.t.t..r......t.....t...r.t...t..t..t...',
#     '.t.t.t......r.....t.....t....t.r...t....r.r.....',
#     '........t...t...r....t...r.....t....t.......r...',
#     '....t.........t.......t.......t.......t..r......',
#     ".....t..rr...t.....t.....t...r.....t...r...t.t.t.",
#     '..r...r.........t............t..........t.....t.',
#     '........t.t.t.........t.....t.....t...t..t..t...',
#     '.t....t...r...r.....t.....t....t.....t..........',
#     '..........t........t.....r...t....t...r....r....',
#     '....r......t...r............t......r.......t....',
#     '........t...t........t.........t.r..t...........',
#     '....t.........t.......t...r...t.......t.....r...',
#     ".....t.......t.....t.....t......r..t......t.t.t.",
#     '................t....r....r..t..r..r....t.....t.',
#     '........t.t.t...r.....t.....t.....t.r.t..t..t...',
#     '.t....t.............t.....t....t.....t.r........',
#     '..........t.....r..t.........t....t..r..........',
#     '..............r........r...........r............'
# ]

plant_map = [
    '..................................................',
    '....t..t...t...t..t...t.t...t..r...t.....t......r.',
    'xxxxxxxx...t..tr.t..r.t.r...t..r.t.r....t...t.....',
    'xxxxxxxx..t...t...t..r...t.r..t.....t.....t.r.t...',
    'xxxxxrxxxxxx....t...r.t..r..t....t.r.....t..t.t...',
    'xxxxxxrxxxxxxxx.r..t.r...t...t.......tr......r....',
    'xxxxxxxxxxxxxxxx...t..t..t.t.....t..t...r..t..t...',
    '.r...t.xxxxxxrxxxt..t.xxxrxxxxt..t....t..r...t..t.',
    '...t..r.txxxxxxxxxxxxxxxxxxrxxxxx...t...t.....t...',
    '.t...t.t..xxxxxxxxxxrxxxrxxxxxrxxxxx..r....t......',
    '..t...t..t.xxxxrxxxxxxxxxxxxxxxxxxxxx..t....t..t..',
    't.t.t...t...xxxxxxxxxxx.t.t.xxrxxxxxxx....r..t....',
    '.t.r..t...t.xxxxxxxrxt.t....txxxxxxrxxx.t.t.t.....',
    '..t.t...t..r.xxxxrxxrt.t..t..txxxxxxxxxx...r...t..',
    '...t...t...t.xxxrrrxxx.t.t..t...xxrxxxxxx.t.......',
    '.t.r...t.....txxxrxxxxxxxt.t..t.txxxxxxrx...t.....',
    '.....t....t...xxx.xxrxxxrxt..t....txxxxxxx.....t..',
    '...t..tr...txxxxxt.xxxxxxx.t.t.t..txxrxxxxxt......',
    '..t..t.tr.t.xxxrxt.xxxrxxxrt.r..t..xxxxrxxxx.t....',
    '.....t..t...xxxxx.t.xxxxxxrxt.t.t..txxxxxxxxxxxxx.',
    '.t...t...t.xxxxxx..t.xxxxxxxx..t.t..xxxxxrxxxxxxxx',
    '...t...t.r.xxxxrx.t...xxxxxxxxt.r.t...txxxxxxxxxxx',
    '.t...t....txxxxxx.tr.txxxrxxxx.t.tr.t..xxxxxxxxxxx',
    '.r..t..r.txxxxrxx..t.t.xxxxxxxx.t..t..t..txxxxxxxx',
    '....r..t.xxxxxxxx......xxxxxxrxt..t.r.t..r..xrxxxx',
    '..t....xxxxxrxxxx.t.r.t.xxxxxxxxt...t.r..t..t..t..',
    'xxxxxxxxxxxxxxxxxx..t...xxxxxxxxt.t.r..t....t.....',
    'xxxrxxxxxxrrxxxxxx.t...txxxxxxxrx...t...t.t..t.t..',
    'xxxxrxxxxxrxrrxxxxx..t..rxxxxxxxxxt...t...t...t...',
    'xxxxxxxxxxxxxxxxxxxx.t..txxxxxxrxxx.t...t..t...t..',
    'xx..t.xxxxxxxxxxxxxx..t...xxxxxxxxxx.t.......t....',
    '.....t....txrxt.xxxxx.t..txxxxrxxxxxxxxt...t..t...',
    '.t.....t...xxx..xxxxxx..t..xxxxxxxxxxxxx.t.....t..',
    '..r.t.....txxxx.txxxxxx..t.rtxxxxxxxxxxxxx.t.t.t..',
    '.....t..t...xxx..xxrxxx.t.t...xxxrxxxxxxxxxxxt....',
    '..t...t....txxxx.txxxxxx.tr.t.t.xxxxxrxxxrxxxxt...',
    '....t...t...xxrx..txxxrxx..rt.t..xxxxxxxrxxxxxx.t.',
    '..r...t...r.txxxx..xxxxxxx.t.rt..t..xxrxxxxxxxxx..',
    '...t...t.....xxxx..txxxxxxx.t...t..t.txxxxxxxxxxt.',
    '.tr..t.r...t..xxxt..txrxxxxx...t..t....xxxxxxxxx..',
    '...t....t.t...xxxx.t..xxxrxxx..tt..t.t..txxxxxxxx.',
    '..t.r..t..r...xxrx...t.xxxxxxxx....t..t....xxxxxx.',
    '.....t...t..t.xxxxt.....trxxxxxx..t..t.t.t..xxxxx.',
    '.tr...t...t..t.xxxxt..t...xxxxxxx...t..t.....xxxxt',
    '...t.t..t.r.t..xxxx........xxxxxx.....t...t.xxxxx.',
    '.t..tr.t..t...t.xxxt.t.t..t.rxxxxx..t...t...xxxxxt',
    '.r..t..t..t.t...xxx...t.t.....xxxxx...t...txxxxx..',
    '..t....t....t..xxxxt..t..t..t..xrxx.t..t..xxxxxx..',
    '.....t...t.....xxxx..t....t....xxxx..t...txxxxx.t.',
    '..t....t.t.t...xxxx..t..t....t..xxx....t..xxxx.t..',
]

def map_drawing(plant_map, tileSize, camera, sc_w, sc_h, sc):
    # y = 0
    # for line in world_map:
    #     x = 0
    #     for block in line:
    #         if (x*tileSize+camera.rect.x*-1 <= sc_w+100 and y*tileSize+camera.rect.y*-1 <= sc_h+100):
    #             if (x*tileSize+camera.rect.x*-1 >= 0-tileSize and y*tileSize+camera.rect.y*-1 >= 0-tileSize):
    #                 if block == "d":
    #                     sc.blit(pygame.transform.scale(dirt_img, (tileSize, tileSize)), (x*tileSize+camera.rect.x*-1,y*tileSize+camera.rect.y*-1))
    #                 if block == "g":
    #                     sc.blit(pygame.transform.scale(grass_img, (tileSize, tileSize)), (x*tileSize+camera.rect.x*-1,y*tileSize+camera.rect.y*-1))
    #                     # sc.blit(pygame.transform.scale(grass_img, (tileSize, tileSize)), (x*tileSize+camera.rect.x*-1,y*tileSize+camera.rect.y*-1))
    #         x+=1
    #     y+= 1
    y = 0
    for line in plant_map:
        x = 0
        for block in line:
            if (x*tileSize+camera.rect.x*-1 <= sc_w+tileSize and y*tileSize+camera.rect.y*-1 <= sc_h+tileSize):
                if (x*tileSize+camera.rect.x*-1 >= 0-tileSize and y*tileSize+camera.rect.y*-1 >= 0-tileSize):
                    if block == "t":
                        sc.blit(pygame.transform.scale(tree_img, (100, 200)), (x*tileSize+camera.rect.x*-1,y*tileSize-100+camera.rect.y*-1))
                    if block == "r":
                        sc.blit(pygame.transform.scale(rock_img, (100, 100)), (x*tileSize+camera.rect.x*-1,y*tileSize+camera.rect.y*-1))
            x+=1        
        y+= 1
