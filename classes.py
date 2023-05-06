import pygame
import os
from map import *
from assets import *
import math

items = []

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
        self.mouse_x = 0
        self.mouse_y = 0
    def movement(self,player, items, enemys):
        keys_input = pygame.key.get_pressed()
        if keys_input[pygame.K_w] and self.rect.top > 0:
            self.rect.y += self.speed * -1
            player.rect.y += self.speed
            self.mouse_y += self.speed
            for enemy in enemys:
                enemy.rect.y += self.speed
            for item in items:
                item.rect.y += self.speed
        if keys_input[pygame.K_s] and self.rect.bottom < world_map_h-sc_h:
            self.rect.y += self.speed
            player.rect.y += self.speed * -1
            self.mouse_y += self.speed * -1
            for enemy in enemys:
                enemy.rect.y += self.speed * -1
            for item in items:
                item.rect.y += self.speed * -1
        if keys_input[pygame.K_d] and self.rect.right < world_map_w-sc_w:
            self.rect.x += self.speed
            player.rect.x += self.speed * -1
            self.mouse_x += self.speed * -1
            for enemy in enemys:
                enemy.rect.x += self.speed * -1
            for item in items:
                item.rect.x += self.speed * -1
        if keys_input[pygame.K_a] and self.rect.left > 0:
            self.rect.x += self.speed*-1
            player.rect.x += self.speed
            self.mouse_x += self.speed
            for enemy in enemys:
                enemy.rect.x += self.speed
            for item in items:
                item.rect.x += self.speed
    def new_mouse_pos(self, new_mouse_x,new_mouse_y):
        self.mouse_x = new_mouse_x
        self.mouse_y = new_mouse_y

class Player(GameSprite):
    def __init__(self, x, y, width, height, image,sc, speed, hp):
        super().__init__(x, y, width, height, image, sc)
        self.speed = speed
        self.speed_x = 0
        self.speed_y = 0
        self.is_moving = False
        self.dist_x = 0
        self.dist_y = 0
        self.frames = 0
        self.race = None
        self.hp = hp
        self.max_hp = hp
    def move(self, mouse_pos_x, mouse_pos_y):
        if self.is_moving:
            self.dist_x = abs(mouse_pos_x - self.rect.x)
            self.dist_y = abs(mouse_pos_y - self.rect.y)
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
    def health(self,sc):
        amount_half_hearts = self.hp/2
        half_heart_exists = amount_half_hearts - int(amount_half_hearts) != 0
        for heart in range(int(self.max_hp/2)):
            if int(amount_half_hearts) > heart:
                sc.blit(pygame.transform.scale(heart_img, (40,40)), (590+heart*40,0))
            elif half_heart_exists and int(amount_half_hearts) == heart and self.hp >= 0:
                sc.blit(pygame.transform.scale(heart2_img, (40,40)), (590+heart*40,0))
            else:
                sc.blit(pygame.transform.scale(heart3_img, (40,40)), (590+heart*40,0))

class Inventory:
    def __init__(self, x, y, width, height, sc):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.sc = sc
        self.color1 = (130, 130, 130)
        self.color2 = (200, 200, 200)
        self.hotbar_list = []
        self.inventory_list = []
        self.is_inv_open = False

    def create_inventory(self):
        x = self.x
        for e in range(10):
            frame = Frame(x, self.y, self.width, self.height, self.color1, self.sc)
            self.hotbar_list.append(frame)
            self.inventory_list.append(frame)
            x += 35
        self.y += 40
        for i in range(4):
            x = self.x
            for y in range(10):
                frame = Frame(x, self.y, self.width, self.height, self.color1, self.sc)
                self.inventory_list.append(frame)
                x += 35
            self.y += 35
    def draw(self):
        if self.is_inv_open == True:
            for frame in self.inventory_list:
                frame.draw()
        else:
            for frame in self.hotbar_list:
                frame.draw()
    def slot_choose(self):
        if not(self.is_inv_open):
            keys = pygame.key.get_pressed()
            if keys[pygame.K_1]:
                for frame in self.hotbar_list:
                    frame.set_color(self.color1)
                    frame.active = False
                self.hotbar_list[0].set_color(self.color2)
                self.hotbar_list[0].active = True
            if keys[pygame.K_2]:
                for frame in self.hotbar_list:
                    frame.set_color(self.color1)
                    frame.active = False
                self.hotbar_list[1].set_color(self.color2)
                self.hotbar_list[1].active = True
            if keys[pygame.K_3]:
                for frame in self.hotbar_list:
                    frame.set_color(self.color1)
                    frame.active = False
                self.hotbar_list[2].set_color(self.color2)
                self.hotbar_list[2].active = True
            if keys[pygame.K_4]:
                for frame in self.hotbar_list:
                    frame.set_color(self.color1)
                    frame.active = False
                self.hotbar_list[3].set_color(self.color2)
                self.hotbar_list[3].active = True
            if keys[pygame.K_5]:
                for frame in self.hotbar_list:
                    frame.set_color(self.color1)
                    frame.active = False
                self.hotbar_list[4].set_color(self.color2)
                self.hotbar_list[4].active = True
            if keys[pygame.K_6]:
                for frame in self.hotbar_list:
                    frame.set_color(self.color1)
                    frame.active = False
                self.hotbar_list[5].set_color(self.color2)
                self.hotbar_list[5].active = True
            if keys[pygame.K_7]:
                for frame in self.hotbar_list:
                    frame.set_color(self.color1)
                    frame.active = False
                self.hotbar_list[6].set_color(self.color2)
                self.hotbar_list[6].active = True
            if keys[pygame.K_8]:
                for frame in self.hotbar_list:
                    frame.set_color(self.color1)
                    frame.active = False
                self.hotbar_list[7].set_color(self.color2)
                self.hotbar_list[7].active = True
            if keys[pygame.K_9]:
                for frame in self.hotbar_list:
                    frame.set_color(self.color1)
                    frame.active = False
                self.hotbar_list[8].set_color(self.color2)
                self.hotbar_list[8].active = True
            if keys[pygame.K_0]:
                for frame in self.hotbar_list:
                    frame.set_color(self.color1)
                    frame.active = False
                self.hotbar_list[9].set_color(self.color2)
                self.hotbar_list[9].active = True

