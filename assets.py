import os
import pygame

path_img = os.path.join(os.path.abspath(__file__+'\..'), "assets")

dirt_img = pygame.image.load(os.path.join(path_img, "dirt.png"))
grass_img = pygame.image.load(os.path.join(path_img, "grass2.png"))
tree_img = pygame.image.load(os.path.join(path_img, "tree.png"))
player_img = pygame.image.load(os.path.join(path_img, "player.png"))
enemy_img = pygame.image.load(os.path.join(path_img, "mushroom_enemy.png"))
rock_img = pygame.image.load(os.path.join(path_img, "rock.png"))
heart_img = pygame.image.load(os.path.join(path_img, "heart1.png"))
heart2_img = pygame.image.load(os.path.join(path_img, "heart2.png"))
heart3_img = pygame.image.load(os.path.join(path_img, "heart3.png"))
house_img = pygame.image.load(os.path.join(path_img, "house.png"))
house2_img = pygame.image.load(os.path.join(path_img, "house2.png"))