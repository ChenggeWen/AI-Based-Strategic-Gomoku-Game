import random

from board import Board
from game import Game

WIDTH = 800
HEIGHT = 800
rows = 15
cols = 15
board_width = 700
board_height = 700
margin = 50
wait = 50
is_game_over = False
player_name = None

board = Board(rows, cols, board_width, board_height, margin)
game = Game()


def setup():
    # global player_name
    # player_name = input('enter your name')
    # if player_name:
    #     print('hi ' + player_name)
    # elif player_name == '':
    #     print('[empty string]')
    # else:
    #     print(player_name)
    size(WIDTH, HEIGHT)
    colorMode(RGB, 1)
    background(0.75, 0.6, 0.2)


def draw():
    global wait
    global is_game_over
    global player_name
    board.display_board()
    board.draw_stones()

    winner = board.check_for_winner()

    if winner or board.is_full():
        game.game_over(winner, player_name)
        is_game_over = True
        return

    if game.current_player == "white":
        if wait == 0:
            ai_move()
            wait = 50
        elif wait > 0:
            wait -= 1
    # if board.is_full():
    #     game.game_over()


def mousePressed():
    global is_game_over
    if is_game_over:
        return
    if game.current_player == "black":
        row, col = board.is_near_intersection(mouseX, mouseY)
        if row is not None and col is not None:
            if board.place_stone(row, col, "black"):

                game.switch_player()


def ai_move():
    best_move = board.find_best_move("white")
    if best_move:
        board.place_stone(best_move[0], best_move[1], "white")
        game.switch_player()
    else:
        empty_positions = board.get_empty_positions()
        if empty_positions:
            row, col = random.choice(empty_positions)
            board.place_stone(row, col, "white")
            game.switch_player()
