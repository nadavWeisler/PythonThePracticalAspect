import ex3a

if __name__ == '__main__':
    mazePath = "exampleFiles/test2.csv"
    mazeObject = ex3a.Maze(mazePath)
    print(mazeObject.data)
    mazeObject.maze_solver()
