import numpy as np


class Agent(object):
    """
    The Class mimic behavior of a participant taking part in the color choosing game.
    """

    def __init__(self):
        pass

    def make_decision(self, left_color, right_color):
        """
        The method decides which color to chose.
        :param left_color: the color appearing on the left side - string.
        :param right_color: the color appearing on the right side - string.
        :return: whether left or right is chosen - string "left" \ "right".
        """
        pass

    def get_reward(self, reward):
        """
        The method receive the reward from the experiment.
        The agent can use this information for future decisions.
        :param reward: the reward given for the previous round.
        :return: does not return anything.
        """
        pass


class RandomAgent(Agent):
    def __init__(self):
        super().__init__()

    def make_decision(self, left_color, right_color):
        self.last_choice = np.random.choice([0, 1], 1, p=[0.5, 0.5])[0]
        return ["left", "right"][self.last_choice]

    def get_reward(self, reward):
        pass


class ComparingColorsAgent(Agent):
    def __init__(self):
        super().__init__()
        # initiation of memory parameters and alpha
        self.stats_table = {}
        self.last_choice = None
        self.last_left_color = None
        self.last_right_color = None
        self.alpha = 0.2

    def make_decision(self, left_color, right_color):
        # set the last decision in order to use it in the reward processing stage
        self.last_left_color = left_color
        self.last_right_color = right_color
        # create the color-coupling parameter if not included in the agent's memory
        # or if the value known to the agent is 0.5.
        if (left_color, right_color) not in self.stats_table \
                or self.stats_table[(left_color, right_color)] == 0.5:
            self.stats_table[(left_color, right_color)] = 0.5
            self.stats_table[(right_color, left_color)] = 0.5
            self.last_choice = np.random.choice([0, 1], 1, p=[0.5, 0.5])[0]

        # if the color-coupling known to the agent
        else:
            self.last_choice = int(self.stats_table[(left_color, right_color)] > 0.5)

        # return the decision
        return ["left", "right"][self.last_choice]

    def get_reward(self, reward):
        # the current color-coupling (Environment)
        key = (self.last_left_color, self.last_right_color)
        # if we choose the color on the right side(1) -> positive point should teach us to choose right(1).
        if self.last_choice == 1:
            self.stats_table[key] = (1 - self.alpha) * self.stats_table[key] + self.alpha * reward
        # if we choose the color on the left side(0) -> positive point should teach us to choose left(0).
        # therefore we use - self.alpha * reward
        else:
            self.stats_table[key] = (1 - self.alpha) * self.stats_table[key] - self.alpha * reward

        # keep the probabilities between 0 and 1
        if self.stats_table[key] > 1:
            self.stats_table[key] = 1
        if self.stats_table[key] < 0:
            self.stats_table[key] = 0

        # update the state of the opposite sides
        self.stats_table[(key[1], key[0])] = 1 - self.stats_table[key]