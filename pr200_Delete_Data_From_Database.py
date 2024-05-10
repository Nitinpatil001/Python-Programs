#delete the data from user table of mydatabase.sqlite database
import sqlite3
cn=sqlite3.connect("mydatabase.sqlite")
cr=cn.cursor()
cr.execute("delete from user where userid='1'")
cr.execute("commit")
print("data deleted")
cn.close()
