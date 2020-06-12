import numpy as np
import pandas as pd

SPECIAL_WORD = "huji"


def filter_numeric_column(df, col_name, num1, num2):
    """
    Filter dataframe by the value of col_name (between num1, num2)
    :param df:                  Dataframe
    :param col_name:            Column name
    :param num1:                Number
    :param num2:                Number
    :return:                    Filtered dataframe
    """
    mid = df[df[col_name] < num2]
    return mid[mid[col_name] >= num1]


def switch_col_names(df, col_name1, col_name2):
    """
    Switch column names
    :param df:                  Dataframe
    :param col_name1:           Column name
    :param col_name2:           Column name
    """
    df.rename({col_name1: col_name2, col_name2: col_name1},
              axis=1,
              inplace=True)


def double_special_letters(df, col_name_letter, col_name_value, col_name_results):
    """
    Create new column of the col_name_value, doubled if letter in SPECIAL_WORD
    :param df:                  Dataframe
    :param col_name_letter:     Letter column name
    :param col_name_value:      Value column name
    :param col_name_results:    Results column name
    """

    def getValue(word, letter, value):
        res = value
        if letter in word:
            res *= 2
        return res

    values = []
    for index, row in df.iterrows():
        values.append(getValue(SPECIAL_WORD, row[col_name_letter], row[col_name_value]))

    df[col_name_results] = values


def put_row_items_together(df, col_name_results):
    """
    Create another column which contain a list of all the row items
    :param df:                  Dataframe
    :param col_name_results:    Result column name
    """
    df[col_name_results] = pd.Series(df.values.tolist())
