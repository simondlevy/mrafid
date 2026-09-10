""" 
File: counterapp.py
Launches the counter program.
"""

from counter    import Counter
from countergui import CounterGUI
        
def main():
    """Instantiates the model and the view,
    and opens the window."""
    model = Counter()
    view = CounterGUI(model)
    view.mainloop()           

# Entry point of the application.
if __name__ == "__main__":
    main()
