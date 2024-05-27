import sys

import pygame

from alien import Alien
from bullet import Bullet
from settings import Settings
from ship import Ship


class AlienInvasion:
    """管理游戏资源和行为的类"""

    def __init__(self):
        """初始化游戏并创建游戏资源"""
        pygame.init()
        pygame.display.set_caption("Alien Invasion")
        self.settings = Settings()
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        # 全拼显示游戏
        # self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        # self.settings.screen_width = self.screen.get_rect().width
        # self.settings.screen_height = self.screen.get_rect().height
        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()
        self.aliens = pygame.sprite.Group()
        self._create_fleet()

    def run_game(self):
        """开始游戏的主循环"""
        while True:
            self._check_event()
            self.ship.update()
            self._update_bullets()
            self._update_alien()
            self._update_screen()

    def _update_bullets(self):
        """更新子弹位置并删除消失的子弹"""
        self.bullets.update()
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)
        # 使用pygame.sprite.groupcollide()检查是否有子弹击中了外星人并将它们移除
        collisions = pygame.sprite.groupcollide(self.bullets, self.aliens, True, True)
        # 当前所有外星人被消灭后，生成新的外星人
        if not self.aliens:
            self.bullets.empty()
            self._create_fleet()

    def _update_alien(self):
        """
        检查是否有外星人位于屏幕边缘
        并更新整群外星人的位置
        """
        self._check_fleet_edges()
        self.aliens.update()

    def _check_fleet_edges(self):
        """有外星人到达边缘时采取相应措施"""
        for alien in self.aliens.sprites():
            if alien.check_edges():
                self._change_fleet_direction()
                break

    def _change_fleet_direction(self):
        """将正群外星人下移并改变他们的方向"""
        for alien in self.aliens.sprites():
            alien.rect.y += self.settings.fleet_drop_speed
        self.settings.fleet_direction *= -1

    def _update_screen(self):
        """更新屏幕上的图像并更新到新屏幕"""
        self.screen.fill(self.settings.bg_color)
        self.ship.blit_me()
        for bullet in self.bullets:
            bullet.draw_bullet()
        self.aliens.draw(self.screen)
        # 让最近绘制的屏幕可见
        pygame.display.flip()

    def _check_event(self):
        """响应案件和鼠标事件"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)

    def _check_keyup_events(self, event):
        """响应按键松开事件"""
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False
        elif event.key == pygame.K_UP:
            self.ship.moving_up = False
        elif event.key == pygame.K_DOWN:
            self.ship.moving_down = False

    def _check_keydown_events(self, event):
        """响应按键按下事件"""
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        elif event.key == pygame.K_UP:
            self.ship.moving_up = True
        elif event.key == pygame.K_DOWN:
            self.ship.moving_down = True
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()
        elif event.key == pygame.K_ESCAPE:
            sys.exit()
        else:
            print(event.key)

    def _fire_bullet(self):
        """创建一颗子弹，并将其加入编组中"""
        if len(self.bullets) < self.settings.bullet_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)

    def _create_fleet(self):
        """
        创建外星人群：
        创建一个外星人并计算一行可容纳多少个外星人
        外形的间距为外星人的宽度
        """
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size
        # 计算一行可以放置多少个外星人
        available_space_x = self.settings.screen_width - (alien_width << 1)
        number_aliens_x = available_space_x // (alien_width << 1)
        # 计算可以放置多少行
        available_space_y = self.settings.screen_height - (3 * alien_height) - self.ship.rect.height
        number_rows = available_space_y // (alien_height << 1)
        # 创建外星人
        for row_number in range(number_rows):
            for alien_number in range(number_aliens_x):
                self._create_alien(alien_number, row_number)

    def _create_alien(self, alien_number, row_number):
        """创建一个外星人并将其加入当前行"""
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size
        # 设置外星人的x轴位置
        alien.x = alien_width + ((alien_number * alien_width) << 1)
        alien.rect.x = alien.x
        # 设置外星人的y轴位置
        alien.rect.y = alien.rect.height + ((alien.rect.height * row_number) << 1)
        # 将外星人添加到组中
        self.aliens.add(alien)


if __name__ == "__main__":
    ai = AlienInvasion()
    ai.run_game()
