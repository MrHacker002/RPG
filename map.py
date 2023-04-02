import pygame

pygame.init()

#variables
sc_w = 1200
sc_h = 800
fps = 60
game = True
block_x = 0
block_y = 0
BLACK = (0,0,0)
#--------------------------------------
#game assets
dirt_img = pygame.image.load("dirt.png")
#--------------------------------------

sc = pygame.display.set_mode((0,0), pygame.FULLSCREEN)
clock = pygame.time.Clock()

#classes
class GameSprite(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height, image):
        super().__init__()
        self.image = pygame.transform.scale(image, (width, height))
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = x, y
    def draw(self):
        sc.blit(self.image, (self.rect.x, self.rect.y))

class Camera():
    def __init__(self):
        self.speed = 10
    def movement(self):
        keys_input = pygame.key.get_pressed()
        if keys_input[pygame.K_w]:
            for block in world_map:
                block.rect.y += self.speed
        if keys_input[pygame.K_a]:
            for block in world_map:
                block.rect.x += self.speed
        if keys_input[pygame.K_s]:
            for block in world_map:
                block.rect.y -= self.speed
        if keys_input[pygame.K_d]:
            for block in world_map:
                block.rect.x -= self.speed
#--------------------------------------
camera = Camera()
world_map = []
for x in range(200):
    for y in range(200):
        dirt = GameSprite(block_x, block_y,100,100,dirt_img)
        world_map.append(dirt)
        block_x += 50
    block_x = 0
    block_y += 50
while game:
    sc.fill(BLACK)
    for block in world_map:
        block.draw()
    camera.movement()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            game = False
    pygame.display.update()
    clock.tick(fps)