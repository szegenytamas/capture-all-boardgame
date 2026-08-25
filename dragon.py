import pygame
from pygame.math import Vector2
import random
from constants import BOARD_HEIGHT, BOARD_WIDTH, CELL_SIZE
import math


class Dragon():
    def __init__(self):
        self.face_image = pygame.image.load(
            'graphics/dragon_face.png').convert_alpha()
        self.flying_image_original = pygame.image.load(
            'graphics/flying.png').convert_alpha()
        self.head_image = pygame.image.load(
            'graphics/dragon_head.png').convert_alpha()
        self.flying_image = self.flying_image_original
        self.is_caught = False
        self.is_flying = False
        self.speed = 4
        self.score = 5000
        self.pos = self.generate_new_pos()
        cx = self.pos.x * CELL_SIZE + CELL_SIZE / 2
        cy = self.pos.y * CELL_SIZE + CELL_SIZE / 2

        self.pixel_pos = Vector2(cx, cy)
        self.target_pixel = Vector2(cx, cy)
        self.rect = pygame.Rect(self.pos.x * CELL_SIZE,
                                self.pos.y * CELL_SIZE, CELL_SIZE, CELL_SIZE)
        self.face_rect = self.face_image.get_rect(center=(cx, cy))
        self.who_caught_me = None
        self.dragon_roar = pygame.mixer.Sound('sounds/roar.mp3')
        self.dragon_roar.set_volume(0.1)
        self.dragon_capture_sound = pygame.mixer.Sound(
            'sounds/dragon_capture.mp3')
        self.dragon_capture_sound.set_volume(0.1)

    def generate_new_pos(self):
        p_x = random.randint(0, BOARD_WIDTH - 1)
        p_y = random.randint(0, BOARD_HEIGHT - 1)
        return Vector2(p_x, p_y)

    def update_pos(self):
        self.pos = self.generate_new_pos()
        cx = self.pos.x * CELL_SIZE + CELL_SIZE / 2
        cy = self.pos.y * CELL_SIZE + CELL_SIZE / 2
        self.pixel_pos = Vector2(cx, cy)
        self.target_pixel = Vector2(cx, cy)
        self.rect.topleft = (self.pos.x * CELL_SIZE, self.pos.y * CELL_SIZE)
        self.face_rect.center = (cx, cy)

    def draw_dragon(self, screen):
        if not self.is_flying:
            pygame.draw.rect(screen, 'black', self.rect)
            if self.is_caught:
                pygame.draw.line(
                    screen, self.who_caught_me[1], self.rect.topleft, self.rect.bottomright, 3)
                pygame.draw.line(
                    screen, self.who_caught_me[1], self.rect.topright, self.rect.bottomleft, 3)
        active_sprite = self.flying_image if self.is_flying else self.face_image
        screen.blit(active_sprite, self.face_rect)

    def start_move(self, new_block):
        self.pos = new_block
        self.target_pixel = Vector2(
            new_block.x * CELL_SIZE + CELL_SIZE / 2,
            new_block.y * CELL_SIZE + CELL_SIZE / 2
        )
        self.rect.topleft = (new_block.x * CELL_SIZE, new_block.y * CELL_SIZE)
        self.is_flying = True

        direction = self.target_pixel - self.pixel_pos
        if direction.length() > 0:
            self.rotation_angle = Vector2(0, -1).angle_to(direction)
            self.flying_image = pygame.transform.rotate(
                self.flying_image_original, -self.rotation_angle)
            self.face_rect = self.flying_image.get_rect(
                center=(int(self.pixel_pos.x), int(self.pixel_pos.y)))

        self.is_flying = True

    def update_animation(self):
        if self.is_flying:

            direction = self.target_pixel - self.pixel_pos
            if direction.length() <= self.speed:
                self.pixel_pos = Vector2(self.target_pixel)
                self.is_flying = False
                self.face_rect = self.face_image.get_rect(
                    center=(int(self.pixel_pos.x), int(self.pixel_pos.y)))
            else:
                direction.normalize_ip()
                self.pixel_pos += direction * self.speed
                self.face_rect.center = (
                    int(self.pixel_pos.x), int(self.pixel_pos.y))
