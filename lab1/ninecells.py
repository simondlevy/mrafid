"""
Author: Abrar Al Rafid
Project 1
File: ninecells.py

"""

from breezypythongui import EasyFrame
from tkinter.font import Font

class LayoutDemo(EasyFrame):
    """Displays labels in the window's quadrants."""

    def __init__(self):
        """Sets up the window and the labels."""
        EasyFrame.__init__(self)
        for rw in range(0, 3):
            for cl in range(0, 3):
                label = self.addLabel(text = f"{str(rw)}, {str(cl)}", row = rw, column = cl, sticky = "NSEW")
                font = Font(family="Verdana", size=24, weight="bold")
                label["font"] = font
                label["foreground"] = "red"

def main():
    """The starting point for launching the program."""
    LayoutDemo().mainloop()

# Instantiates and pops up the window.
if __name__ == "__main__":
    main()