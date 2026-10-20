from mazemodel import MazeModel

for filename in ("maze1.txt", "maze2.txt"):
    maze = MazeModel(filename)

    while maze.canMove():
        maze.move()

    print(filename, "was solved:", maze.isSolved())