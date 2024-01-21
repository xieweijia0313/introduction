class Settings:
    """存储《外星人入侵》所有设置的类"""

    def __init__(self):
        """初始化游戏的设置"""
        # 屏幕宽度
        self.screen_width = 1200
        # 屏幕高度
        self.screen_height = 800
        # 屏幕背景颜色，RGB红绿蓝
        self.bg_color = (230, 230, 230)
        # 飞船移动速度，像素
        self.ship_speed = 1.5
        # 子弹移动速度，像素
        self.bullet_speed = 1.5
        # 子弹宽度
        self.bullet_width = 3
        # 子弹高度
        self.bullet_height = 15
        # 子弹背景颜色
        self.bullet_color = (60, 60, 60)
        # 子弹数量
        self.bullet_allowed = 10
        # 外星人移动速度
        self.alien_speed = 0.1
        # 外星人下移高度
        self.fleet_drop_speed = 10
        # 外星人，1右移，-1左移
        self.fleet_direction = 1
