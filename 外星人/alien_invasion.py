"""
version = "1.2"
项目环境搭建：
1.Pygame安装。打开PyCharm终端。【python -m pip install --user pygame】
更新pip。【python.exe -m pip install --upgrade pip】

流程：
1.创建一个空Pygame窗口文件,"alien_invasion.Py"
2.创建设置文件，“settings.py”
3.创建外星飞船模型和位置文件，“settings.py”
重构，简化既有代码的结构，使其更容易扩展。

“images”文件夹存放项目图片资源
"""

import sys
import pygame
from settings import Settings  # 设置库
from ship import Ship  # 资源库
from bullet import Bullect
from alien import Alien


class AlienInvasion:
    """管理游戏资源和行为的类"""

    def __init__(self):
        """初始化游戏并创建游戏资源"""
        pygame.init()
        # 创建Settings类的实例对象。
        self.settings = Settings()
        # 创建一个名为screen的显示窗口，设置窗口的长和宽。
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        # 全屏显示,self.screen传入pygame.FULLSCREEN
        # self.settings.screen_width = self.screen.get_rect().width
        # self.settings.screen_height = self.screen.get_rect().height
        pygame.display.set_caption("Alien Invasion")
        # 游戏实例，传入当前的窗口。
        self.ship = Ship(self)
        # 使用sprite.Group()方法创建子弹编组
        self.bullets = pygame.sprite.Group()
        # 新建外星人类的编组
        self.aliens = pygame.sprite.Group()
        self._create_fleet()

    def run_game(self):
        """开始游戏主循环"""
        while True:
            # 检测事件
            self._check_events()
            # 刷新飞船
            self.ship.update()
            # 刷新子弹
            self._update_bullets()
            self._update_aliens()
            # 刷新屏幕
            self._update_screen()

    def _check_events(self):
        """重构代码,管理事件"""

        # 事件循环，监视键盘和鼠标事件。
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

            # 检测事件类型，是否是按下键盘按键。
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)

            # 检测事件类型，是否是松开键盘按键。
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)

    def _check_keydown_events(self, event):
        """响应按键"""
        # 检测按下的是否是右键，如果是就将飞梭向右移动。
        if event.key == pygame.K_RIGHT:
            # self.ship.rect.x += 1
            self.ship.moving_right = True
        # 检测按下的是否是左键，如果是就将飞梭向左移动。
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        # 检测按下的是否是"q"键，如果是就将退出游戏。
        elif event.key == pygame.K_q:
            sys.exit()
        # 检测按下的是否是空格键，如果是就创建一颗子弹。
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()

    def _check_keyup_events(self, event):
        """响应松开"""
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False

    def _update_screen(self):
        """重构代码,更新屏幕"""

        # 每次循环时都重新绘制屏幕。
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        # draw方法，将编组里面的每一个元素依次绘制到屏幕上面
        self.aliens.draw(self.screen)
        # 让最近绘制的屏幕可见。
        pygame.display.flip()

    def _update_bullets(self):
        # 移动子弹
        self.bullets.update()
        # 遍历编组的副本，将移动到屏幕之外的子弹移除
        for bullet in self.bullets.copy():
            # 子弹外接矩形的底部小于等于0
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)
        self._check_bullet_alien_collisions()
        # print(len(self.bullets))

    def _check_bullet_alien_collisions(self):
        # 碰撞检测，(子弹， 外星人，碰撞子弹是否要消失，碰撞外星人是否要消失。True 消失, False不消失)
        collisions = pygame.sprite.groupcollide(
            self.bullets, self.aliens, False, True
        )
        if not self.aliens:
            # 删除现有的子弹并新建一批外星人
            self.bullets.empty()
            self._create_fleet()

    def _fire_bullet(self):
        """创建一个新子弹，并将其加入编组 bullets 中。"""
        if len(self.bullets) < self.settings.bullet_allowed:
            new_bullet = Bullect(self)
            self.bullets.add(new_bullet)

    def _create_fleet(self):
        """创建外星人群。"""
        # 创建一个外星人。
        alien = Alien(self)
        # 获取外星人的宽度
        # alien_width = alien.rect.width
        alien_width, alien_height = alien.rect.size
        # 获取游戏窗口的宽度-2*外星人宽度。
        available_space_x = self.settings.screen_width - (2 * alien_width)
        # 可用空间除以2*外星人宽度，结果向下取整。
        numbers_aliens_x = available_space_x // (2 * alien_width)
        # 获取飞船外接矩形的高度。
        ship_height = self.ship.rect.height
        available_space_y = (self.settings.screen_height - (3 * alien_height - ship_height))
        numbers_rows = available_space_y // (2 * alien_height)

        # 创建第一行外星人。
        for row_number in range(numbers_rows):
            for alien_number in range(numbers_aliens_x):
                self._create_alien(alien_number, row_number)

    def _create_alien(self, alien_number, row_number):
        """创建一个外星人并将其放在当前行。"""
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size
        alien.x = alien_width + 2 * alien_width * alien_number
        # 因为rect.x一般取整数，所以先将精确的数值赋值给alien.x。
        alien.rect.x = alien.x
        # y轴阵列
        alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number
        self.aliens.add(alien)

    def _update_aliens(self):
        self._check_fleet_edges()
        self.aliens.update()
        # 检测外星人和飞船有没有发生碰撞，（游戏元素，游戏编组）检查游戏元素有没有和游戏编组里面的任何成员发生碰撞，如果碰撞返回True。
        if pygame.sprite.spritecollideany(self.ship, self.aliens):
            print("Ship hit")

    def _check_fleet_edges(self):
        """有外星人到达边缘时，采取的措施"""
        for alien in self.aliens.sprites():
            if alien.check_edges():
                self._change_fleet_direction()
                break

    def _change_fleet_direction(self):
        """将整体外星人下移，并改变他们的方向。"""
        for alien in self.aliens.sprites():
            alien.rect.y += self.settings.fleet_drop_speed
        self.settings.fleet_direction *= -1


if __name__ == '__main__':
    ai = AlienInvasion()
    ai.run_game()
