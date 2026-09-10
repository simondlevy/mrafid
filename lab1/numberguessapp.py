"""
Author: Abrar Al Rafid
File: numberguessapp.py

Launches the number guess program, where the computer
guesses a user's number.

Run at the command line with optional lower and upper bounds.
Defaults are 1..100.

Examples:

python3 numberguessapp.py
python3 numberguessapp.py 1 1000
python3 numberguessapp.py 50 100
"""

from numberguess    import NumberGuess
from numberguessgui import NumberGuessGUI
import sys
        
def main():
    """Instantiates the model and the view,
    and opens the window."""
    if len(sys.argv) == 1:
        low = 1
        high = 100
    else:
        low = int(sys.argv[1])
        high = int(sys.argv[2])
    model = NumberGuess(low, high)
    view = NumberGuessGUI(model)
    view.mainloop()           

# Entry point of the application.
if __name__ == "__main__":
    main()
