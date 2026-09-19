"""
Name: Abrar AL Rafid
File: student.py
Resources to manage a student's name and test scores.
"""

class Student(object):
    """Represents a student."""

    def __init__(self, name = "", numberOfScores = 3):
        """All scores are initially 0."""
        self.name = name
        self.scores = []
        for count in range(numberOfScores):
            self.scores.append(0)

    def __str__(self):
        """Returns the string representation of the student."""
        return "Name: " + self.name  + "\n" + \
               "\n".join(map(lambda number, score:
                             "Score " + str(number) + ": " + str(score),
                             range(1, len(self.scores) + 1),
                             self.scores)) + \
               "\nHigh score: " + str(self.getHighScore()) + \
               "\nAverage: " + str(self.getAverage())

    def getNumberOfScores(self):
        """Returns the number of scores."""
        return len(self.scores)

    def getName(self):
        """Returns the student's name."""
        return self.name

    def setName(self, newName):
        """Changes the student's name to newName."""
        self.name = newName
  
    def setScore(self, i, score):
        """Resets the ith score, counting from 0."""
        self.scores[i] = score

    def getScore(self, i):
        """Returns the ith score, counting from 0."""
        return self.scores[i]
   
    def getAverage(self):
        """Returns the average score."""
        return sum(self.scores) / len(self.scores)
    
    def getHighScore(self):
        """Returns the highest score."""
        return max(self.scores)

from random import randint

def main(numScores = 3):
    """Tests sorting."""
    # Create the list and put 5 students into it
    students = list()
    names = ("Juan", "Bill", "Stacy", "Maria", "Charley")
    for name in names:
        s = Student(name, numScores)
        for index in range(numScores):
            s.setScore(index, randint(70, 100))
        students.append(s)
    # Print the contents
    print("The list of students:")
    for s in students:
        print(s)
        
if __name__ == "__main__":
    main()
    

