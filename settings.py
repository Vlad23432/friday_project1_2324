class Settings:
    """Класс для настроек игры (всех)"""
    def __init__(self):
        """Инициализация настроек игры"""
        self.screen_width = 1280
        self.screen_height = 800
        self.bg_color = (230, 230, 230)
        self.ship_speed_factor = 1.5

        # настройки пули
        self.bullet_width = 4
        self.bullet_height = 15
        self.bullet_speed = 1
        self.bullet_color = (241, 115, 255)
        self.bullets_allowed = 3