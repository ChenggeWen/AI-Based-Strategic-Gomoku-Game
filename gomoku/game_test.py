from game import Game


def test_game_constructor():
    game = Game()
    assert game.current_player == "black"
    assert not game.name_check


def test_switch_player():
    game = Game()
    game.switch_player()
    assert game.current_player == "white"
    game.switch_player()
    assert game.current_player == "black"


def test_update_scores():
    game = Game()
    game.write_scores({"Player1": 5, "Player2": 3})
    game.update_scores("Player1")
    scores = game.read_scores()
    assert scores["Player1"] == 6
