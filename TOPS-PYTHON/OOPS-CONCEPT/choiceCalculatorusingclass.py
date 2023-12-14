class calculator():
 def __init__(self):
  print('''---------User Choice--------
        1.Addition
        2.Substraction
        3.Multiply
        4.Divide
       ''')

  def add(self,num1,num2):
   return num1+num2

  def sub(self,num1,num2):
   return num1-num2

  def multiply(self,num1,num2):
   return num1 * num2

  def divide(self,num1,num2):
      if num2!= 0:
       return num1 / num2
      else:
       return("Cannot Divide By Zero")



calculator=calculator()

# user input
num1=float(input("Enter First Number"))
num2=float(input("Enter Second Number"))

# User choice For Calciulation Of User Choice

choice= input("Enter Choice (1/2/3/4)")

if choice == '1':
 result=calculator.add(num1,num2)

elif choice =='2':
 result = calculator.sub(num1,num2)

elif choice == '3':
 result = calculator.multiply(num1,num2)

elif choice == '4':
 result = calculator.divide(num1,num2)

else:
 result = "Invalid Choice !"

print(f"Results => {result}" )