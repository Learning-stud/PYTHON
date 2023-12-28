count = 0
file = open("file.txt","r")

data = file.read()
datas = data.split()
for words in datas:
 if not words.isnumeric():
     count += 1
     print(words)


print("Total Nubers of Words ",count)