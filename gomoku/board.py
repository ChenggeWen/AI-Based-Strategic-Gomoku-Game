
class Board:
    WINNING_SCORE = 1000
    FOUR_IN_ROW_SCORE = 400
    BLOCK_FOUR_IN_ROW_SCORE = 500
    THREE_IN_ROW_SCORE = 200
    BLOCK_THREE_IN_ROW_SCORE = 300
    TWO_IN_ROW_SCORE = 50
    BLOCK_TWO_IN_ROW_SCORE = 100
    SOME_SCORE_FOR_ONE_IN_ROW = 10
    SOME_SCORE_FOR_BLOCKING_ONE_IN_ROW = 30

    def __init__(self, rows, cols, board_width, board_height, margin):
        self.rows = rows
        self.cols = cols
        self.board_width = board_width
        self.board_height = board_height
        self.size = board_width/(cols-1)
        self.margin = margin
        self.stones = [[None for _ in range(cols)] for _ in range(rows)]

    def display_board(self):
        """
        draw the board
        """
        stroke(0)
        strokeWeight(6)

        for i in range(self.rows):
            line(self.margin, self.margin+self.size*i,
                 self.margin+self.board_width,
                 self.margin+self.size*i)
        for j in range(self.cols):
            line(self.margin + self.size*j, self.margin,
                 self.margin + self.size*j,
                 self.margin + self.board_height)

    def is_near_intersection(self, x, y):
        """
        check whether the stone is near the intersection
        """
        for row in range(self.rows):
            for col in range(self.cols):
                intersection_x = self.margin + col*self.size
                intersection_y = self.margin + row*self.size

                distance = ((
                    (x - intersection_x) ** 2
                    + (y - intersection_y) ** 2) ** 0.5
                            )
                if distance < self.size/2:
                    return row, col
        return None, None

    def place_stone(self, row, col, color):
        """
       place stone
        """
        if self.stones[row][col] is None:
            self.stones[row][col] = color
            return True
        return False

    def draw_stones(self):
        """
        draw stones on board
        """
        for row in range(self.rows):
            for col in range(self.cols):
                if self.stones[row][col] is not None:
                    if self.stones[row][col] == "black":
                        fill(0)
                    elif self.stones[row][col] == "white":
                        fill(1)
                    strokeWeight(2)
                    ellipse(
                        self.margin + col*self.size,
                        self.margin + row*self.size,
                        self.size*0.8,
                        self.size*0.8
                            )

    def is_full(self):
        """
        check whether the board is full
        """
        for row in range(self.rows):
            for col in range(self.cols):
                if self.stones[row][col] is None:
                    return False
        return True

    def get_empty_positions(self):
        """
        return all empty positions
        """
        empty_positions = []
        for row in range(self.rows):
            for col in range(self.cols):
                if self.stones[row][col] is None:
                    empty_positions.append((row, col))
        return empty_positions

    def count_consecutive_stones(self, row, col, color, d_row, d_col):
        """
        for AI judgment
        """
        count = 0

        for i in range(1, 5):
            new_row = row + d_row * i
            new_col = col + d_col * i
            if not (0 <= new_row < self.rows and 0 <= new_col < self.cols):
                break
            if self.stones[new_row][new_col] == color:
                count += 1
            else:
                break

        for i in range(1, 5):
            new_row = row - d_row * i
            new_col = col - d_col * i
            if not (0 <= new_row < self.rows and 0 <= new_col < self.cols):
                break
            if self.stones[new_row][new_col] == color:
                count += 1
            else:
                break

        return count

    def evaluate_score(self, row, col, color):
        score = 0
        for d_row, d_col in [(1, 0), (0, 1), (1, 1), (-1, 1)]:
            count = self.count_consecutive_stones(row,
                                                  col,
                                                  color,
                                                  d_row,
                                                  d_col)
            if count == 4:
                score += self.FOUR_IN_ROW_SCORE
            elif count == 3:
                score += self.THREE_IN_ROW_SCORE
            elif count == 2:
                score += self.TWO_IN_ROW_SCORE
            elif count == 1:
                score += self.SOME_SCORE_FOR_ONE_IN_ROW

            opponent_color = "black" if color == "white" else "white"
            opponent_count = self.count_consecutive_stones(row, col,
                                                           opponent_color,
                                                           d_row, d_col)
            if opponent_count == 4:
                score += self.BLOCK_FOUR_IN_ROW_SCORE
            elif opponent_count == 3:
                score += self.BLOCK_THREE_IN_ROW_SCORE
            elif opponent_count == 2:
                score += self.BLOCK_TWO_IN_ROW_SCORE
            elif opponent_count == 1:
                score += self.SOME_SCORE_FOR_BLOCKING_ONE_IN_ROW

        return score

    def find_best_move(self, color):
        best_score = -1
        best_move = None
        for row in range(self.rows):
            for col in range(self.cols):
                if self.stones[row][col] is None:
                    score = self.evaluate_score(row, col, color)
                    if score > best_score:
                        best_score = score
                        best_move = (row, col)
        return best_move

    def check_for_winner(self):
        for row in range(self.rows):
            for col in range(self.cols):
                if self.stones[row][col] is not None:
                    color = self.stones[row][col]
                    for d_row, d_col in [(1, 0), (0, 1), (1, 1), (-1, 1)]:
                        if self.count_consecutive_stones(row, col,
                                                         color,
                                                         d_row, d_col) == 4:
                            return color
        return None
