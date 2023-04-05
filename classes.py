import pygame
import os
from map import *
from assets import player_img


class GameSprite(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height, image, sc):
        super().__init__()
        self.image = pygame.transform.scale(image, (width, height))
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = x, y
        self.sc = sc
    def draw(self):
        self.sc.blit(self.image, (self.rect.x, self.rect.y))
    # def draw_sur(self,surface):
    #     surface.blit(self.image, (self.rect.x, self.rect.y))

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
            mouse_pos_y += self.speed * -1
        if keys_input[pygame.K_d] and self.rect.right < world_map_w-sc_w:
            self.rect.x += self.speed
            player.rect.x += self.speed * -1
            mouse_pos_x += self.speed
        if keys_input[pygame.K_a] and self.rect.left > 0:
            self.rect.x += self.speed*-1
            player.rect.x += self.speed
            # mouse_pos_x += self.speed * -1

class Player(GameSprite):
    def __init__(self, x, y, width, height, image,sc, speed):
        super().__init__(x, y, width, height, image, sc)
        self.speed = speed
        self.speed_x = 0
        self.speed_y = 0
        self.is_moving = False
        self.dist_x = 0
        self.dist_y = 0
        self.frames = 0
        self.race = None
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

class Inventory:
    pass
            
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

class Button:
    def __init__(self, x, y, w, h,color1, color2, text, size, text_color, sc):
        self.rect = pygame.Rect(x,y,w,h) 
        #цвет кнопки на которую не навели мышкой
        self.color1 = color1
        #цвет кнопки когда на нее навели
        self.color2 = color2
        #текст на кнопке
        self.text = text
        #текущий цвет
        self.color = color1
        font1 = pygame.font.SysFont("Verdana", size)
        self.lable = font1.render(self.text, True, text_color)
        self.sc = sc
    def set_color(self,new_color):   
        self.color = new_color
    def draw(self):
        pygame.draw.rect(self.sc,self.color, self.rect)
        self.sc.blit(self.lable,(self.rect.x+20,self.rect.y))
    def is_clicked(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            x, y = event.pos
            if self.rect.collidepoint(x,y):
                return True
    def is_focused(self, event):
        if event.type == pygame.MOUSEMOTION:
            x, y = event.pos
            if self.rect.collidepoint(x,y):
                self.set_color(self.color2)
            else:
                self.set_color(self.color1)

def menu1(window, clock, FPS, button1, button2, button3):
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
        clock.tick()

pictures = []
def hero_choose(window, clock, FPS, button4, button5, button6, button7, hero):
    window.fill((0, 0, 0))
    hero_choose1 = True
    x_pict = 60
    for i in range(3):
        picture = GameSprite(x_pict, 300,100,100,player_img, window)
        pictures.append(picture)
        x_pict+=240
    picture = GameSprite(820, 300,100,100,player_img, window)
    pictures.append(picture)
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
        clock.tick()