import pygame
from board import Board
from animal import Animal
from player import Player
from dragon import Dragon
from ui import UI
from pygame.math import Vector2
import random
from constants import CELL_SIZE, BOARD_WIDTH, BOARD_HEIGHT, A_COLORS, ANIMAL_PICTURES, FORBIDDEN_BLOCKS
import sys


pygame.init()


def set_for_new_game():
    global dragon
    for animal in animals:
        animal.who_caught_me = None
        animal.is_caught = False
    players.clear()
    selected_colors.clear()
    dragon = None
    pygame.time.set_timer(dragon_animation_timer,
                          random.randint(10000, 12000))
    board.game_paused = False
    board.game_on = False
    bg_music.play(-1)


screen = pygame.display.set_mode(
    (CELL_SIZE*BOARD_WIDTH, CELL_SIZE*BOARD_HEIGHT))
board = Board()
ui = UI()
dragon = None
icon = pygame.image.load('graphics/panther.png').convert_alpha()
pygame.display.set_icon(icon)
pygame.display.set_caption('CAPTURE ALL!')

clock = pygame.time.Clock()

capture_sound = pygame.mixer.Sound('sounds/shot.mp3')
capture_sound.set_volume(0.03)
bg_music = pygame.mixer.Sound('sounds/background_music.mp3')
bg_music.set_volume(0.2)
bg_music.play(-1)


