import sys

import pygame

from bullet import Bullet


def check_keydown_events(event, ai_settings, screen, ship, bullets):
    """реагирует на нажатие клавиш. """
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True
    elif event.key == pygame.K_SPACE:
        fire_bullet(ai_settings, screen, ship, bullets)
    elif event.key == pygame.K_q:
        sys.exit()


def chech_keyup_events(event, ship):
    """реагирует на отпускание клавиш. """

    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False


def check_events(ai_settings, screen, ship, bullets):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, ai_settings, screen, ship, bullets)
        elif event.type == pygame.KEYUP:
            chech_keyup_events(event, ship)


def update_screen(ai_settings, screen, ship, bullets):
    screen.fill(ai_settings.bg_color)

    for bullet in bullets.sprites():
        bullet.draw_bullet()
    ship.blitme()
    # Отображение последнего прорисованного экрана
    pygame.display.flip()


def update_bullets(bullets):
    """Обновляет позиции пуль и уничтожает страрые пули."""
    # Обновление позиций пуль.
    bullets.update()

    # Удаление пуль, вышедших за край экрана

    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)


def fire_bullet(ai_settings, screen, ship, bullets):
    """Выпускает пулю, если если максимум еще не достигнут"""
    # Создание новой пули и включени ее в группу bullets

    if len(bullets) < ai_settings.bullet_allowed:
        new_bullet = Bullet(ai_settings, screen, ship)
        bullets.add(new_bullet)
