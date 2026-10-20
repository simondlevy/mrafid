"""
File: grid.py
"""

from arrays import Array

class Grid(object):
    """Represents a two-dimensional array."""

    def __init__(self, rows, columns, fillValue = None):
        self._data = Array(rows)
        for row in range(rows):
            self._data[row] = Array(columns, fillValue)

    def getHeight(self):
        """Returns the number of rows."""
        return len(self._data)

    def getWidth(self):
        "Returns the number of columns."""
        return len(self._data[0])

    def __getitem__(self, index):
        """Supports two-dimensional indexing with [][]."""
        return self._data[index]

    def __str__(self):
        """Returns a string representation of the grid."""
        result = ""
        for row in range(self.getHeight()):
            for col in range(self.getWidth()):
                result += str(self._data[row][col]) + " "
            result += "\n"
        return result

    def __iter__(self):
        """Yields the grid's items in row major order."""
        row = 0
        while row < self.getHeight():
            column = 0
            while column < self.getWidth():
                yield self[row][column]
                column += 1
            row += 1

def main(rows = 10, columns = 10, fillValue = 1):
    g = Grid(rows, columns, fillValue)
    print("The grid:\n", g)
    for row in range(g.getHeight()):
        for column in range(g.getWidth()):
            g[row][column] = (row, column)
    print("The grid positions:\n", g)
    print("The items in row major order:")
    for item in g:
        print(item)

if __name__ == "__main__": main()
    
            
