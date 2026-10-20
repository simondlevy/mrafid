"""
Author: Ken Lambert
File: mazesquare.py
"""

from breezypythongui import EasyCanvas

class MazeSquare(EasyCanvas):
    """Represents a square in a maze."""

    def __init__(self, parent, width, height, letter):
        """Sets up the canvas."""
        EasyCanvas.__init__(self, parent, width = width,
                            height = height)
        self.x = width / 2
        self.y = height / 2
        if letter == "*":
            self["background"] = "black"
        self.letterID = None
        if letter in ("P", "T"):
            self.setLetter(letter)

    def setLetter(self, letter):
        """Draws the queen on the square."""
        if self.letterID:
            self.delete(self.letterID) 
        self.letterID = self.drawText(letter, self.x, self.y)

