"""
Name: Abrar AL Rafid
File: rosterapp.py
Launches the roster program.
"""

from roster    import createRoster
from rostergui import RosterGUI
        
def main():
    """Instantiates the model and the view,
    and opens the window."""
    model = createRoster(3)
    view = RosterGUI(model)
    view.mainloop()
    
# Entry point of the application.
if __name__ == "__main__":
    main()
