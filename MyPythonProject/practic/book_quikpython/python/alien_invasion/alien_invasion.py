import sys,pygame
import setting,ship,alien,game_functions
from pygame.sprite import Group
from game_stats import GameStats
from button import Button
from scoreboard import Scoreboard

def run_game():
    pygame.init()
    ai_setting=setting.Setting() #创建配置对象
    screen=pygame.display.set_mode((ai_setting.screen_width,ai_setting.screen_hight))  #设置屏幕大小
    pygame.display.set_caption("Alien Invasion") #设置标题
    #创建存储统计信息的对象
    stats=GameStats(ai_setting)
    sb=Scoreboard(ai_setting,screen,stats)
    play_button=Button(screen,'PLAY')
    ships=ship.Ship(screen,ai_setting) #创建飞船  
    bullets=Group()
    aliens=Group()
    #game_functions.create_fleet(ai_setting,screen,ships,aliens)#创建外星人群

    while True:
        game_functions.check_events(ai_setting,stats,sb,play_button,aliens,screen,ships,bullets)#监控按键和视窗
        if stats.game_active:
            ships.update()#飞船状态更新
            game_functions.update_bullets(ai_setting,screen,sb,stats,ships,aliens,bullets)#子弹状态更新
            game_functions.update_aliens(ai_setting,screen,sb,stats,ships,aliens,bullets)#外星人状态更新
        game_functions.update_screen(ai_setting,stats,sb,screen,ships,aliens,bullets,play_button)#屏幕物体刷新

run_game()