animals = [Animal(100, Vector2(0, 0),
                  A_COLORS['green'], ANIMAL_PICTURES['albatross']),
           Animal(300, Vector2(2, 0),
                  A_COLORS['orange'], ANIMAL_PICTURES['sealion']),
           Animal(300, Vector2(5, 0),
                  A_COLORS['orange'], ANIMAL_PICTURES['penguin']),
           Animal(300, Vector2(9, 0),
                  A_COLORS['orange'], ANIMAL_PICTURES['reindeer']),
           Animal(300, Vector2(17, 0),
                  A_COLORS['orange'], ANIMAL_PICTURES['wolf']),
           Animal(300, Vector2(24, 0),
                  A_COLORS['orange'], ANIMAL_PICTURES['moose']),
           Animal(200, Vector2(12, 1),
                  A_COLORS['skin'], ANIMAL_PICTURES['otter']),
           Animal(200, Vector2(14, 1),
                  A_COLORS['skin'], ANIMAL_PICTURES['lynx']),
           Animal(300, Vector2(21, 1),
                  A_COLORS['orange'], ANIMAL_PICTURES['arcticfox']),
           Animal(200, Vector2(25, 1),
                  A_COLORS['skin'], ANIMAL_PICTURES['sable']),
           Animal(600, Vector2(6, 2),
                  A_COLORS['brown'], ANIMAL_PICTURES['polarbear']),
           Animal(200, Vector2(13, 2),
                  A_COLORS['skin'], ANIMAL_PICTURES['boar']),
           Animal(600, Vector2(1, 3),
                  A_COLORS['brown'], ANIMAL_PICTURES['grizzly']),
           Animal(300, Vector2(3, 3),
                  A_COLORS['orange'], ANIMAL_PICTURES['walrus']),
           Animal(300, Vector2(10, 3),
                  A_COLORS['orange'], ANIMAL_PICTURES['damdeer']),
           Animal(500, Vector2(18, 3),
                  A_COLORS['pink'], ANIMAL_PICTURES['brownbear']),
           Animal(200, Vector2(4, 4),
                  A_COLORS['skin'], ANIMAL_PICTURES['eagle']),
           Animal(200, Vector2(9, 4),
                  A_COLORS['skin'], ANIMAL_PICTURES['goat']),
           Animal(200, Vector2(15, 4),
                  A_COLORS['skin'], ANIMAL_PICTURES['roedeer']),
           Animal(100, Vector2(19, 4),
                  A_COLORS['green'], ANIMAL_PICTURES['heron']),
           Animal(300, Vector2(23, 4),
                  A_COLORS['orange'], ANIMAL_PICTURES['yak']),
           Animal(600, Vector2(0, 5),
                  A_COLORS['brown'], ANIMAL_PICTURES['bison']),
           Animal(100, Vector2(7, 5),
                  A_COLORS['green'], ANIMAL_PICTURES['hare']),
           Animal(100, Vector2(12, 5),
                  A_COLORS['green'], ANIMAL_PICTURES['pheasant']),
           Animal(200, Vector2(20, 5),
                  A_COLORS['skin'], ANIMAL_PICTURES['caucasiangoat']),
           Animal(200, Vector2(21, 5),
                  A_COLORS['skin'], ANIMAL_PICTURES['mouflon']),
           Animal(200, Vector2(4, 6),
                  A_COLORS['skin'], ANIMAL_PICTURES['fox']),
           Animal(100, Vector2(14, 6),
                  A_COLORS['green'], ANIMAL_PICTURES['marabou']),
           Animal(300, Vector2(10, 7),
                  A_COLORS['orange'], ANIMAL_PICTURES['jackal']),
           Animal(300, Vector2(16, 7),
                  A_COLORS['orange'], ANIMAL_PICTURES['crane']),
           Animal(800, Vector2(18, 7),
                  A_COLORS['gray'], ANIMAL_PICTURES['tiger']),
           Animal(100, Vector2(23, 7),
                  A_COLORS['green'], ANIMAL_PICTURES['crane_2']),
           Animal(100, Vector2(0, 8),
                  A_COLORS['green'], ANIMAL_PICTURES['armadillo']),
           Animal(100, Vector2(2, 8),
                  A_COLORS['green'], ANIMAL_PICTURES['owl']),
           Animal(300, Vector2(6, 8),
                  A_COLORS['orange'], ANIMAL_PICTURES['reddeer']),
           Animal(100, Vector2(13, 8),
                  A_COLORS['green'], ANIMAL_PICTURES['hyena']),
           Animal(500, Vector2(15, 8),
                  A_COLORS['pink'], ANIMAL_PICTURES['hippo']),
           Animal(200, Vector2(21, 8),
                  A_COLORS['skin'], ANIMAL_PICTURES['bezoargoat']),
           Animal(300, Vector2(25, 8),
                  A_COLORS['orange'], ANIMAL_PICTURES['tapir']),
           Animal(200, Vector2(8, 9),
                  A_COLORS['skin'], ANIMAL_PICTURES['wild-boar']),
           Animal(1000, Vector2(12, 9),
                  A_COLORS['red'], ANIMAL_PICTURES['lion']),
           Animal(200, Vector2(1, 10),
                  A_COLORS['skin'], ANIMAL_PICTURES['skunk']),
           Animal(400, Vector2(5, 10),
                  A_COLORS['blue'], ANIMAL_PICTURES['turtle']),
           Animal(100, Vector2(7, 10),
                  A_COLORS['green'], ANIMAL_PICTURES['howler-monkey']),
           Animal(500, Vector2(9, 10),
                  A_COLORS['pink'], ANIMAL_PICTURES['gorilla']),
           Animal(200, Vector2(14, 10),
                  A_COLORS['skin'], ANIMAL_PICTURES['antelope']),
           Animal(100, Vector2(19, 10),
                  A_COLORS['green'], ANIMAL_PICTURES['pelican']),
           Animal(600, Vector2(25, 10),
                  A_COLORS['brown'], ANIMAL_PICTURES['indianrhino']),
           Animal(600, Vector2(16, 11),
                  A_COLORS['brown'], ANIMAL_PICTURES['whiterhino']),
           Animal(100, Vector2(18, 11),
                  A_COLORS['green'], ANIMAL_PICTURES['flamingo']),
           Animal(400, Vector2(22, 11),
                  A_COLORS['blue'], ANIMAL_PICTURES['cobra']),
           Animal(200, Vector2(2, 12),
                  A_COLORS['skin'], ANIMAL_PICTURES['polecat']),
           Animal(800, Vector2(5, 12),
                  A_COLORS['gray'], ANIMAL_PICTURES['leopard']),
           Animal(800, Vector2(12, 12),
                  A_COLORS['gray'], ANIMAL_PICTURES['elephant']),
           Animal(100, Vector2(20, 12),
                  A_COLORS['green'], ANIMAL_PICTURES['crocodile']),
           Animal(200, Vector2(24, 12),
                  A_COLORS['skin'], ANIMAL_PICTURES['pangolin']),
           Animal(200, Vector2(6, 13),
                  A_COLORS['skin'], ANIMAL_PICTURES['sloth']),
           Animal(200, Vector2(10, 13),
                  A_COLORS['skin'], ANIMAL_PICTURES['okapi']),
           Animal(300, Vector2(17, 13),
                  A_COLORS['orange'], ANIMAL_PICTURES['kudu']),
           Animal(200, Vector2(25, 13),
                  A_COLORS['skin'], ANIMAL_PICTURES['red-panda']),
           Animal(300, Vector2(8, 14),
                  A_COLORS['orange'], ANIMAL_PICTURES['chimpanzee']),
           Animal(400, Vector2(16, 14),
                  A_COLORS['blue'], ANIMAL_PICTURES['gnu']),
           Animal(200, Vector2(0, 15),
                  A_COLORS['skin'], ANIMAL_PICTURES['racoon']),
           Animal(200, Vector2(5, 15),
                  A_COLORS['skin'], ANIMAL_PICTURES['bongo']),
           Animal(400, Vector2(9, 15),
                  A_COLORS['blue'], ANIMAL_PICTURES['zebra']),
           Animal(400, Vector2(12, 15),
                  A_COLORS['blue'], ANIMAL_PICTURES['giraffe']),
           Animal(200, Vector2(14, 15),
                  A_COLORS['skin'], ANIMAL_PICTURES['beizaantelope']),
           Animal(300, Vector2(21, 15),
                  A_COLORS['orange'], ANIMAL_PICTURES['warthog']),
           Animal(400, Vector2(3, 16),
                  A_COLORS['blue'], ANIMAL_PICTURES['blackbear']),
           Animal(200, Vector2(19, 16),
                  A_COLORS['skin'], ANIMAL_PICTURES['gazelle']),
           Animal(100, Vector2(24, 16),
                  A_COLORS['green'], ANIMAL_PICTURES['badger']),
           Animal(300, Vector2(0, 17),
                  A_COLORS['orange'], ANIMAL_PICTURES['condor']),
           Animal(200, Vector2(13, 17),
                  A_COLORS['skin'], ANIMAL_PICTURES['nyala']),
           Animal(400, Vector2(4, 18),
                  A_COLORS['blue'], ANIMAL_PICTURES['anteater']),
           Animal(300, Vector2(11, 18),
                  A_COLORS['orange'], ANIMAL_PICTURES['ostrich']),
           Animal(400, Vector2(12, 18),
                  A_COLORS['blue'], ANIMAL_PICTURES['buffalo']),
           Animal(600, Vector2(15, 18),
                  A_COLORS['brown'], ANIMAL_PICTURES['blackpanther']),
           Animal(200, Vector2(20, 18),
                  A_COLORS['skin'], ANIMAL_PICTURES['javorantelope']),
           Animal(200, Vector2(23, 18),
                  A_COLORS['skin'], ANIMAL_PICTURES['aardvark']),
           Animal(400, Vector2(25, 18),
                  A_COLORS['blue'], ANIMAL_PICTURES['kangaroo'])]
