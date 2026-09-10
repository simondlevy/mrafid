"""
Author: Abrar Al Rafid
File: numberguess.py
"""

class NumberGuess(object):

    def __init__(self, low, high):
        """Guesses the starting number"""
        self.value = (low + high) // 2
        self.LOW = low
        self.HIGH = high
        self.low = low
        self.high = high

    def tooLow(self):
        self.low = self.value
        self.value = (self.value + self.high) // 2

    def tooHigh(self):
        self.high = self.value
        self.value = (self.low + self.value) // 2

    def getValue(self):
        return self.value

    def __str__(self):
        return str(self.value)