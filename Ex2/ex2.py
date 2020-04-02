class Matrix(object):
    """

    """

    def __init__(self, n_rows, n_cols, items):
        """
        """
        # you need to check the parameters here
        self.n_rows = n_rows
        self.n_cols = n_cols
        self.items = items  # list of numbers
        self.mat = [items[i:i + n_cols] for i in range(0, len(items), n_cols)]

    def switch_rows(self, row_index1, row_index2):
        """  """

    pass

    def multiple_row(self, row_index, number):
        """  """

    pass

    def add_row_to_row(self, row_index1, row_index2, scalar):
        """  """

    pass

    def gauss_ranking(self):
        """  """

    pass


class SquaredMatrix(Matrix):
    def __init__(self, n, items):
        """ init """
        # super

    def __pow__(self, n):
        """  """
