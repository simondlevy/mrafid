"""
Author: Abrar Al Rafid
Project 1
File: imagedemo.py

"""

from breezypythongui import EasyFrame
from tkinter import PhotoImage
from tkinter.font import Font

class ImageDemo(EasyFrame):
    """Displays an image and a caption."""

    def __init__(self):
        """Sets up the window and widgets."""
        EasyFrame.__init__(self, title = "Image Demo")
        self.setResizable(True)
        imageLabel = self.addLabel(text = "",
                                   row = 0, column = 0,
                                   sticky = "NSEW")
        textLabel = self.addLabel(text = "Smokey the cat",
                                  row = 1, column = 0,
                                  sticky = "NSEW")
        
        # Load the image and associate it with the image label.
        self.image = PhotoImage(file = "smokey.gif")
        imageLabel["image"] = self.image

        # Set the font and color of the caption.
        font = Font(family = "Verdana", size = 24, slant = "italic", weight = "bold")
        textLabel["font"] = font
        textLabel["foreground"] = "red"

def main():
    """The starting point for launching the program."""
    ImageDemo().mainloop()

# Instantiates and pops up the window.
if __name__ == "__main__":
    main()
