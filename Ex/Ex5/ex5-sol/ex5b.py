# 316493758
# 4

import os
import pandas as pd

FRIENDS_SEASONS_CSV = ["friends_imdb_episode_season_1.csv",
                       "friends_imdb_episode_season_2.csv",
                       "friends_imdb_episode_season_3.csv",
                       "friends_imdb_episode_season_4.csv",
                       "friends_imdb_episode_season_5.csv",
                       "friends_imdb_episode_season_6.csv",
                       "friends_imdb_episode_season_7.csv",
                       "friends_imdb_episode_season_8.csv",
                       "friends_imdb_episode_season_9.csv",
                       "friends_imdb_episode_season_10.csv"]

QUOTES_CSV = "friends_quotes.csv"
RATING_CSV = "rating_all_imdb.csv"

EPISODE_ID = "tconst"
SEASON_NUMBER = "seasonNumber"
EPISODE_NUMBER = "episodeNumber"
ALL_VALUE = "All"
QUOTES_COLUMN = "quote"
VOTE_COUNT = "numVotes"
AVG_RATING = "averageRating"

SEASON_COLUMNS_QUOTES = "season"
EPISODE_NUMBER_COLUMNS_QUOTES = "episode_number"
AUTHOR_COL = "author"
NUMBER_OF_LINES = "number of lines"
RESULT_SEASON_NUMBER = "season number"
RESULT_EPISODE = "episode number"
RESULT_CHARACTER = "character name"


def get_only_friends_rating(csv_folder):
    """
    Get rating of only friends episodes
    :param csv_folder:      Folder contain our csv file
    :return:                Data frame
    """
    rating_df = get_df_from_filename_and_folder(csv_folder, RATING_CSV)
    episode_df = get_all_episodes_df_and_episode_count(csv_folder)[0]
    merge_df = rating_df.merge(episode_df, on=EPISODE_ID, how="inner")
    return merge_df


def get_all_episodes_df_and_episode_count(csv_folder):
    """
    Get all episode data frame and dictionary contains episode count
    :param csv_folder:          Folder of our csv files
    :return:                    Data frame
    """
    df = pd.DataFrame()
    season_episode_count = {}
    season_count = 1
    for season_csv in FRIENDS_SEASONS_CSV:
        season_df = get_df_from_filename_and_folder(csv_folder, season_csv)
        season_episode_count[season_count] = season_df.shape[0]
        season_count += 1
        df = pd.concat([df, season_df[[EPISODE_ID, SEASON_NUMBER, EPISODE_NUMBER]]])
    return df, season_episode_count


def get_file_path(folder, file):
    """
    Get file full path from directory and file
    :param folder:      Folder path
    :param file:        File name
    :return:            Full path
    """
    return os.path.join(folder, file)


def get_episode_and_season_from_id(episode_id, csv_folder):
    """
    Get episode season numbers of episode id
    :param episode_id:          Episode id
    :param csv_folder:          Folder of our csv files
    :return:                    Episode and season numbers
    """
    df = get_all_episodes_df_and_episode_count(csv_folder)[0]
    df = df[df[EPISODE_ID] == episode_id]
    return df[SEASON_NUMBER].values[0], df[EPISODE_NUMBER].values[0]


def create_season_rating(csv_folder):
    """
    Create season ranking
    :param csv_folder:      Folder of our csv files
    :return:                Data frame
    """
    rating_df = get_only_friends_rating(csv_folder)
    rating_df[AVG_RATING] = (rating_df[AVG_RATING] * rating_df[VOTE_COUNT])

    resDf = rating_df.drop([EPISODE_ID], axis=1)
    resDf = resDf.groupby([SEASON_NUMBER]).sum()
    resDf[AVG_RATING] = resDf[AVG_RATING] / resDf[VOTE_COUNT]
    return resDf.drop([EPISODE_NUMBER], axis=1)


def get_df_from_filename_and_folder(folder, file_name):
    """
    Get data frame from file name and folder
    :param folder:          Folder path of our csv files
    :param file_name:       File name
    :return:                Data frame
    """
    file_name = get_file_path(folder, file_name)
    season_df = pd.read_csv(file_name)
    return season_df


def most_lines_in_the_most_popular_episode(csv_folder):
    """
    Get lines count of each character in the second most popular episode
    :param csv_folder:          Folder of our csv files
    :return:                    Data frame
    """
    rating_df = get_only_friends_rating(csv_folder)
    second_poplar_value = rating_df[VOTE_COUNT].nlargest(2).iloc[1]
    second_poplar_episode = rating_df[rating_df[VOTE_COUNT] == second_poplar_value]

    season, episode = get_episode_and_season_from_id(second_poplar_episode[EPISODE_ID].iloc[0],
                                                     csv_folder)

    quotes_df = get_df_from_filename_and_folder(csv_folder, QUOTES_CSV)
    quotes_df = quotes_df.rename({AUTHOR_COL: RESULT_CHARACTER}, axis=1)
    quotes_df = quotes_df[quotes_df[SEASON_COLUMNS_QUOTES] == season]
    quotes_df = quotes_df[quotes_df[EPISODE_NUMBER_COLUMNS_QUOTES] == episode]
    result_df = quotes_df.groupby(RESULT_CHARACTER).size().to_frame(NUMBER_OF_LINES)
    result_df[RESULT_SEASON_NUMBER] = [season] * result_df.shape[0]
    result_df[RESULT_EPISODE] = [episode] * result_df.shape[0]
    return result_df


def who_said_it(csv_folder, character_name, phrase):
    """
    Get count of the phrase mentioned by the character
    :param csv_folder:          Folder of our csv files
    :param character_name:      Character name
    :param phrase:              Phrase
    :return:                    Count
    """
    quotes = get_df_from_filename_and_folder(csv_folder, QUOTES_CSV)
    quotes[QUOTES_COLUMN] = quotes[QUOTES_COLUMN].str.lower()
    quotes = quotes[quotes[QUOTES_COLUMN].str.contains(str.lower(phrase))]
    quotes_only_character = quotes[quotes[AUTHOR_COL] == character_name]
    quotes_all = quotes[quotes[AUTHOR_COL] == ALL_VALUE]
    quotes = pd.concat([quotes_only_character, quotes_all])
    return quotes.shape[0]
