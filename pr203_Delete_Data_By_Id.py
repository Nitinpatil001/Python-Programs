#delete the data from user table of mydatabase.sqlite database
import sqlite3
cn=sqlite3.connect("mydatabase.sqlite")
cr=cn.cursor()
ui=input("enter userid ")
cr.execute("delete from user where userid='"+ui+"'")
cr.execute("commit")
print("data deleted")
cn.close()
