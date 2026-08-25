import pygame
from pygame.math import Vector2
from constants import STARTING_POINTS, CELL_SIZE, OFFSETS, FORBIDDEN_BLOCKS


class Player:
    def __init__(self, _color_tuple, _start_index, _his_turn=False):
        self.pos = STARTING_POINTS[_start_index]
        self.color = _color_tuple
        self.image = pygame.image.load(
            f'graphics/hunter_{self.color[0]}.png').convert_alpha()
        self.score = 0
        self.his_turn = _his_turn
        self.num_caught_animals = 0
        self.update_rect()
        self.target_pixel = Vector2(self.pixel_pos)
        self.is_moving = False
        self.speed = 4

    def update_rect(self):
        cx = self.pos.x * CELL_SIZE + CELL_SIZE / 2
        cy = self.pos.y * CELL_SIZE + CELL_SIZE / 2
        self.rect = self.image.get_rect(center=(cx, cy))
        self.pixel_pos = Vector2(cx, cy)

    def start_move(self, new_block):
        self.pos = new_block
        self.target_pixel = Vector2(
            new_block.x * CELL_SIZE + CELL_SIZE / 2,
            new_block.y * CELL_SIZE + CELL_SIZE / 2
        )
        self.is_moving = True

    def update_animation(self):
        if self.is_moving:
            direction = self.target_pixel - self.pixel_pos
            if direction.length() < self.speed:
                self.pixel_pos = Vector2(self.target_pixel)
                self.is_moving = False
            else:
                direction.normalize_ip()
                self.pixel_pos += direction * self.speed
            self.rect.center = (self.pixel_pos.x, self.pixel_pos.y)

    def draw_player(self, screen):
        screen.blit(self.image, self.rect)

    def possible_moves(self, screen, players, animal_poses):
        offsets = OFFSETS
        self.next_moves = [self.pos + offset for offset in offsets]

        green = (39, 245, 42)
        if self.his_turn and not self.is_moving:
            taken = [p.pos for p in players]
            for i in self.next_moves:
                if i in FORBIDDEN_BLOCKS or i in taken:
                    continue

                next_move = pygame.Rect(
                    i.x*CELL_SIZE, i.y*CELL_SIZE, CELL_SIZE, CELL_SIZE)
                if i in animal_poses:
                    pygame.draw.rect(screen, 'green', next_move, 5)
                else:
                    pygame.draw.rect(screen, green, next_move)
                    pygame.draw.rect(screen, self.color[1], next_move, 5)

    def move_player(self, new_block):
        if new_block in self.next_moves and new_block not in FORBIDDEN_BLOCKS:
            self.pos = new_block
            self.rect = self.image.get_rect(center=(self.pos.x*CELL_SIZE + CELL_SIZE/2,
                                                    self.pos.y*CELL_SIZE + CELL_SIZE/2))

    def check_capture(self, animals, capture_sound, a_timer=None, dragon=None, ):
        if dragon:
            if self.pos == dragon.pos:
                dragon.is_caught = True
                self.score += dragon.score
                dragon.who_caught_me = self.color
                pygame.time.set_timer(a_timer, 0)
                dragon.dragon_capture_sound.play()
                return
        for animal in animals:
            if self.pos == animal.pos and not animal.is_caught:
                animal.is_caught = True
                animal.who_caught_me = self.color[1]
                self.score += animal.score
                self.num_caught_animals += 1
                capture_sound.play()
