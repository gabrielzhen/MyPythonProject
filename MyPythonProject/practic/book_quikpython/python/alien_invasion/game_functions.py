import sys,pygame
from bullet import Bullet
from alien import Alien
from time import sleep
#重构后的keydown方法
def check_keydown_events(event,ai_setting,screen,ships,bullets):
    if event.key==pygame.K_RIGHT:
        ships.moving_right=True
    if event.key==pygame.K_LEFT:
        ships.moving_left=True
    if event.key==pygame.K_SPACE:
        fire_bullet(ai_setting,screen,ships,bullets)
    if event.key==pygame.K_q:
        sys.exit()
    
#重构后的keyup方法
def check_keyup_events(event,ships):
    if event.key==pygame.K_RIGHT:
        ships.moving_right=False
    if event.key==pygame.K_LEFT:
        ships.moving_left=False 

#监控按键方法
def check_events(ai_setting,stats,sb,play_button,aliens,screen,ships,bullets):
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            sys.exit()
        elif event.type==pygame.KEYDOWN:
            check_keydown_events(event,ai_setting,screen,ships,bullets)               
        elif event.type==pygame.KEYUP:
            check_keyup_events(event,ships)  
        elif event.type==pygame.MOUSEBUTTONDOWN:
            mouse_x,mouse_y=pygame.mouse.get_pos()
            check_play_button(stats,ai_setting,sb,screen,ships,aliens,bullets,play_button,mouse_x,mouse_y)    
#新开始游戏进行初始化
def  check_play_button(stats,ai_setting,sb,screen,ships,aliens,bullets,play_button,mouse_x,mouse_y):
    if play_button.rect.collidepoint(mouse_x,mouse_y) and not stats.game_active:
        pygame.mouse.set_visible(False)
        ai_setting.initialize_dynamic_settings()
        stats.reset_stats()
        stats.game_active=True  
        sb.prep_score()
        sb.prep_level() 
        sb.prep_ships() 
        bullets.empty()
        aliens.empty()
        #创建外星人群和飞船居中
        create_fleet(ai_setting,screen,ships,aliens)
        ships.center_ship()                
        
#刷新屏幕
def update_screen(ai_setting,stats,sb,screen,ships,aliens,bullets,play_button):
    screen.fill(ai_setting.bg_color)
    sb.show_score()
    ships.blitme()
    aliens.draw(screen)#不同于ship aliens存在于一个组中 所以需要用draw方法进行绘制
    for bullet in bullets.sprites():#获取group里面的值
        bullet.draw_bullet()
    if not stats.game_active:
        play_button.draw_button()
    pygame.display.flip()


#子弹管理
def update_bullets(ai_setting,screen,sb,stats,ships,aliens,bullets):
    bullets.update()
    #删除消失的子弹
    for bullet in bullets.copy():
            if bullet.rect.y<=0:
                bullets.remove(bullet)
    check_bullet_alien_collisions(ai_setting,screen,sb,stats,ships,aliens,bullets)

#碰撞检测 创建新外星人
def  check_bullet_alien_collisions(ai_setting,screen,sb,stats,ships,aliens,bullets):
    collisions=pygame.sprite.groupcollide(bullets,aliens,True,True)
    if collisions:
        for alien in collisions.values():
            stats.score+=ai_setting.alien_points*len(alien)
            sb.prep_score()
        check_high_score(stats,sb)
    #检查外星人是否全部没有了？
    if len(aliens)==0:
        ai_setting.increase_speed()
        bullets.empty()

        #提高等级
        stats.level+=1
        sb.prep_level()
        create_fleet(ai_setting,screen,ships,aliens)


#子弹开火
def fire_bullet(ai_setting,screen,ships,bullets):
    if len(bullets)<ai_setting.bullet_allowed:
        new_bullet=Bullet(ai_setting,screen,ships)#将每次获取的bullet实例加到group编组中，可以在后面遍历的时候使用方法
        bullets.add(new_bullet)

#计算一行可以创建多少外星人
def get_number_alines_x(ai_setting,alien_width):
    available_sapce_x=ai_setting.screen_width-2*alien_width
    number_aliens_x=int(available_sapce_x/(2*alien_width))
    return number_aliens_x
#计算可以创建多少行外星人
def get_number_rows(ai_setting,ship_height,alien_height):
    available_sapce_y=ai_setting.screen_hight-3*alien_height-ship_height
    number_rows=int(available_sapce_y/(2*alien_height))
    return number_rows
#创建一个特性位置的外星人
def create_alien(ai_setting,screen,aliens,aline_number,row_number):
        alien=Alien(ai_setting,screen)
        alien_width=alien.rect.x
        alien_height=alien.rect.y
        alien.x=alien_width+2*alien_width*aline_number
        alien.rect.x=alien.x 
        alien.rect.y=alien_height+2*alien_height*row_number
        aliens.add(alien)#将外星人添加到aliens组中
#创建外星人群
def create_fleet(ai_setting,screen,ships,aliens):
    alien=Alien(ai_setting,screen)
    number_aliens_x=get_number_alines_x(ai_setting,alien.rect.x)
    number_rows=get_number_rows(ai_setting,ships.rect.height,alien.rect.y)
    #根据计算创建第一行外星人
    for row_number in range(number_rows):
        for aline_number in range(number_aliens_x):
            create_alien(ai_setting,screen,aliens,aline_number,row_number)

#外星人到达边缘进行相关操作
def check_fleet_edges(ai_setting,aliens):
    for alien in aliens.sprites():
        if alien.check_edges():
            change_fleet_direction(ai_setting,aliens)
            break #有这样的情况就跳出不进行其他外星人的判断
#更新外星人的方向
def change_fleet_direction(ai_setting,aliens):
    for alien in aliens.sprites():
        alien.rect.y+=ai_setting.fleet_drop_speed
    ai_setting.fleet_direction*=-1

#响应被外星人撞到的飞船
def ship_hit(ai_setting,screen,sb,stats,ships,aliens,bullets):
    if  stats.ships_left>0:
        stats.ships_left-=1
        sb.prep_ships()
        #清空子弹和外星人
        bullets.empty()
        aliens.empty()
        #创建外星人群和飞船居中
        create_fleet(ai_setting,screen,ships,aliens)
        ships.center_ship()
        sleep(0.5)
    else:
        stats.game_active=False
        pygame.mouse.set_visible(True)

#检查是否有外星人撞到底部
def check_alines_bottom(ai_setting,screen,sb,stats,ships,aliens,bullets):
    screen_rect=screen.get_rect()
    for alien in aliens.sprites():
        if alien.rect.bottom>=screen_rect.bottom:
            ship_hit(ai_setting,screen,sb,stats,ships,aliens,bullets)
            break

#更新外星人位置
def update_aliens(ai_setting,screen,sb,stats,ships,aliens,bullets):
    check_fleet_edges(ai_setting,aliens)
    aliens.update()
    if pygame.sprite.spritecollideany(ships,aliens):
        ship_hit(ai_setting,screen,sb,stats,ships,aliens,bullets)
    check_alines_bottom(ai_setting,screen,sb,stats,ships,aliens,bullets)

def check_high_score(stats,sb):
    if stats.score>stats.high_score:
        stats.high_score=stats.score
        sb.prep_high_score()
