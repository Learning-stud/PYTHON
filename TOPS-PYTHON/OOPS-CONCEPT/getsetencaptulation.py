class Student:
    def __init__(self):
        self.name = "jay"
        self.contact = "7573826063"

    def setName(self, name):
        self.name = name

    def getName(self):
        return self.name

    def setContact(self, contact):
        self.contact = contact

    def getContact(self):
        return self.contact

# Create an instance of the Student class
s = Student()

# Set the contact using the setContact method
s.setContact("54654828")

# Print the current values using the get methods
print("Name:", s.getName())
print("Contact:", s.getContact())
