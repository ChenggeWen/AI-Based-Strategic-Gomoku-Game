class Game:
    def __init__(self):
        self.current_player = "black"
        self.name_check = False

    def switch_player(self):
        if self.current_player == "black":
            self.current_player = "white"
        else:
            self.current_player = "black"

    # def game_over(self):
    #     fill(1)
    #     textSize(50)
    #     textAlign(CENTER, CENTER)
    #     text("Game Over", width / 2, height / 2)

    def game_over(self, winner_color=None, player_name=None):
        fill(0, 1, 0.8)
        textSize(100)
        textAlign(CENTER, CENTER)
        if winner_color:
            text(winner_color + " Wins!", width / 2, height / 2)
            if winner_color == "black" and not self.name_check:
                player_name = self.input("Enter your name:")
                if player_name:
                    self.update_scores(player_name)
                    self.name_check = True
        else:
            text("Game Over", width / 2, height / 2)

    def read_scores(self):
        scores = {}
        try:
            with open('scores.txt', 'r') as file:
                for line in file:
                    name, score = line.strip().split()
                    scores[name] = int(score)
        except IOError:
            scores = {}
        return scores

    def write_scores(self, scores):
        with open('scores.txt', "w") as file:
            for name, score in sorted(scores.items(),
                                      key=lambda x:
                                          x[1], reverse=True):
                file.write(name + " " + str(score) + "\n")

    def update_scores(self, player_name):
        scores = self.read_scores()
        scores[player_name] = scores.get(player_name, 0) + 1
        self.write_scores(scores)

    def input(self, message=''):
        from javax.swing import JOptionPane
        return JOptionPane.showInputDialog(frame, message)
