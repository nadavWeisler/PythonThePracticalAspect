import pandas as pd
from ex5a import double_special_letters, filter_numeric_column, \
    put_row_items_together, switch_col_names

from ex5b import create_season_rating, who_said_it, most_lines_in_the_most_popular_episode


def testA():
    df = pd.DataFrame(data={'col1': [1, 2, 3, 4, 5], 'col2': [3, 4, 5, 6, 7]})
    print(df)

    df_filtered = filter_numeric_column(df, 'col1', 2, 4)
    print(df_filtered)

    df = pd.DataFrame(data={'col1': [1, 2, 3, 4, 5], 'col2': [3, 4, 5, 6, 7]})
    switch_col_names(df, 'col1', 'col2')
    print(df)

    df = pd.DataFrame(data={'letter': ['h', 'a', 'b', 'c', 'i'], 'value': [3, 4, 5, 6, 7]})
    double_special_letters(df, 'letter', 'value', 'col_res')
    print(df)

    df = pd.DataFrame(data={'col1': [1, 2, 3, 4, 5], 'col2': [3, 4, 5, 6, 7]})
    put_row_items_together(df, 'res1')
    print(df)


def testB():
    data_folder = "friends_datasets"

    df = create_season_rating(data_folder)
    df.to_csv("create_season_rating.csv")

    res = who_said_it(data_folder, "Monica", "my god")
    print("Break: " + str(res))

    res = who_said_it(data_folder, "Ross", "UNAGI")
    print("ROSS: " + str(res))

    res = who_said_it(data_folder, "Chandler", "Yemen")
    print("Yemen: " + str(res))

    df = most_lines_in_the_most_popular_episode(data_folder)
    df.to_csv("most_lines_in_the_most_popular_episode.csv")


if __name__ == '__main__':
    testB()
