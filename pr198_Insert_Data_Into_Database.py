#store the data into user table of mydatabase.sqlite database
import sqlite3
cn=sqlite3.connect("mydatabase.sqlite")
cr=cn.cursor()
cr.execute("insert into user values('1','ram','seeta')")
cr.execute("commit")
print("data stored")
cn.close()
