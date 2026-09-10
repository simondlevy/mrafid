"""
Name: Abrar Al Rafid
File: numberguessgui.py
"""

from breezypythongui import EasyFrame
import os
from breezypythongui import EasyDialog

class NumberGuessGUI(EasyFrame):
    """View for a counter."""

    def __init__(self, guess):
        """Sets up the window, label, and buttons."""
        EasyFrame.__init__(self, title = f"Guessing")

        # Instance variable to track the guess.
        self.guess = guess

        # Initialize number of guesses
        self.count = 1

        # A label to display the guess in the first row.
        self.label = self.addLabel(text = f"My guess is {str(self.guess)} for {self.count} guess(es)",
                                   row = 0, column = 0,
                                   sticky = "NSEW",
                                   columnspan = 3)

        # Three command buttons.
        self.addButton(text = "Too low",
                       row = 1, column = 0,
                       command = self.tooLow)

        self.addButton(text = "Too high",
                       row = 1, column = 1,
                       command = self.tooHigh)

        self.addButton(text = "Correct",
                       row = 1, column = 2,
                       command = self.correct)

    # Methods to handle user events.
    def tooLow(self):
        self.guess.tooLow()
        self.count += 1
        self.label["text"] = f"My guess is {str(self.guess)} for {self.count} guess(es)"

    def tooHigh(self):
        self.guess.tooHigh()
        self.count += 1
        self.label["text"] = f"My guess is {str(self.guess)} for {self.count} guess(es)"

    def correct(self):
        """Displays game over screen."""
        self.messageBox(title="Game Over", message=f"My guess is {str(self.guess)} for {self.count} guess(es)")
        self.destroy()
        os._exit(0)