import os
import pygame

path_img = os.path.join(os.path.abspath(__file__+'\..'), "assets")

dirt_img = pygame.image.load(os.path.join(path_img, "dirt.png"))
grass_img = pygame.image.load(os.path.join(path_img, "grass2.png"))
tree_img = pygame.image.load(os.path.join(path_img, "tree.png"))
player_img = pygame.image.load(os.path.join(path_img, "player.png"))