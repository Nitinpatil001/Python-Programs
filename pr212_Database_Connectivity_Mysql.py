#database connectivity using mysql
import mysql.connector
cn=mysql.connector.connect(host="localhost",user="root",password="",database="shivaji")
cr=cn.cursor()
query="insert into user values('rp','ram patil','seeta')"
cr.execute(query)
cr.execute("commit")
print("data stored")
cn.close()
