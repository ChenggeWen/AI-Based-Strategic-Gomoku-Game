from board import Board


def test_board_constructor():
    rows = 6
    cols = 7
    board_width = 800
    board_height = 600
    margin = 20
    board = Board(rows, cols, board_width, board_height, margin)
    assert board.rows == rows
    assert board.cols == cols
    assert board.board_width == board_width
    assert board.board_height == board_height
    assert board.margin == margin


def test_place_stone():
    board = Board(6, 7, 800, 600, 20)
    assert board.place_stone(0, 0, "black")  # 第一次放置成功
    assert not board.place_stone(0, 0, "white")  # 同一位置第二次放置失败


def test_is_full():
    board = Board(3, 3, 300, 300, 20)
    board.place_stone(0, 0, "black")
    board.place_stone(0, 1, "white")
    board.place_stone(0, 2, "black")
    board.place_stone(1, 0, "white")
    board.place_stone(1, 1, "black")
    board.place_stone(1, 2, "white")
    board.place_stone(2, 0, "black")
    board.place_stone(2, 1, "white")
    board.place_stone(2, 2, "black")
    assert board.is_full() is True


def test_evaluate_score():
    board = Board(6, 7, 800, 600, 20)
    board.place_stone(0, 0, "black")
    board.place_stone(0, 1, "black")
    board.place_stone(0, 2, "black")
    board.place_stone(0, 3, "black")
    assert board.evaluate_score(0, 0, "black") == Board.FOUR_IN_ROW_SCORE/2


def test_get_empty_positions():
    board = Board(3, 3, 300, 300, 20)
    board.place_stone(0, 0, "black")
    board.place_stone(0, 1, "white")
    empty_positions = board.get_empty_positions()
    assert (0, 0) not in empty_positions
    assert (0, 1) not in empty_positions
    assert (0, 2) in empty_positions


def test_count_consecutive_stones():
    board = Board(6, 7, 800, 600, 20)
    board.place_stone(0, 0, "black")
    board.place_stone(0, 1, "black")
    board.place_stone(0, 2, "black")
    board.place_stone(0, 3, "black")
    assert board.count_consecutive_stones(0, 0, "black", 1, 0) == 0


def test_find_best_move():
    board = Board(6, 7, 800, 600, 20)
    board.place_stone(0, 0, "black")
    board.place_stone(0, 1, "black")
    board.place_stone(0, 2, "white")
    best_move = board.find_best_move("black")
    assert best_move == (1, 1)


def test_check_for_winner():
    board = Board(6, 7, 800, 600, 20)
    board.place_stone(0, 0, "black")
    board.place_stone(0, 1, "black")
    board.place_stone(0, 2, "black")
    board.place_stone(0, 3, "black")
    assert board.check_for_winner() is None
