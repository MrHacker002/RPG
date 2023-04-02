import pygame

pygame.init()

#variables
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
sc_w, sc_h = sc.get_width(), sc.get_height()
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
    def draw_sur(self,surface):
        surface.blit(self.image, (self.rect.x, self.rect.y))

class Camera():
    def __init__(self):
        self.speed = 10
    def movement(self):
        keys_input = pygame.key.get_pressed()
        for line in world_map:
            for block in line:
                if keys_input[pygame.K_w] and world_map[0][0].rect.top < 0:
                    block.rect.y += self.speed
                if keys_input[pygame.K_a] and world_map[0][0].rect.left < 0:
                    block.rect.x += self.speed
                if keys_input[pygame.K_s] and world_map[0][49].rect.bottom > sc_h:
                    block.rect.y -= self.speed
                if keys_input[pygame.K_d] and world_map[49][0].rect.right > sc_w+100:
                    block.rect.x -= self.speed
#--------------------------------------
camera = Camera()
tileSize = 100
world_map = [[GameSprite(tileSize*i,tileSize*y,tileSize,tileSize,dirt_img) for y in range(50)] for i in range(50)]
while game:
    sc.fill(BLACK)
    for line in world_map:
        for block in line:
            block.draw()
    camera.movement()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            game = False
    pygame.display.flip()
    clock.tick(fps)
