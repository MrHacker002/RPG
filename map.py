import pygame
import time
import random
import os
from tilemap import plant_map

pygame.init()

#variables
sc_w = 1000
sc_h = 800
fps = 60
game = True
block_x = 0
block_y = 0
BLACK = (0,0,0)
#--------------------------------------

sc = pygame.display.set_mode((sc_w, sc_h))
clock = pygame.time.Clock()

path_img = os.path.join(os.path.abspath(__file__+'\..'), "assets")
#game assets
dirt_img = pygame.image.load(os.path.join(path_img, "dirt.png"))
grass_img = pygame.image.load(os.path.join(path_img, "grass2.png"))
player_img = pygame.image.load(os.path.join(path_img, "player.png"))
tree_img = pygame.image.load(os.path.join(path_img, "tree.png"))
#-------------------------------------
#classes
class GameSprite(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height, image):
        super().__init__()
        self.image = pygame.transform.scale(image, (width, height))
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = x, y
    def draw(self):
        sc.blit(self.image, (self.rect.x, self.rect.y))
    def draw_sur(self,surface):
        surface.blit(self.image, (self.rect.x, self.rect.y))

class Camera():
    def __init__(self,x,y):
        self.speed = 15
        self.rect = pygame.Rect(x,y,0,0)
    def movement(self, mouse_pos_x, mouse_pos_y, player):
        keys_input = pygame.key.get_pressed()
        if keys_input[pygame.K_w] and self.rect.top > 0:
            self.rect.y += self.speed * -1
            player.rect.y += self.speed
            # mouse_pos_y += self.speed * -1
        if keys_input[pygame.K_s] and self.rect.bottom < world_map_h-sc_h:
            self.rect.y += self.speed
            player.rect.y += self.speed * -1
            mouse_pos_y += self.speed
        if keys_input[pygame.K_d] and self.rect.right < world_map_w-sc_w:
            self.rect.x += self.speed
            player.rect.x += self.speed * -1
            mouse_pos_x += self.speed
        if keys_input[pygame.K_a] and self.rect.left > 0:
            self.rect.x += self.speed*-1
            player.rect.x += self.speed
            # mouse_pos_x += self.speed * -1
        return mouse_pos_x, mouse_pos_y
class Player(GameSprite):
    def __init__(self, x, y, width, height, image, speed):
        super().__init__(x, y, width, height, image)
        self.speed = speed
        self.speed_x = 0
        self.speed_y = 0
        self.is_moving = False
        self.dist_x = 0
        self.dist_y = 0
        self.frames = 0
    def move(self, mouse_pos_x, mouse_pos_y):
        if self.is_moving:
            if self.rect.x < mouse_pos_x:
                self.dist_x = mouse_pos_x - self.rect.x
            if self.rect.x > mouse_pos_x:
                self.dist_x = self.rect.x - mouse_pos_x
            if self.rect.y < mouse_pos_y:
                self.dist_y = mouse_pos_y - self.rect.y
            if self.rect.y > mouse_pos_y:
                self.dist_y = self.rect.y - mouse_pos_y
            if self.dist_x > self.dist_y:
                self.speed_x = self.speed
                self.frames = self.dist_x//self.speed
                if self.frames != 0:
                    self.speed_y = self.dist_y//self.frames
            if self.dist_y > self.dist_x:
                self.speed_y = self.speed
                self.frames = self.dist_y//self.speed
                if self.frames != 0:
                    self.speed_x = self.dist_x//self.frames
            if self.rect.x < mouse_pos_x:
                self.rect.x += self.speed_x
            else:
                self.rect.x -= self.speed_x
            if self.rect.y < mouse_pos_y:
                self.rect.y += self.speed_y
            else:
                self.rect.y -= self.speed_y
            self.frames -= 1
            if self.frames == 0:
                self.is_moving = False
        else:
            self.dist_x = 0
            self.dist_y = 0
            self.speed_x = 0
            self.speed_y = 0
            

#--------------------------------------
#Создание экземпляров классов
camera = Camera(0,0)
hero = Player(800, 400, 100, 100, player_img, 3)
# Создание карты
tileSize = 100
world_map = [[random.choice(["g", "d"]) for x in range(50)] for y in range(50)]
world_map_w = len(world_map[0])*tileSize
world_map_h = len(world_map)*tileSize

mouse_pos_x = 0
mouse_pos_y = 0
while game:
    sc.fill(BLACK)
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
    hero.draw()
    hero.move(mouse_pos_x, mouse_pos_y)
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
    camera.movement(mouse_pos_x, mouse_pos_y, hero)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            game = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            # print(hero.is_moving)
            if event.button == 3:
                mouse_pos_x, mouse_pos_y = event.pos
                hero.is_moving = True
                print(mouse_pos_x, mouse_pos_y)
    pygame.display.update()
    clock.tick()