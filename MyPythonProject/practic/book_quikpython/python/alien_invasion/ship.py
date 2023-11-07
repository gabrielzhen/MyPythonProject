import pygame
from pygame.sprite import Sprite

class Ship(Sprite):
    def __init__(self,screen,ai_setting):
        super().__init__()
        self.screen=screen
        self.ai_setting=ai_setting
        self.image=pygame.image.load('images/ship.bmp')
        self.rect=self.image.get_rect()#获取飞船的矩形
        self.screen_rect=self.screen.get_rect()#获取屏幕的矩形
        #将飞船放在屏幕正中底部
        self.rect.centerx=self.screen_rect.centerx
        self.rect.bottom=self.screen_rect.bottom
        self.moving_right=False
        self.moving_left=False
        #飞船属性中存储小数值
        self.center=float(self.rect.centerx)
    #绘制飞船
    def blitme(self):
        self.screen.blit(self.image,self.rect)
    
    #更新飞船坐标
    def update(self):
        if self.moving_right and self.rect.right<self.screen_rect.right:
            self.center+=self.ai_setting.ship_speed_factor
        if self.moving_left and self.rect.left>self.screen_rect.left:
            self.center-=self.ai_setting.ship_speed_factor
        self.rect.centerx=self.center

    def center_ship(self):
        self.center=self.screen_rect.centerx
    