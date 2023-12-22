import pymysql

mydb = pymysql.connect(host="localhost",user="root",passwd="")
mycursor=mydb.cursor()

mycursor.execute("create database topspython")

mydb.commit()