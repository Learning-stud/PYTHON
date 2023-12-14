# The code is defining a class called `vehicle` with a method called `types`. The `types` method prints the message "There are so many types of Vehicles..." when called.
class vehicals:
 def types(self):
  print('Theree are so many types of Vehicals...')


my_cars = vehicals()
my_cars.types()




class birds:
 def types_of_birds(self):
  print("there are so many types of birds.. ")

species = birds()
species.types_of_birds()


# class Students:
#     def attendance(self):
#         input("Enter the students attendance...")

# # Create an instance of the class
# teachers = Students()

# # Call the attendance method
# teachers.attendance()
# print(students)

class Students():
    def attendance(self):
        return input("Enter the students attendance.......")

# Create an instance of the class
teachers = Students()

# Call the attendance method and store the result
attendance_value = teachers.attendance()

# Print the entered attendance
print("Entered Attendance:", attendance_value)