class Enemy(GameSprite):
    def __init__(self, x, y, width, height, image, sc, speed, hp, player):
        super().__init__(x,y,width,height,image,sc)
        self.speed = speed
        self.hp = hp
        self.max_hp = self.hp
        self.player = player

    def movement(self):
        dist_x = self.player.rect.x - self.rect.x
        dist_y = self.player.rect.y - self.rect.y
        distance = (dist_x**2 + dist_y**2) **0.5
        if distance != 0:
            if (dist_x > 3 and dist_x <= 500) and (dist_y > 3 and dist_y <= 500):
                self.rect.x += self.speed * dist_x / distance
                self.rect.y += self.speed * dist_y / distance
            if (dist_x < 3 and dist_x >= -500) and (dist_y < 3 and dist_y >= -500):
                self.rect.x += int(self.speed * dist_x / distance)
                self.rect.y += int(self.speed * dist_y / distance)
            if (dist_x > 3 and dist_x <= 500) and (dist_y < 3 and dist_y >= -500):
                self.rect.x += self.speed * dist_x / distance
                self.rect.y += self.speed * dist_y / distance
            if (dist_x < 3 and dist_x >= -500) and (dist_y > 3 and dist_y <= 500):
                self.rect.x += self.speed * dist_x / distance
                self.rect.y += self.speed * dist_y / distance

class Area:
    def __init__(self,x,y,width, height,color, sc):
        self.color=color
        self.rect = pygame.Rect(x,y, width, height)
        self.sc = sc
    def set_color(self,new_color):
        self.color=new_color
    def draw(self):
        pygame.draw.rect(self.sc, self.color, self.rect)

class Frame(Area):
    def __init__(self,x,y,width, height,color, sc):
        super().__init__(x,y,width, height,color, sc)
        self.taken = False
        self.active = False

class Item(GameSprite):
    def __init__(self,x,y,width,height,image,sc, stackable, stack_quantity):
        super().__init__(x,y,width,height,image,sc)
        self.frame_owner = None
        self.stackable = stackable
        self.stack_quantity = stack_quantity
        self.is_replacing = False
        self.shift_x = 0
        self.shift_y = 0
    def move(self):
        pass
    def take(self, player, inventory):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_e] and abs(player.rect.x - self.rect.x) < 100 and abs(player.rect.y - self.rect.y) < 100:
            for frame in inventory.inventory_list:
                if frame.taken:
                    for item in items:
                        if item.frame_owner == inventory.inventory_list.index(frame) and item.stackable and item.stack_quantity <= 99-self.stack_quantity:
                            item.stack_quantity += self.stack_quantity
                            break
                else:
                    self.frame_owner = inventory.inventory_list.index(frame)
                    self.rect.x = frame.rect.x+5
                    self.rect.y = frame.rect.y+5
                    self.rect.width = frame.rect.width-10
                    self.rect.height = frame.rect.height-10
                    self.is_replacing = False
                    print(self.rect.x, self.rect.y, self.rect.width, self.rect.height, self.frame_owner)
                    break

class Weapon(Item):
    def __init__(self,x,y,width,height,image,sc, stackable, stack_quantity, name, damage, speed, range, player):
        super().__init__(x,y,width,height,image,sc, stackable, stack_quantity)
        self.name = name
        self.damage = damage
        self.speed = speed
        self.rollback = self.speed
        self.range = range
        self.player = player
        self.attacking = False

class Sword(Weapon):
    def attack(self, mouse_pos, enemes):
        if self.attacking:
            for enemy in enemys:
                if enemy.rect.collidepoint(mouse_pos):
                    if abs(self.player.rect.x + 50 - enemy.rect.x+50) <= self.range and abs(self.player.rect.y + 50 - enemy.rect.y+50) <= self.range:
                        enemy.hp -= self.damage
            if self.rollback == 0:
                self.attacking = False
            if self.rollback <= 0:
                self.rollback = self.speed 
            else:
                self.rollback -= 0.1



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