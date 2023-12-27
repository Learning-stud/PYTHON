class Myexception(Exception):
  pass
try:
 number1 = int(input("Enter A positive Number "))
 if number1 < 0:
   raise Myexception
 print("Enter Number : ",number1)


 number2 = int(input("Enter Another No"))
 if number2 < 0 :
   raise Myexception
 print("Enter Number : ",number2)
except:
  print("Number Must Be Positive.")
