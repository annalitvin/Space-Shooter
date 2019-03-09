class Settings():
    """Класс для хранения всех настроек игры Alient Invasion"""

    def __init__(self):
        """Инициализирует настройки игры"""
        self.screen_width = 1200
        self.screen_height = 600
        self.bg_color = (230, 230, 230)

        #настройка корабля
        self.ship_speed_factor = 1.5

        #параметры пули
        self.bullet_speed_factor = 1
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = 60, 60, 60
        self.bullet_allowed = 3

