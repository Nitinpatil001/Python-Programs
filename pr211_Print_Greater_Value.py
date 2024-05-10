#display only those whose salary morethan 5000rs.
import sqlite3
cn=sqlite3.connect("mydatabase.sqlite")
cr=cn.cursor()
query="select * from emp"
result=cr.execute(query)
for i in result.fetchall():
    if i[2]>5000:
        print(i)
cn.close()
