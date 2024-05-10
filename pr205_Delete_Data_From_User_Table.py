#delete the data from user table of mydatabase.sqlite database
import sqlite3
cn=sqlite3.connect("mydatabase.sqlite")
cr=cn.cursor()
result=cr.execute("select * from user")
for i in result.fetchall():
    for j in i:
        print(j)
cn.close()
