import pandas as pd
import numpy as np
import pygame
import agent

# define global arguments for visual properties
WIDTH = 1200
HEIGHT = 800
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
RED = (255, 0, 0)
CYAN = (0, 255, 255)
YELLOW = (255, 255, 0)
GREY = (127, 127, 127)
TARGET_RIGHT = [(1000, 425), (1050, 425), (1050, 375), (1000, 375)]
TARGET_LEFT = [(200, 425), (250, 425), (250, 375), (200, 375)]
TEST_LENGTH = 10


def create_all_combinations(lst, num_of_repetitions):
    return num_of_repetitions * [(lst[i1], lst[i2]) for i1 in range(len(lst)) for i2 in range(i1 + 1, len(lst))]


class SimpleDecisionTask(object):
    def __init__(self, num_of_repetitions, manual_game=True, my_agent=None):
        # screen parameters
        pygame.init()
        size = WIDTH, HEIGHT
        self.screen = pygame.display.set_mode(size)
        self.font = pygame.font.SysFont("Arial", 20)
        self.colors = {'Blue': BLUE, "Red": RED, "Cyan": CYAN, "Yellow": YELLOW}

        # experiments parameters
        self.num_of_repetitions = num_of_repetitions
        self.manual_game = manual_game
        self.round_scores = []
        self.round_scores_titles = ["Round Index", "Reaction Time", "left color", "left reward in current trial",
                                    "right color", "right reward in current trial",
                                    "Clicked Key", "Reward"]
        self.between_trials_time = 500
        self.possible_probs = [0.1, 0.3, 0.7, 0.9]
        self.instruction_msg = "Put you fingers on the left and right keys. Click on one of them to start the game"
        self.won_msg = "You won 1 points :)"
        self.lost_msg = "You lost 1 points :("

        # update the probability of each color
        self.colors_prob = []
        self.update_color_probability()

        # randomly assign color for each round
        self.rounds = []
        self.init_rounds_configuration()
        self.num_of_rounds = len(self.rounds)

        # create agent if needed
        if not manual_game:
            self.agent = my_agent

    def update_color_probability(self):
        color_probs_vals = np.random.choice(self.possible_probs, size=len(self.colors), replace=False)
        self.colors_prob = dict(zip(self.colors.keys(), color_probs_vals))

    def init_rounds_configuration(self):
        self.rounds = create_all_combinations(list(self.colors.keys()), self.num_of_repetitions)

    def display_text_on_screen(self, text_str):
        text = self.font.render(text_str, True, GREY, BLACK)
        textrect = text.get_rect()
        textrect.centerx = self.screen.get_rect().centerx
        textrect.centery = self.screen.get_rect().centery
        self.screen.blit(text, textrect)
        pygame.display.flip()

    def wait_for_left_right_press(self):
        pygame.event.clear()
        continue_flag = True
        while continue_flag:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN or event.type == pygame.KEYUP:
                    if event.key == pygame.K_LEFT:
                        cur_key = "left"
                        continue_flag = False
                    if event.key == pygame.K_RIGHT:
                        cur_key = "right"
                        continue_flag = False
        pygame.event.clear()
        return cur_key

    def start_instruction_screen(self):
        self.display_text_on_screen(self.instruction_msg)
        # Wait for a response only if manual game
        if self.manual_game:
            self.wait_for_left_right_press()
        pygame.time.delay(self.between_trials_time)

    def run_round(self, round_index):
        cur_round = self.rounds[round_index]
        # change the sides of the colors randomly
        flag_first_color_is_left = np.random.choice([0, 1], 1)[0]
        if not flag_first_color_is_left:
            cur_round = (cur_round[1], cur_round[0])

        # sample the reward for each color
        left_color_reward = np.random.choice([0, 1], 1, p=[1 - self.colors_prob[cur_round[0]],
                                                           self.colors_prob[cur_round[0]]])[0]
        right_color_reward = np.random.choice([0, 1], 1, p=[1 - self.colors_prob[cur_round[1]],
                                                            self.colors_prob[cur_round[1]]])[0]

        # present two options after short delay
        trial_clock = pygame.time.Clock()
        self.screen.fill(BLACK)
        pygame.display.flip()

        # present target
        pygame.draw.polygon(self.screen, self.colors[cur_round[0]], TARGET_LEFT)
        pygame.draw.polygon(self.screen, self.colors[cur_round[1]], TARGET_RIGHT)
        pygame.display.flip()

        # wait for participant input
        if self.manual_game:
            cur_key = self.wait_for_left_right_press()
        else:
            cur_key = self.agent.make_decision(cur_round[0], cur_round[1])

        # present the reward
        if (cur_key == "left" and left_color_reward == 1) or (cur_key == "right" and right_color_reward == 1):
            self.display_text_on_screen(self.won_msg)
            cur_reward = 1
        else:
            self.display_text_on_screen(self.lost_msg)
            cur_reward = -1

        # if agent playing send it the reward
        if not self.manual_game:
            self.agent.get_reward(cur_reward)

        # save the relevant information to the round scores list
        self.round_scores.append(
            [round_index, trial_clock.tick(),
             cur_round[0], left_color_reward, cur_round[1], right_color_reward,
             cur_key, cur_reward])

        # wait time between trials
        pygame.time.delay(self.between_trials_time)

        # clear the keys
        pygame.event.clear()

    def get_results(self):
        """ save CSV file of the results stored in the round_scores attribute"""
        return pd.DataFrame(data=self.round_scores, columns=self.round_scores_titles)

    def start_exp(self):
        # start the game screen
        self.start_instruction_screen()

        # start the rounds of the game
        for round_index in range(self.num_of_rounds):
            self.run_round(round_index)


def test_agent(agent_instance):
    game_object = SimpleDecisionTask(num_of_repetitions=30,
                                     manual_game=False,
                                     my_agent=agent_instance)

    results = get_result_after_n_times(game_object)
    return [max(results), sum(results) / len(results)]


def get_result_after_n_times(game):
    results = []
    for i in range(100):
        game.start_exp()
        results.append(game.get_results()["Reward"].sum())
    return results


if __name__ == "__main__":
    game = SimpleDecisionTask(num_of_repetitions=30, manual_game=False,
                              my_agent=agent.ComparingColorsAgent())  # Agent mode

    print(test_agent(agent.RandomAgent()))
    print(test_agent(agent.ComparingColorsAgent()))
    print(test_agent(agent.ColorBasedAgent()))
    # game = SimpleDecisionTask(num_of_repetitions=20, manual_game=True) # Manual mode
    # game.start_exp()
    # df = game.get_results()
    # output_path = r"your_path_output.csv"
    # df.to_csv(output_path)
    # print("The score in this run is %f." % df["Reward"].sum())
