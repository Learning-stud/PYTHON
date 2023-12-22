import pymysql
mydb = pymysql.connect(host="localhost",user="root",passwd="",database="topspython")
mycursor=mydb.cursor()
menu = '''
         press 1 for add student
         press 2 for student update
         press 3 for delete data of student
         press 4 for display student





       '''
def addOpration():
 print("--------------ADD STUDENT----------------")
 name = input("Enter name : ")
 subject = input("Enter Subject : ")

 args= (name,subject)
 query= "insert into  student (name , subject) values('%s','%s')"

 mycursor.execute(query % args)
 mydb.commit()

def updateOpration():
 id - int(input("Which Student Do You Want To Update : "))
 name = input("Enter Update Name: ")
 subject = input("Enter Update Subject: ")

 args =(name,subject,id)
 query = "Update student set name '%s', subject='%s',wher id ='%s'"

 mycursor.execute(query % args)
 mydb.commit()


def searchOpration():
 name= input("Enter Yoyr Name ")
 query= "select * from student where name = '%s'"
 args = (name)
 mycursor.execute(query % args)
 res = mycursor.fetchone()
 print(res[0])
 print(res[1])
 print(res[2])

status = True
while status:
 print(menu)
 choice = int(input("Enter Your Choice : "))
 if choice == 1:
  addOpration()
 elif choice==2:
  updateOpration()
 elif choice ==4:
  searchOpration()
 u_choice= input("Do You Want to performm more opration press y for yes and press n for no")
 if u_choice == 'y' or u_choice == 'yes':
  status=True
 else:
  status = False
