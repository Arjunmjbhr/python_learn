class Student:
    totalStudent = 0
    def __init__(self, first, last, email, phone):
        self.first = first
        self.last = last
        self.email = email
        self.phone = phone
        Student.totalStudent += 1
    
    def printFullName(self):
        print("Fullname: ", self.first + " " + self.last)
    def changePhone(self, newPhone):
        self.phone = newPhone
        print("PhoneNo: " + self.phone)

student1 = Student("john","doe","johndoe@school.edu", "1234567890")
# student1.first = "john"
# student1.last = "doe"
# student1.email = "john.doe@school.edu"
# student1.phone = "0123456789"

student2=Student("steve", "fisherman", "stevefisherman@school.edu", "0987654321")
# student2.first = "steve"
# student2.last = "fisherman"
# student2.email = "steve.doe@school.edu"
# student2.phone = "0987654321"

# print(student1.first+ " " +student1.last )
# print(student2.first+ " " +student2.last )

student1.printFullName()
student1.changePhone("8848092884")

student2.printFullName()
student2.changePhone("9400179719")

print(Student.totalStudent)