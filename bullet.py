import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    """Класс для управления пулями, выпущенными кораблем."""

    def __init__(self, ai_settings, screen, ship):
        """создает объект пули в текущей позиции корабля."""
        super(Bullet, self).__init__()
        self.screen = screen

        # Создание пули в позиции (0,0) и назначение преаильной позиции.
        self.rect = pygame.Rect(0, 0, ai_settings.bullet_width,
                    ai_settings.bullet_height)
        self.rect.centerx = self.rect.centerx
        self.rect.top = self.rect.top

        # Позиция пули хранится в вещественном формате
        self.y = float(self.rect.y)

        self.color = ai_settings.bullet_color
        self.speed_factor = ai_settings.bullet_speed_factor
