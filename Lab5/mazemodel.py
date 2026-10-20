"""
File: mazemodel.py

Determine the solution to a maze problem.
Uses a gid to represent the maze.  This grid is input from
a text file.  Uses a backtracking algorithm.
Prints the maze at the start and at the end of the process,
as well as the number of choice points visited and the number
of choice points remaining on the stack.
"""

from counter import Counter
from grid import Grid
from mazesquare import MazeSquare
from stack import Stack

class MazeModel(object):
    """Represents a maze."""

    def __init__(self, fileName):
        self.visitedCounter = Counter()
        self.remainingCounter = Counter()
        self.maze = self.getMazeFromFile(fileName)
        self.startRow, self.startColumn = self.findStartPos()
        self.pebbles = "ABCDEFGHIJKLMNOQRSUVWXYZabcdefghijklmnoqrsuvwxyz123456789"
        self.pebblesAndWall = self.pebbles + "*"
        self.pebblePos = 0
        self.stack = Stack()
        self.stack.push((self.startRow, self.startColumn))
        self.solved = False

    def __str__(self):
        """Returns the string rep of the maze."""
        return str(self.maze)
    
    def getMazeFromFile(self, fileName):
        """Reads the maze from a text file and returns a grid that
        represents it."""
        fileObj = open(fileName, 'r')
        firstLine = list(map(int, fileObj.readline().strip().split()))
        rows = firstLine[0]
        columns = firstLine[1]
        maze = Grid(rows, columns, "*")
        for row in range(rows):
            line = fileObj.readline().strip()
            column = 0
            for ch in line:
                maze[row][column] = ch
                column += 1
        return maze

    def findStartPos(self):
        """Returns the position of the start symbol in the grid."""
        for row in range(self.maze.getHeight()):
            for column in range(self.maze.getWidth()):
                if self.maze[row][column] == 'P':
                    return (row, column)
        return (-1, -1)

    def getWidth(self):
        """Returns the width of the maze in columns."""
        return self.maze.getWidth()
                
    def getHeight(self):
        """Returns the height of the maze in columns."""
        return self.maze.getHeight()

    def getLetter(self, row, column):
        """Returns the letter in the maze at index."""
        return self.maze[row][column]

    def canMove(self):
        """Returns True of the maze is not solved and there
        are more choice points left."""
        return not self.solved and not self.stack.isEmpty()

    def isSolved(self):
        """Returns True if the maze is solved or False otherwise."""
        return self.solved

    def move(self):
        """Precondition: canMove returns True.
        Makes a move in the maze and returns the current choice point."""
        (row, column) = self.stack.pop()
        self.visitedCounter.increment()
        if  self.maze[row][column] == 'T':
            self.remainingCounter.increment(len(self.stack))
            self.solved = True
        elif not self.maze[row][column] in self.pebbles:
            # Cell has not been visited, so mark it and add adjacent unvisited
            # positions to the memory
            if self.pebblePos == len(self.pebbles):
                self.pebblePos = 0
            self.maze[row][column] = self.pebbles[self.pebblePos]
            self.pebblePos += 1
            # Try NORTH
            if row != 0 and not self.maze[row - 1][column] in self.pebblesAndWall:
                adjacentPoint = (row - 1, column)
                if not adjacentPoint in self.stack:
                    self.stack.push(adjacentPoint)             
            # Try SOUTH
            if row + 1 != self.maze.getHeight() and not self.maze[row + 1][column] in self.pebblesAndWall:         
                adjacentPoint = (row + 1, column)
                if not adjacentPoint in self.stack:
                    self.stack.push(adjacentPoint)             
            # Try EAST
            if column + 1 != self.maze.getWidth() and not self.maze[row][column + 1] in self.pebblesAndWall:         
                adjacentPoint = (row, column + 1)
                if not adjacentPoint in self.stack:
                    self.stack.push(adjacentPoint)             
            # Try WEST
            if column != 0 and not self.maze[row][column - 1] in self.pebblesAndWall:         
                adjacentPoint = (row, column - 1)
                if not adjacentPoint in self.stack:
                    self.stack.push(adjacentPoint)             
        return (row, column)

def main(fileName = "maze1.txt"):
    maze = MazeModel(fileName)
    print(maze)
    while maze.canMove():
        position = maze.move()
        print(maze)
        print(position)
    print("\nSEARCH CONCLUDED\n")
    print("\nThere were " + str(maze.visitedCounter) + \
          " choice points visited.\n")
    print("\nThere were " + str(maze.remainingCounter) + \
          " choice points left in memory.\n")

if __name__ == '__main__': 
    main()


