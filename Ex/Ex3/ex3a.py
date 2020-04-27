class Maze(object):
    TARGET_CONSTANT = "T"
    START_CONSTANT = "S"
    WALL_CONSTANT = "X"
    EMPTY_STRING = ""

    @staticmethod
    def clean_list(lst):
        new_line = []
        for item in lst:
            new_line.append(item.replace("\n", ''))
        return new_line

    @staticmethod
    def get_lines_from_files(file_name):
        result = []
        try:
            with open(file_name, "r") as f:
                for line in f.readlines():
                    result.append(Maze.clean_list(line.split(',')))
        except IOError:
            print("File not accessible")
        finally:
            return result

    @staticmethod
    def validate_maze(matrix):
        target_col = -1
        target_row = -1
        start_col = -1
        start_row = -1
        for i in range(len(matrix)):
            if Maze.START_CONSTANT in matrix[i]:
                if start_col != -1 or matrix[i].count(Maze.START_CONSTANT) > 1:
                    return False
                else:
                    start_col = matrix[i].index(Maze.START_CONSTANT)
                    start_row = i
            elif Maze.TARGET_CONSTANT in matrix[i]:
                if target_col != -1 or matrix[i].count(Maze.TARGET_CONSTANT) > 1:
                    return False
                else:
                    target_col = matrix[i].index(Maze.TARGET_CONSTANT)
                    target_row = i

        if not (target_col > -1 and target_col > -1):
            return False

        return (start_row, start_col), (target_row, target_col)

    def __init__(self, csv_file_path):
        self.data = Maze.get_lines_from_files(csv_file_path)
        validation_result = Maze.validate_maze(self.data)
        if validation_result:
            self.start, self.target = Maze.validate_maze(self.data)

    def maze_solver(self):
        return self.solve_maze(self.start[0], self.start[1], [])

    def solve_maze(self, row, col, been_there):
        if row < 0 or row >= len(self.data) or \
                col < 0 or col >= len(self.data[0]):
            return False
        elif self.data[row][col] == Maze.WALL_CONSTANT:
            return False
        elif self.data[row][col] == Maze.TARGET_CONSTANT:
            return True
        else:
            been_there.append((row, col))
            retVal = False
            if not (row + 1, col) in been_there:
                retVal = retVal or self.solve_maze(row + 1, col, been_there)
            if not (row - 1, col) in been_there:
                retVal = retVal or self.solve_maze(row - 1, col, been_there)
            if not (row, col + 1) in been_there:
                retVal = retVal or self.solve_maze(row, col + 1, been_there)
            if not (row, col - 1) in been_there:
                retVal = retVal or self.solve_maze(row, col - 1, been_there)

            return retVal
