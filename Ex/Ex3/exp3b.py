SNAKES = [(27, 7), (36, 3), (50, 34), (59, 46), (66, 24), (73, 12), (76, 63), (89, 67), (97, 86), (99, 26)]
LADDERS = [(2, 23), (7, 29), (22, 41), (28, 77), (30, 32), (44, 58), (54, 69), (70, 90), (80, 83),
           (87, 93)]


class SnakesAndLadders(object):

    def __init__(self, snakes_list, ladder_list):
        self.board = []
        self.snakes = snakes_list
        self.ladders = ladder_list
        self.probs = [1 / 6, 1 / 6, 1 / 6, 1 / 6, 1 / 6, 1 / 6]

    def update_dice(self, prob_list):
        if sum(prob_list) == 1:
            self.probs = prob_list

    def roll_dice(self):
        return

    def play_game(self):
        return

# if you want to initiate an instance of a game you can run this line:
# game = SnakesAndLadders(SNAKES, LADDERS)
# We defined SNAKES and LADDERS at the beginning of the file, so you could play with it
