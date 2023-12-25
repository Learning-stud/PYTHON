"""
THERE ARE 2 TYPES OF EXCEPTION

1ST => BUILT - IN EXCEPTION
2ND => USER DEFIND OR CUSTOM EXCEPTION

       WHICH IS CREATED BY USER AND WE CAN CALL AS PER REQUIRMENT

"""


class Myexception(Exception):
 pass
try:
 num = int(input("Enter A Number"))
 if num < 0:
    raise Myexception
except Myexception:
  print("Number Must Be positive ")