# 316493758
# 5

ERROR_MSG_INVALID_ITEMS_LIST = "Invalid items list"
ERROR_MSG_ITEM_COUNT_DOES_NOT_FIT = "Items count does not fit"
ERROR_MSG_INVALID_ROW_COUNT = "Invalid rows count"
ERROR_MSG_INVALID_COL_COUNT = "Invalid columns count"
ERROR_MSG_INVALID_ROW_INDEX = "Invalid row index"
ERROR_MSG_INVALID_POW_INPUT = "Invalid pow input"
ERROR_MSG_INVALID_SCALAR = "Invalid scalar"


class Matrix(object):
    """
    Matrix class
    """

    def __init__(self, n_rows, n_cols, items):
        """
        Matrix constructor
        :param n_rows: Rows count (int)
        :param n_cols: Columns count (int)
        :param items:  Cell items (Numbers list)
        """
        Matrix._init_validations(n_rows, n_cols, items)
        self.n_rows = n_rows
        self.n_cols = n_cols
        self.items = items
        self.mat = [items[i:i + n_cols] for i in range(0, len(items), n_cols)]

    def switch_rows(self, row_index1, row_index2):
        """
        Switch rows in row_index1 and row_index2
        :param row_index1:  First row index (int)
        :param row_index2:  Second row index (int)
        """
        self._validate_row_index(row_index1)
        self._validate_row_index(row_index2)
        self.mat[row_index1], self.mat[row_index2] = self.mat[row_index2], self.mat[row_index1]

    def multiple_row(self, row_index, number):
        """
        Multiply row on row_index by number
        :param row_index:   Row index
        :param number:      Number (int or float)
        """
        self._validate_row_index(row_index)
        Matrix._validate_scalar(number)
        self.mat[row_index] = self._get_multiple_row(row_index, number)

    def add_row_to_row(self, row_index1, row_index2, scalar):
        self._validate_row_index(row_index1)
        self._validate_row_index(row_index2)
        Matrix._validate_scalar(scalar)
        """
        Add one row to the other multiply by scalars
        :param row_index1:  First row index (int)
        :param row_index2:  Second row index (int)
        :param scalar:      Scalar (int or float)
        """
        self.mat[row_index1] = Matrix._get_two_rows_adding(self.mat[row_index1],
                                                           self._get_multiple_row(row_index2, scalar))

    def gauss_ranking(self):
        """
        Do gauss ranking
        """
        self._order_mat_by_rank()
        self._do_gaussian_elimination()
        self._order_mat_by_rank()
        self._cosmetic_changes()

    def _validate_row_index(self, row_index):
        """
        Validate row index
        :param row_index: row index
        :return:
        """
        if not isinstance(row_index, int):
            raise TypeError(ERROR_MSG_INVALID_ROW_INDEX)
        elif not (0 <= row_index < len(self.mat)):
            raise ValueError(ERROR_MSG_INVALID_ROW_INDEX)

    def _get_first_index(self, row_index):
        """
        Get first number (that is not zero) from row
        on row_index
        :param row_index: Row index (int)
        :return: first row index, -1 otherwise
        """
        for i in range(len(self.mat[row_index])):
            if self.mat[row_index][i] != 0:
                return i
        return -1

    def _cosmetic_changes(self):
        """
        Do Cosmetic changes to matrix
        """
        for row_index in range(len(self.mat)):
            for cell_index in range(len(self.mat[row_index])):
                if self.mat[row_index][cell_index] % 1 == 0:
                    self.mat[row_index][cell_index] = int(self.mat[row_index][cell_index])

    def _order_mat_by_rank(self):
        """
        Order matrix by their first number location
        """
        for row in range(1, len(self.mat)):
            if self._better_rank(row - 1, row):
                self.switch_rows(row - 1, row)
                for i in range(row - 1, 0, -1):
                    if self._better_rank(i - 1, i):
                        self.switch_rows(i - 1, i)
                    else:
                        break

    def _do_gaussian_elimination(self):
        for row_index in range(len(self.mat)):
            row_first = self._get_first_index(row_index)
            if row_first == -1:
                continue
            if self.mat[row_index][row_first] != 1:
                self.multiple_row(row_index, (1 / self.mat[row_index][row_first]))
            for i in range(row_index + 1, len(self.mat)):
                if self.mat[i][row_first] != 0:
                    self.add_row_to_row(i, row_index, (self.mat[i][row_index] * -1))

    def _better_rank(self, row_index1, row_index2):
        """
        Return True if the row on row_index1 should be higher
        then the row on row_index2, False otherwise
        :param row_index1: First row index (int)
        :param row_index2: Second row index (ind)
        :return: Boolean
        """
        for i in range(len(self.mat[row_index1])):
            if self.mat[row_index1][i] == 0 and self.mat[row_index2][i] != 0:
                return True
            elif self.mat[row_index1][i] != 0 and self.mat[row_index2][i] == 0:
                return False
        return False

    def _get_multiple_row(self, row_index, number):
        """
        Get row on index row_index multiply by number
        :param row_index: Row index (int)
        :param number:    Scalar (number)
        :return:          Row multiply number (list)
        """

        return list(map(Matrix._multiply_num_in_scalar,
                        self.mat[row_index],
                        [number] * len(self.mat[row_index])))

    @staticmethod
    def _row_validations(row_count):
        """
        Rows number tests, raise an error if there is any
        :param row_count: Row number (int)
        """
        if not isinstance(row_count, int):
            raise TypeError(ERROR_MSG_INVALID_ROW_COUNT)
        elif row_count < 1:
            raise ValueError(ERROR_MSG_INVALID_ROW_COUNT)

    @staticmethod
    def _col_validations(col_count):
        """
        Columns number tests, raise an error if there is any
        :param col_count: Columns number (int)
        """
        if not isinstance(col_count, int):
            raise TypeError(ERROR_MSG_INVALID_COL_COUNT)
        elif col_count < 1:
            raise ValueError(ERROR_MSG_INVALID_COL_COUNT)

    @staticmethod
    def _validate_scalar(n):
        """
        Validate scalar input
        :param n: object
        """
        if not Matrix._is_digit(n):
            raise TypeError(ERROR_MSG_INVALID_SCALAR)

    @staticmethod
    def _is_digit(obj):
        """
        Test if object is int or float
        :param obj: object
        :return:    True if object is int or float, False otherwise
        """
        return isinstance(obj, int) or isinstance(obj, float)

    @staticmethod
    def _all_is_digits(lst):
        """
        Check if list contains only numbers
        :param lst: list (list)
        :return:    True if contains only numbers, False otherwise
        """
        return False not in list(map(Matrix._is_digit, lst))

    @staticmethod
    def _init_validations(row_count, col_count, lst):
        """
        First tests on constructor, raise an error if there any
        :param row_count: Rows count (int)
        :param col_count: Columns count (int)
        :param lst:       Items list (list)
        """
        Matrix._row_validations(row_count)
        Matrix._col_validations(col_count)

        if len(lst) != (row_count * col_count):
            raise ValueError(ERROR_MSG_ITEM_COUNT_DOES_NOT_FIT)
        else:
            if not isinstance(lst, list):
                raise TypeError(ERROR_MSG_INVALID_ITEMS_LIST)
            if not Matrix._all_is_digits(lst):
                raise TypeError(ERROR_MSG_INVALID_ITEMS_LIST)

    @staticmethod
    def _multiply_num_in_scalar(num, scalar):
        """
        Multiply numbers
        :param num:     First number (int or float)
        :param scalar:  Second number(int or float)
        :return:        num * scalar
        """
        return num * scalar

    @staticmethod
    def _add_numbers(num1, num2):
        """
        Combine two numbers
        :param num1:    First number (int or float)
        :param num2:    Second number (int or float)
        :return:        Numbers adding (int or float)
        """
        return num1 + num2

    @staticmethod
    def _get_two_rows_adding(row1, row2):
        """
        Get tow rows combines
        :param row1: First row (list)
        :param row2: Second row (list)
        :return: Combined row (list)
        """

        return list(map(Matrix._add_numbers, row1, row2))


