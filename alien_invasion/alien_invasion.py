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
            self._update_screen()

    def _update_bullets(self):
        """更新子弹位置并删除消失的子弹"""
        self.bullets.update()
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)

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
        elif event.key == pygame.K_q:
            sys.exit()
        else:
            print(event.key)

    def _fire_bullet(self):
        """创建一颗子弹，并将其加入编组中"""
        if len(self.bullets) < self.settings.bullet_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)

    def _create_fleet(self):
        """创建外星人群"""
        new_alien = Alien(self)
        self.aliens.add(new_alien)


if __name__ == "__main__":
    ai = AlienInvasion()
    ai.run_game()
