"""
File: countergui.py
"""

from breezypythongui import EasyFrame

class CounterGUI(EasyFrame):
    """View for a counter."""

    def __init__(self, counter):
        """Sets up the window, label, and buttons."""
        EasyFrame.__init__(self, title = "Counter")

        # Instance variable to track the count.
        self.counter = counter

        # A label to displat the count in the first row.
        self.label = self.addLabel(text = str(self.counter),
                                   row = 0, column = 0,
                                   sticky = "NSEW",
                                   columnspan = 3)

        # Three command buttons.
        self.addButton(text = "Decrement",
                       row = 1, column = 0,
                       command = self.decrement)

        self.addButton(text = "Reset",
                       row = 1, column = 1,
                       command = self.reset)

        self.addButton(text = "Increment",
                       row = 1, column = 2,
                       command = self.increment)


    # Methods to handle user events.
    def increment(self):
        """Increments the counter and updates the display."""
        self.counter.increment()
        self.label["text"] = str(self.counter)

    def decrement(self):
        """Decrements the counter and updates the display."""
        self.counter.decrement()
        self.label["text"] = str(self.counter)

    def reset(self):
        """Resets the counter and updates the display."""
        self.counter.reset()
        self.label["text"] = str(self.counter)
