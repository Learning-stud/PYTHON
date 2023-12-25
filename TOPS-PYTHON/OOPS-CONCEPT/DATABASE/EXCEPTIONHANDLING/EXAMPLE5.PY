import sys


try:
 print(a)
except:
 print("SOMETHING WENT WRONG")
 print(sys.exc_info())
 print(sys.exc_info()[0])
 print(sys.exc_info()[1])