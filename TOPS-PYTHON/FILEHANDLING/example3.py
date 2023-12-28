f = open("file.txt","a")
for i in range(5):
  name = input("Enter Your name : ")
  f.write("\n" + name)

f.close()