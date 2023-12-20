class Products:
 mobile = 15000
 __laptop = 75000

 def display(self):
  print(self.mobile)
  print(self.laptop)

 def modifyPrice(self,upadatedLaptop):
     self.__laptop= upadatedLaptop

product = Products()
product.display()
product.mobile=4500
product.laptop=85000