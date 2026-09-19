"""
Name: Abrar AL Rafid
File: studentapp.py
Launches the student program.
"""

from student    import Student
from studentgui import StudentGUI1, StudentGUI2, StudentGUI3
        
def main():
    """Instantiates the model and the view,
    and opens the window."""
    model = Student("Ken", 10)
    model.setScore(0, 100)
    model.setScore(1, 100)
    model.setScore(2, 77)
    view = StudentGUI3(model)
    view.mainloop()
    
# Entry point of the application.
if __name__ == "__main__":
    main()
