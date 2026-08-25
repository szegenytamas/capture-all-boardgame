import pygame
from pygame.math import Vector2
from constants import CELL_SIZE, BOARD_WIDTH, BOARD_HEIGHT, STARTING_POINTS, FORBIDDEN_BLOCKS, P_COLORS, A_COLORS, ANIMAL_PICTURES


class Board():
    def __init__(self):
        self.cell_size = CELL_SIZE
        self.board_width = BOARD_WIDTH
        self.board_height = BOARD_HEIGHT
        self.starting_points = STARTING_POINTS
        self.forbidden_blocks = FORBIDDEN_BLOCKS
        self.game_paused = False
        self.game_on = False
        self.skull_img = pygame.image.load(
            'graphics/skull.png').convert_alpha()

    def draw_board(self, screen):
        dark_yellow = (245, 183, 39)
        red = (245, 42, 39)

        for row in range(self.board_height):
            for col in range(self.board_width):
                pos = Vector2(col, row)
                rect = pygame.Rect(
                    col * self.cell_size, row * self.cell_size, self.cell_size, self.cell_size
                )
                if pos in self.starting_points:
                    pygame.draw.rect(screen, red, rect)
                else:
                    pygame.draw.rect(screen, dark_yellow, rect)
                pygame.draw.rect(screen, 'black', rect, 1)

                if pos in self.forbidden_blocks:
                    skull_rect = self.skull_img.get_rect(center=(col*self.cell_size + self.cell_size/2,
                                                                 row*self.cell_size + self.cell_size/2))
                    screen.blit(self.skull_img, skull_rect)
