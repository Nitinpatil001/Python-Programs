#insert date into emp table of mydatabase.sqlite database
import sqlite3
cn=sqlite3.connect("mydatabase.sqlite")
cr=cn.cursor()
ch='y'
while ch=='y':
    en=input("enter empno")
    nm=input("enter name")
    sal=input("enter salary")
    query="insert into emp values("+en+",'"+nm+"',"+sal+")"
    cr.execute(query)
    cr.execute("commit")
    ch=input("continue(y/n)")
cn.close()
print("data stored")
