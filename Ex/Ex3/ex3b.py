# 316493758
# 2

import numpy as np

SNAKES = [(27, 7), (36, 3), (50, 34), (59, 46), (66, 24), (73, 12), (76, 63), (89, 67), (97, 86), (99, 26)]
LADDERS = [(2, 23), (7, 29), (22, 41), (28, 77), (30, 32), (44, 58), (54, 69), (70, 90), (80, 83),
           (87, 93)]
END_CELL = 100


class SnakesAndLadders(object):

    def __init__(self, snakes_list, ladder_list):
        """
        Constructor
        :param snakes_list:     Snake list
        :param ladder_list:     Ladder List
        """
        self.snakes = SnakesAndLadders.list_to_dic(snakes_list)
        self.ladders = SnakesAndLadders.list_to_dic(ladder_list)
        self.probs = [1 / 6, 1 / 6, 1 / 6, 1 / 6, 1 / 6, 1 / 6]
        self.dice_values = [1, 2, 3, 4, 5, 6]

    @staticmethod
    def list_to_dic(lst):
        """
        Make tuple list to dictionary
        :param lst:     tuple list
        :return:        dictionary
        """
        result = {}
        for item in lst:
            result[item[0]] = item[1]
        return result

    def update_dice(self, prob_list):
        """
        Update dice probability
        :param prob_list:
        :return:
        """
        self.probs = prob_list

    def roll_dice(self):
        """
        Roll dice
        :return:    Dice result
        """
        return min(np.random.choice(a=self.dice_values, size=1, p=self.probs))

    def play_game(self):
        """
        Play game
        :return:    tuple of number of turns and all turns
        """
        won = False
        turn = 0
        current_position = 0
        rolls = []
        while turn < 900 and not won:
            turn += 1
            dice_value = self.roll_dice()
            rolls.append(dice_value)
            current_position += dice_value
            if current_position >= END_CELL:
                won = True
            elif current_position in self.ladders.keys():
                if self.roll_dice() < 4:
                    current_position = self.ladders[current_position]
            elif current_position in self.snakes:
                if self.roll_dice() > 3:
                    current_position = self.snakes[current_position]
        return turn, rolls
