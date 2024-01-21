import pygame
from pygame.sprite import Sprite  # Sprite类多个元素进行编组


class Bullect(Sprite):
    """管理飞船所发射子弹的类。"""

    def __init__(self, ai_game):
        """在飞船当前位置创建一个子弹对象。"""
        # super()初始化父类属性。
        super().__init__()

        # ai_game.screen显示窗口
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.color = self.settings.bullet_color

        # 在(0, 0)点位置，创建一个子弹的矩形，在设置正确的位置。
        self.rect = pygame.Rect(0, 0, self.settings.bullet_width, self.settings.bullet_height)
        # 子弹外接矩形和飞船外接矩形，顶部对齐。
        self.rect.midtop = ai_game.ship.rect.midtop

        # 存储用小数表示的子弹位置。
        self.y = float(self.rect.y)

    def update(self):
        # 向上移动子弹
        self.y -= self.settings.bullet_speed
        self.rect.y = self.y

    def draw_bullet(self):
        """在屏幕(screen窗口)上绘制子弹。"""
        pygame.draw.rect(self.screen, self.color, self.rect)
