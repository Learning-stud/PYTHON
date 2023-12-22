# TRY WITH MULTIPLE EXCEPTION
try :
 num1 =int(input("Enter A number "))
 num2  =int(input("Enter A number2 "))
 ans =num1 / num2
 print(ans)

except ValueError:
 print("invalid input")
except ZeroDivisionError :
 print("Cannot divide by 0")
