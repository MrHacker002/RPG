import pygame

pygame.init()
sc = pygame.display.set_mode((0,0), pygame.FULLSCREEN)
clock = pygame.time.Clock()
FPS = 60
class Button:
    def __init__(self, x, y, w, h,color1, color2, text, size, text_color):
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
    def set_color(self,new_color):   
        self.color = new_color
    def draw(self):
        pygame.draw.rect(sc,self.color, self.rect)
        sc.blit(self.lable,(self.rect.x+20,self.rect.y))
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
button1 = Button(760, 300, 250, 50,(255,0,0),(0,255,0), "Начать игру", 30, (0,0,0))
button2 = Button(760, 370, 250, 50,(255,0,0),(0,255,0), "Загрузить игру", 30, (0,0,0))
button3 = Button(760, 440, 250, 50,(255,0,0),(0,255,0), "Настройки", 30, (0,0,0))