animal_poses = [i.pos for i in animals]
dragon_animation_timer = pygame.USEREVENT + 1
pygame.time.set_timer(dragon_animation_timer,
                      random.randint(10000, 12000))

selected_colors = []
starting_ids = []
players = []
players_that_caught_limit = []
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == dragon_animation_timer and board.game_on and not board.game_paused and len([a for a in animals if a.is_caught == True]) > 14:
            occupied_positions = [p.pos for p in players] + \
                animal_poses + FORBIDDEN_BLOCKS

            if dragon:
                new_pos = dragon.pos
                while new_pos == dragon.pos or new_pos in occupied_positions:
                    new_pos = dragon.generate_new_pos()
                dragon.start_move(new_pos)
            else:
                dragon = Dragon()
                while dragon.pos in occupied_positions:
                    dragon.update_pos()
                dragon.dragon_roar.play()

        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            m_pos = pygame.mouse.get_pos()
            any_player_moving = any(p.is_moving for p in players)

            if board.game_on and not board.game_paused and not any_player_moving:
                to_move = Vector2(
                    m_pos[0]//board.cell_size, m_pos[1]//board.cell_size)
                for i, player, in enumerate(players):
                    if player.his_turn and to_move not in [p.pos for p in players] and to_move in player.next_moves:
                        player.start_move(to_move)
                        if dragon:
                            player.check_capture(
                                animals, capture_sound, dragon_animation_timer, dragon)
                        else:
                            player.check_capture(
                                animals, capture_sound)
                        player.his_turn = False
                        next_turn_idx = (i + 1) % len(players)
                        players[next_turn_idx].his_turn = True
                        break
            elif not board.game_on:
                for p in ui.selected_players:
                    if p['rect'].collidepoint(m_pos):
                        if p['color'] in selected_colors:
                            selected_colors.remove(p['color'])
                        else:
                            selected_colors.append(p['color'])

                if ui.play_text_rect.collidepoint(m_pos) and len(selected_colors) > 0:
                    starting_ids = random.sample(
                        range(0, 8), len(selected_colors))
                    for idx, color_data in enumerate(selected_colors):
                        p = Player(
                            color_data, starting_ids[idx], _his_turn=(idx == 0))
                        players.append(p)
                    board.game_on = True
            elif board.game_on and board.game_paused:
                if ui.quit_text_rect.collidepoint(m_pos):
                    pygame.quit()
                    sys.exit()
                elif ui.restart_text_rect.collidepoint(m_pos):
                    bg_music.stop()
                    set_for_new_game()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and board.game_on:
                board.game_paused = not board.game_paused
    if board.game_on:
        board.draw_board(screen)
        for animal in animals:
            animal.draw_animal(screen)
        for player in players:
            player.update_animation()
            player.draw_player(screen)
            player.possible_moves(
                screen, players, animal_poses)
        if dragon:
            if not board.game_paused:
                dragon.update_animation()
            dragon.draw_dragon(screen)
            if dragon.is_caught:
                bg_music.stop()
                board.game_paused = True
        if board.game_paused:
            ui.pause_game(screen, players, dragon)
    else:
        ui.game_intro(screen, selected_colors)
    pygame.display.update()
    clock.tick(60)
