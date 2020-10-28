class Person:
    def __init__(self, fname, lname):
        self.firstName = fname
        self.lastName = lname
        print("First Name: {}, Last Name: {}".format(self.firstName, self.lastName))

class Student:
    def __init__(self, year):
        self.graduationYear = year
        print("Graduation Year: {}".format(self.graduationYear))

class Major(Person, Student):
    def __init__(self, fname, lname, year, majors):
        self.major = majors
        Person.__init__(self, fname, lname)
        Student.__init__(self, year)
        print("First Name: {}, Last Name: {}, Graduation Year: {}, Major: {}".format(self.firstName, self.lastName, self.graduationYear, self.major))


mj = Major("Triwibowo Ridho", "Permana", "2016", "Teknik Informatika")