# f = open("file.txt","r")
# d = f.read()
# print(d)


f = open("file.txt","r")
# d = f.read()
d = f.readline()  # for displaying  first word
d = f.readlines()  # for displaying  Every word
# print("No Of Lines",len(d))
print(d)