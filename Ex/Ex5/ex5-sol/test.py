import pandas as pd
from ex5a import double_special_letters, filter_numeric_column,\
    put_row_items_together, switch_col_names

if __name__ == '__main__':
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
