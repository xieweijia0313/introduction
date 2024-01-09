import pygame


class Ship:
    """管理飞船的类"""

    def __init__(self, ai_game):

        """初始化飞船并设置初始化位置。"""
        # ai_game.screen游戏窗口。
        self.screen = ai_game.screen
        # 加载游戏窗口为外接矩形。
        self.screen_rect = ai_game.screen.get_rect()
        # 指定矩形位置，要将游戏元素居中，可设置相应rect 对象的属性center 、centerx 或centery 。要让游戏元素与屏幕边缘对齐，可使用属性top 、bottom 、left 或right ；
        # 要调整游戏元素的水平或垂直位置，可使用属性x 和y ，它们分别是相应矩形左上角的 x 和 y 坐标。
        # 加载飞船图像，并设置rect（外接矩形）属性
        self.image = pygame.image.load(R'images\ship.bmp')
        # 加载飞船图像为外接矩形。
        self.rect = self.image.get_rect()
        # 加载飞船settings配置文件
        self.settings = ai_game.settings

        # 位置对齐，让飞船底部中央位置等于游戏窗口底部中央位置。
        # self.rect.centerx = self.screen_rect.centerx
        self.rect.midbottom = self.screen_rect.midbottom
        # 存储精确的水平位置
        self.x = float(self.rect.x)
        # 检测飞船是否正在向右移动。
        self.moving_right = False
        # 检测飞船是否正在向左移动。
        self.moving_left = False

    def blitme(self):
        """在游戏窗口的指定位置绘制飞船。"""
        self.screen.blit(self.image, self.rect)

    def update(self):
        # 根据移动标志调整飞船位置。且飞船移动位置不能超出游戏窗口
        if self.moving_right and self.rect.right < self.screen_rect.right:
            # 飞船的移动速度读取setting.py配置文件设定的速度
            self.x += self.settings.ship_speed

        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.ship_speed
        self.rect.x = self.x
