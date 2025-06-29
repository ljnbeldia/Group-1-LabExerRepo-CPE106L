import random

"""
File: student.py
Resources to manage a student's name and test scores.

Programming Problem:
Add three methods to the Student class (in the file student.py) that compare two Student objects. 
One method should test for equality. A second method should test for less than. The third method should 
test for greater than or equal to. In each case, the method returns the result of the comparison of 
the two students’ names. Include a main function that tests all of the comparison operators. (LO: 10.2)

"""

class Student(object):

    """Represents a student."""

    def __init__(self, name, number):
        """All scores are initially 0."""
        self.name = name
        self.scores = []
        for count in range(number):
            self.scores.append(0)

    def getName(self):
        """Returns the student's name."""
        return self.name
  
    def setScore(self, i, score):
        """Resets the ith score, counting from 1."""
        self.scores[i - 1] = score

    def getScore(self, i):
        """Returns the ith score, counting from 1."""
        return self.scores[i - 1]
   
    def getAverage(self):
        """Returns the average score."""
        return sum(self.scores) / len(self._scores)
    
    def getHighScore(self):
        """Returns the highest score."""
        return max(self.scores)
 
    def __str__(self):
        """Returns the string representation of the student."""
        return "Name: " + self.name  + "\nScores: " + \
               " ".join(map(str, self.scores))
    
    def __eq__(self, other):
        """Checks if two students have the same name."""
        if isinstance(other, Student):
            return self.name == other.name
        return NotImplemented

    def __lt__(self, other):
        """Checks if this student's name is less than the other's name."""
        if isinstance(other, Student):
            return self.name < other.name
        return NotImplemented

    def __ge__(self, other):
        """Checks if this student's name is greater than or equal to the other's name."""
        if isinstance(other, Student):
            return self.name >= other.name
        return NotImplemented

def main():
    """A simple test."""
    # student = Student("Ken", 5)
    # student2 = Student("Alice", 5)
    # student3 = Student("Zara", 5)
    
    # print("Testing equality:")
    # print(f"Is {student.getName()} equal to {student2.getName()}? {student == student2}")
    # print(f"Is {student.getName()} equal to {student3.getName()}? {student == student3}")
    # print(f"Is {student2.getName()} equal to {student3.getName()}? {student2 == student3}")
    # print(f"Is {student2.getName()} equal to {student2.getName()}? {student2 == student2}")

    # print("\nTesting less than:")
    # print(f"Is {student.getName()} less than {student2.getName()}? {student < student2}")
    # print(f"Is {student2.getName()} less than {student3.getName()}? {student2 < student3}")
    # print(f"Is {student3.getName()} less than {student.getName()}? {student3 < student}")

    # print("\nTesting greater than or equal to:")
    # print(f"Is {student.getName()} greater than or equal to {student2.getName()}? {student >= student2}")
    # print(f"Is {student2.getName()} greater than or equal to {student3.getName()}? {student2 >= student3}")
    # print(f"Is {student3.getName()} greater than or equal to {student.getName()}? {student3 >= student}")

    '''
    Placing several students (which contains different names) in a list and sorting them by name.
    '''
    students = [
        Student("Ken", 5),
        Student("Alice", 5),
        Student("Zara", 5),
        Student("Bob", 5),
        Student("Mona", 5)
    ]
    print("\nOriginal list of students (shuffled):")
    random.shuffle(students)
    for s in students:
        print(s)
        print("-" * 20)

    students.sort()
    print("\nSorted list of students by name:")
    for s in students:
        print(s)
        print("-" * 20)


if __name__ == "__main__":
    main()


