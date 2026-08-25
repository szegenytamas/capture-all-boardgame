import pygame
from constants import CELL_SIZE, BOARD_HEIGHT, BOARD_WIDTH, P_COLORS, ANIMALS_TO_CATCH


class UI:
    def __init__(self):
        self.pause_font = pygame.font.Font(
            'fonts/PoetsenOne-Regular.ttf', 35)
        self.intro_font = pygame.font.Font(
            'fonts/PoetsenOne-Regular.ttf', 55)
        self.intro_text = self.intro_font.render(
            "CAPTURE ALL !", True, 'black')
        self.intro_text_rect = self.intro_text.get_rect(
            center=((BOARD_WIDTH*CELL_SIZE)//2, (CELL_SIZE*BOARD_HEIGHT//10)))
        self.play_text = self.pause_font.render(
            "START".center(20, ' '), True, 'black')
        self.play_text_rect = self.play_text.get_rect(center=(
            (BOARD_WIDTH*CELL_SIZE)/1.15, (CELL_SIZE*BOARD_HEIGHT//2)))
        self.intro_img = pygame.image.load('graphics/tigerface.png')
        self.intro_img_rect = self.intro_img.get_rect(center=(
            (BOARD_WIDTH*CELL_SIZE)//2, (CELL_SIZE*BOARD_HEIGHT//2)))
        self.restart_text = self.pause_font.render(
            "RESTART GAME".center(20, ' '), True, 'black')
        self.restart_text_rect = self.restart_text.get_rect(center=(
            (BOARD_WIDTH*CELL_SIZE)/1.5, (CELL_SIZE*BOARD_HEIGHT//4)))
        self.quit_text = self.pause_font.render(
            "EXIT".center(20, ' '), True, 'black')
        self.quit_text_rect = self.quit_text.get_rect(center=(
            (BOARD_WIDTH*CELL_SIZE)/1.5, (CELL_SIZE*BOARD_HEIGHT//1.4)))
        self.paw_img = pygame.image.load('graphics/paw.png')

        self.selected_players = []
        for idx, color_data in enumerate(P_COLORS):
            image = pygame.image.load(
                f'graphics/hunter_{color_data[0]}.png').convert_alpha()
            image = pygame.transform.scale(
                image, size=(80, 80))
            rect = image.get_rect(midleft=(
                (BOARD_WIDTH * CELL_SIZE + idx * 800) / 6,
                (CELL_SIZE * BOARD_HEIGHT / 1.15)))
            self.selected_players.append(
                {'surf': image, 'rect': rect, 'color': color_data})

    def pause_game(self, screen, players, dragon=None):
        pause_rect = pygame.Rect(
            2*CELL_SIZE, 2*CELL_SIZE, 22*CELL_SIZE, 15*CELL_SIZE)
        pygame.draw.rect(screen, (204, 156, 0), pause_rect, 0, 20)
        pygame.draw.rect(screen, 'black', pause_rect, 4, 20)
        screen.blit(self.restart_text, self.restart_text_rect)
        pygame.draw.rect(screen, 'green', self.restart_text_rect, 5)
        screen.blit(self.quit_text, self.quit_text_rect)
        pygame.draw.rect(screen, 'red', self.quit_text_rect, 5)

        for gap, player in enumerate(sorted(players, key=lambda x: x.score, reverse=True)):
            player_icon_surf = player.image
            player_icon_rect = player_icon_surf.get_rect(
                topleft=(3*CELL_SIZE, (4+gap*2)*CELL_SIZE))
            screen.blit(player_icon_surf, player_icon_rect)
            score_text = self.pause_font.render(
                f": {player.score}", True, 'black')
            animal_count = self.pause_font.render(
                f"{player.num_caught_animals}", True, 'black')
            screen.blit(score_text, ((4*CELL_SIZE, (3.8+gap*2)*CELL_SIZE)))
            screen.blit(animal_count, ((9*CELL_SIZE, (3.8+gap*2)*CELL_SIZE)))
            screen.blit(
                self.paw_img, ((10.1*CELL_SIZE, (3.8+gap*2)*CELL_SIZE)))

        if dragon:
            if dragon.is_caught:
                congrat_text = self.pause_font.render(
                    f"DRAGON HAS BEEN CAUGHT BY {dragon.who_caught_me[0].capitalize()}", True, dragon.who_caught_me[1])
                congrat_text_rect = congrat_text.get_rect(
                    center=((BOARD_WIDTH*CELL_SIZE)//2, (CELL_SIZE*BOARD_HEIGHT//1.9)))
                screen.blit(congrat_text, congrat_text_rect)

    def game_intro(self, screen, selected_colors):
        intro_rect = pygame.Rect(
            0, 0, 26*CELL_SIZE, 19*CELL_SIZE)
        pygame.draw.rect(screen, (204, 156, 0), intro_rect)
        screen.blit(self.intro_img, self.intro_img_rect)
        screen.blit(self.intro_text, self.intro_text_rect)

        for p in self.selected_players:
            screen.blit(p['surf'], p['rect'])
            if p['color'] in selected_colors:
                pygame.draw.rect(screen, 'green', p['rect'], 5)
            else:
                pygame.draw.rect(screen, 'black', p['rect'], 5)
        screen.blit(self.play_text, self.play_text_rect)
        pygame.draw.rect(screen, 'black', self.play_text_rect, 5)