class SquaredMatrix(Matrix):
    """
    SquaredMatrix class, it is uniq because its rows
    and columns are with the same length
    """

    def __init__(self, n, items):
        """
        SquaredMatrix constructor
        :param n: Cols and rows count
        :param items: item count
        """
        Matrix.__init__(self, n, n, items)

    def __pow__(self, n):
        """
        Multiply self.mat with itself n times
        :param n:
        :return:
        """

        def validate_pow(n):
            """
            Validate pow argument
            :param n: pow argument
            """
            if not SquaredMatrix._is_digit(n):
                raise TypeError(ERROR_MSG_INVALID_POW_INPUT)
            elif not (n > 0 and n % 1 == 0):
                raise ValueError(ERROR_MSG_INVALID_POW_INPUT)

        validate_pow(n)
        original_matrix = self.mat
        for count in range(n):
            self.mat = self._multiply_with_another(original_matrix)

    def _multiply_with_another(self, second_matrix):
        """
        Multiply matrix with another given matrix
        :param second_matrix: List of lists
        :return:
        """
        transpose_mat = self.get_transpose_matrix(second_matrix)
        newMat = []
        for row in self.mat:
            newRow = []
            for i in range(len(row)):
                newCell = 0
                for j in range(len(row)):
                    newCell += row[j] * transpose_mat[i][j]
                newRow.append(newCell)
            newMat.append(newRow)
        return newMat

    @staticmethod
    def get_transpose_matrix(original_matrix):
        """
        Get transpose matrix for original_matrix
        :param original_matrix:  list of lists
        :return: transpose matrix (list of lists)
        """
        newMat = []
        for i in range(len(original_matrix)):
            newRow = []
            for j in range(len(original_matrix[0])):
                newRow.append(original_matrix[j][i])
            newMat.append(newRow)
        return newMat
