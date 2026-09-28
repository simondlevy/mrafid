"""
Name: Abrar AL Rafid
File: studentgui.py
Provides three different GUI-based views of a Student object.

StudentGUI1 shows a student's info in a simple text area.

StudentGUI2 shows a student's info in editable text fields.

StudentGUI3 shows a student's info in a text area, and pops
up a dialog to allow its modification.
"""

from breezypythongui import EasyFrame, EasyDialog

class StudentGUI1(EasyFrame):
    """Displays the student's info in a text area."""

    def __init__(self, student):
        """Sets up the window, label, and buttons."""
        EasyFrame.__init__(self, title = "Student")

        # Instance variable to track the student.
        self.student = student

        # A text area to display the student's info
        self.addTextArea(text = str(self.student),
                         row = 0, column = 0, width = 25)


class StudentGUI2(EasyFrame):
    """Displays the student's info in editable fields."""

    def __init__(self, student):
        """Sets up the window, label, and buttons."""
        EasyFrame.__init__(self, title = "Student")

        # Instance variable to track the student.
        self.student = student

        numScores = student.getNumberOfScores()

        # Label and name for the student's name
        self.addLabel(text = "Name", row = 0, column = 0)
        self.nameField = self.addTextField(text = self.student.getName(),
                                           row = 0, column = 1)

        # Labels and fields for the student's scores
        self.scoreFieldList = list()
        for index in range(numScores):
            self.addLabel(text = "Score " + str(index + 1),
                          row = index + 1, column = 0)
            field = self.addIntegerField(value = student.getScore(index),
                                         row = index + 1, column = 1)
            self.scoreFieldList.append(field)

        self.addLabel(text = "Average score", row = numScores + 2, column = 0)
        self.aveField = self.addFloatField(value = self.student.getAverage(),
                                           row = numScores + 2, column = 1,
                                           state = "readonly", precision = 2)
        self.addLabel(text = "HighScore", row = numScores + 3, column = 0)
        self.highField = self.addIntegerField(value = self.student.getHighScore(),
                                           row = numScores + 3, column = 1,
                                              state = "readonly")
            

class StudentGUI3(EasyFrame):
    """Displays the student's info in a text area.
    Pops up a dialog to modify the student's info,
    and refreshes the text area when done."""

    def __init__(self, student):
        """Sets up the window, label, and buttons."""
        EasyFrame.__init__(self, title = "Student")

        # Instance variable to track the student.
        self.student = student

        # A text area to display the student's info
        self.textArea = self.addTextArea(text = str(self.student),
                                         row = 0, column = 0, width = 25)

         # Button to modify the Student object
        self.addButton(text = "Modify", row = 1, column = 0,
                       command = self.modify)

    def modify(self):
        """Pops up a dialog to modify the student's info.
        Updates the text area if the user clicks OK."""
        dialog = StudentDialog(self, self.student)
        if dialog.modified():
            self.textArea.setText(str(self.student))

class StudentDialog(EasyDialog):
    """Opens a dialog on a student object."""

    def __init__(self, parent, student):
        """Sets up the window."""
        self.student = student
        EasyDialog.__init__(self, parent, "Student Editor")
    
    def body(self, master):
        """Sets up the widgets."""
        self.addLabel(master, text = "Name", row = 0, column = 0)
        self.nameField = self.addTextField(master,
                                           text = self.student.getName(),
                                           row = 0, column = 1)
        # Labels and fields for the student's scores
        self.scoreFieldList = list()
        for index in range(self.student.getNumberOfScores()):
            self.addLabel(master, text = "Score " + str(index + 1),
                          row = index + 1, column = 0)
            field = self.addIntegerField(master,
                                         value = self.student.getScore(index),
                                         row = index + 1, column = 1)
            self.scoreFieldList.append(field)

    # Event handling method
    def apply(self):
        """When the OK button is clicked, transfers data from the
        fields to the song."""
        if self.nameField.getText() == "":
            self.messageBox("ERROR", "Name is missing")
            return
        self.student.setName(self.nameField.getText())
        for index in range(self.student.getNumberOfScores()):
            self.student.setScore(index, self.scoreFieldList[index].getNumber())
        self.setModified()
           
        
        

