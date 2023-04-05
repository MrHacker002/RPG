import pygame
import time
import os
from menu import *
pygame.init()

sc = pygame.display.set_mode((0,0), pygame.FULLSCREEN)
clock = pygame.time.Clock()

#variables
sc_w = sc.get_width()
sc_h = sc.get_height()
fps = 60
game = True
block_x = 0
block_y = 0
BLACK = (0,0,0)
#--------------------------------------
path_img = os.path.join(os.path.abspath(__file__+'\..'), "assets")
#game assets
dirt_img = pygame.image.load("grass2.png")
player_img = pygame.image.load("player.png")
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
    def movement(self, mouse_pos_x, mouse_pos_y):
        keys_input = pygame.key.get_pressed()
        if keys_input[pygame.K_w] and self.rect.top > 0:
            self.rect.y += self.speed * -1
        if keys_input[pygame.K_s] and self.rect.bottom < world_map_h-sc_h:
            self.rect.y += self.speed
        if keys_input[pygame.K_d] and self.rect.right < world_map_w-sc_w:
            self.rect.x += self.speed
        if keys_input[pygame.K_a] and self.rect.left > 0:
            self.rect.x += self.speed*-1
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
                self.speed_y = self.dist_y//self.frames
            if self.dist_y > self.dist_x:
                self.speed_y = self.speed
                self.frames = self.dist_y//self.speed
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
class Area:
    def __init__(self,x,y,wydth, height,color):
        self.color=color
        self.rect = pygame.Rect(x,y, wydth, height)
    def set_color(self,new_color):
        self.color=new_color
    def draw(self):
        pygame.draw.rect(sc, self.color, self.rect)

class Label(Area):
    def set_text(self,text, text_size,text_color):
        font = pygame.font.SysFont('verdana', text_size)
        self.image=font.render(text,True,text_color)
    def draw_label(self, shift_x, shift_y):
        self.shift_x = shift_x
        self.shift_y = shift_y
        sc.blit(self.image, (self.rect.x + shift_x, self.rect.y + shift_y))


#--------------------------------------
#Создание экземпляров классов
button1 = Button(760, 100, 300, 50,(255,0,0),(0,255,0), "Почати нову гру", 30, (0,0,0))
button2 = Button(760, 300, 300, 50,(255,0,0),(0,255,0), "Загрузити гру", 30, (0,0,0))
button3 = Button(760, 500, 300, 50,(255,0,0),(0,255,0), "Налаштування",30,(0,0,0))
camera = Camera(0,0)
global hero
hero = Player(800, 400, 100, 100, player_img, 15)
#Создаем список

pictures = []




# Создание карты
tileSize = 100
world_map = [["d" for x in range(90)] for y in range(90)]
world_map_w = len(world_map[0])*tileSize
world_map_h = len(world_map)*tileSize

mouse_pos_x = 0
mouse_pos_y = 0

def menu1(window, clock, FPS):
    global game
    menu = True
    while menu:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                game = False
            if button1.is_clicked(event):
                menu=False
                return menu
            button1.is_focused(event)
            button2.is_focused(event)
            button3.is_focused(event)

        button1.draw()
        button2.draw()
        button3.draw()
        pygame.display.update()
        clock.tick(FPS)
button4 = Button(300, 700, 200, 50,(255,0,0),(0,255,0), "Людина", 25, (0,0,0))
button5 = Button(700, 700, 200, 50,(255,0,0),(0,255,0), "Темний ельф", 25, (0,0,0))
button6 = Button(1100, 700, 200, 50,(255,0,0),(0,255,0), "Орк", 25, (0,0,0))
button7 = Button(1500, 700, 200, 50,(255,0,0),(0,255,0), "Лісний ельф", 25, (0,0,0))
def hero_choose(window, clock, FPS):
    sc.fill(BLACK)
    hero_choose1 = True
    x_pict = 350
    for i in range(4):
        picture = GameSprite(x_pict, 300,100,100,player_img)
        pictures.append(picture)
        x_pict+=400
    while hero_choose1:

        button4.draw()
        button5.draw()
        button6.draw()
        button7.draw()
        for i in pictures:
            i.draw()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                game = False
            elif button4.is_clicked(event):
                hero.race = 'human'
                hero_choose1=False
                return hero_choose1
            elif button5.is_clicked(event):
                hero.race = 'dark_elf'
                hero_choose1=False
                return hero_choose1
            elif button6.is_clicked(event):
                hero.race = 'ogre'
                hero_choose1=False
                return hero_choose1
            elif button7.is_clicked(event):
                hero.race = 'wood_elf'
                hero_choose1=False
                return hero_choose1
            button4.is_focused(event)
            button5.is_focused(event)
            button6.is_focused(event)
            button7.is_focused(event)
        pygame.display.update()
        clock.tick(FPS)
#game = True
menu1(sc,clock,FPS)
hero_choose(sc,clock,FPS)


                

game = True
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
            x+=1
        y+= 1
    camera.movement(mouse_pos_x, mouse_pos_y)
    hero.draw()
    hero.move(mouse_pos_x, mouse_pos_y)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            game = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            print(hero.is_moving)
            if event.button == 3:
                mouse_pos_x, mouse_pos_y = event.pos
                hero.is_moving = True
    pygame.display.update()
    clock.tick(fps)
    # print(clock.get_fps())