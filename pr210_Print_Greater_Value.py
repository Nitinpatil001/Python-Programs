#display only those whose salary morethan 5000rs.
import sqlite3
cn=sqlite3.connect("mydatabase.sqlite")
cr=cn.cursor()
query="select * from emp where salary>5000"
result=cr.execute(query)
for i in result.fetchall():
    print(i)
cn.close()
