#update the data of user table of mydatabase.sqlite database
import sqlite3
cn=sqlite3.connect("mydatabase.sqlite")
cr=cn.cursor()
cr.execute("update user set username='ramesh',password='suresh' where userid='1'")
cr.execute("commit")
print("data updated")
cn.close()
