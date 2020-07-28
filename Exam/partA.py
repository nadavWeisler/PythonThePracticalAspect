# 316493758
# 3

import pandas as pd


# Question 1
def is_palindrome(my_str):
    """
    Recursive palindrome validator
    :param my_str:  String
    :return:        Boolean
    """
    my_str = my_str.lower()
    if len(my_str) <= 1:
        return True
    else:
        if my_str[0] != my_str[-1]:
            return False
        else:
            return is_palindrome(my_str[1:-1])


# Question 2
class EvenNumber(object):
    """
    Class for even numbers
    """
    def __init__(self, value):
        """
        Constructor
        :param value:   Int
        """
        self.multiple_with = 2
        self.value_error_msg = "Number is bigger or equal to 100 or not divided by 2"
        self.type_error_msg = "Type of value should be integer"
        if not isinstance(value, int):
            raise TypeError(self.type_error_msg)
        if self._check_new_value_by_multiple_with(value) and \
                100 > value > 0:
            self.value = value
        else:
            raise ValueError(self.value_error_msg)

    def _check_new_value_by_multiple_with(self, value):
        """
        Check if value is multiply by multiple_with
        :param value:   Int
        :return:        Boolean
        """
        return value % self.multiple_with == 0

    def add_number(self, value):
        """
        Add number to self.value
        :param value:   Int
        :return:        Boolean
        """
        if value % self.multiple_with != 0:
            return False
        elif self.value + value >= 100 or self.value + value <= 0:
            return False
        else:
            self.value += value
            return True


class MultiplesOfSix(EvenNumber):
    """
    Class for multiples of 6, inherit from EvenNumber
    """
    def __init__(self, value):
        """
        Constructor
        :param value:   Int
        """
        try:
            super().__init__(value)
            self.multiple_with = 6
            if not self._check_new_value_by_multiple_with:
                raise ValueError()
        except ValueError:
            self.error_msg = "Number is bigger or equal to 100 or not divided by 6"
            raise ValueError(self.error_msg)


# Question 3
def traded_players_points_per_game(csv_dir, team_letters):
    """
    Get pandas data frame of traded players points during the playoff
    :param csv_dir:         Csv files directory
    :param team_letters:    Team letters(3 letter start with capital)
    :return:                Pandas data frame
    """
    try:
        playoff_team_df = pd.read_csv(csv_dir + "\\Playoff_" + team_letters + ".csv")
    except FileNotFoundError:
        return

    players = playoff_team_df["FULL NAME"].unique()

    regular_season_path = csv_dir + "\\Regular_season.csv"
    reg_df = pd.read_csv(regular_season_path)
    reg_df = reg_df[reg_df["FULL NAME"].isin(players)]
    reg_df = reg_df[reg_df['FULL NAME'].map(reg_df['FULL NAME'].value_counts()) > 2]
    players = reg_df["FULL NAME"].unique()

    playoff_team_df = playoff_team_df[playoff_team_df["FULL NAME"].isin(players)]
    playoff_team_df = playoff_team_df.drop(['TEAM'], axis=1)
    playoff_team_df.groupby(['FULL NAME']).mean()
    playoff_team_df.sort_values(by=['POINTS PER GAME'], ascending=False)
    playoff_team_df = playoff_team_df.reset_index()
    playoff_team_df = playoff_team_df.drop(["index"], axis=1)
    return playoff_team_df
