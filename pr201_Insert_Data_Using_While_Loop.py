#insert the data into user table of mydatabase.sqlite database
import sqlite3
cn=sqlite3.connect("mydatabase.sqlite")
cr=cn.cursor()
ch='y'
while ch=='y':
    ui=input("enter userid ")
    un=input("enter username ")
    ps=input("enter password ")
    cr.execute("insert into user values('"+ui+"','"+un+"','"+ps+"')")
    cr.execute("commit")
    ch=input("continue(y/n)")

print("data inserted")
cn.close()
