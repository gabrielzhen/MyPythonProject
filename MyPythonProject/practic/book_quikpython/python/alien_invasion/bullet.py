import pygame
from pygame.sprite import Sprite
class Bullet(Sprite):
    def __init__(self,ai_setting,screen,ships):
        super().__init__()#继承sprite类
        self.screen=screen
        self.rect=pygame.Rect(0,0,ai_setting.bullet_width,ai_setting.bullet_height)#创建子弹矩形 初始位置0,0
        self.rect.centerx=ships.rect.centerx
        self.rect.top=ships.rect.top
        #获取默认的子弹的y轴坐标给属性y
        self.y=float(self.rect.y)

        self.color=ai_setting.bullet_color
        self.speed_factor=ai_setting.bullet_speed_factor
    
    def update(self):
        self.y-=self.speed_factor
        self.rect.y=self.y
    
    def draw_bullet(self):
        pygame.draw.rect(self.screen,self.color,self.rect)

