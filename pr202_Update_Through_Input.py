#update the data of user table of mydatabase.sqlite database
import sqlite3
cn=sqlite3.connect("mydatabase.sqlite")
cr=cn.cursor()
ui=input("enter userid ")
un=input("enter username ")
ps=input("enter password ")
cr.execute("update user set username='"+un+"',password='"+ps+"' where userid='"+ui+"'")
cr.execute("commit")
print("data updated")
cn.close()
