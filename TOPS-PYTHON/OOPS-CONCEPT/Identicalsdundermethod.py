# class A:
#  def __init__(self,a):
#   self.a = a

#  def __eq__(self,a):
#    return self.a == a

# obj1 = A(12,)
# obj2 = A(13)

# print(obj1==obj2)



class A:
 def __init__(self,a,b):
  self.a = a
  self.b = b

 def __eq__(self,x):
   return (self.a == x.a and self.b == x.b)

obj1 = A(12,3)
obj2 = A(2,3)

print(obj1==obj2)