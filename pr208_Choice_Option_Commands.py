#insert,update,delete,display with choice option
import sqlite3
cn=sqlite3.connect("mydatabase.sqlite")
cr=cn.cursor()
ch=0
while ch!=5:
    print("1.insert")
    print("2.update")
    print("3.delete")
    print("4.display")
    print("5.exit")
    ch=int(input("enter choice"))
    if ch==1:
        ui=input("enter userid")
        un=input("enter username")
        ps=input("enter password")
        query="insert into user values('"+ui+"','"+un+"','"+ps+"')"
        cr.execute(query)
        cr.execute("commit")
        print("record inserted")
    elif ch==2:
        ui=input("enter userid")
        un=input("enter username")
        ps=input("enter password")
        query="update user set username='"+un+"', password='"+ps+"' where userid='"+ui+"'"
        cr.execute(query)
        cr.execute("commit")
        print("record updated")
    elif ch==3:
        ui=input("enter userid")
        query="delete from user where userid='"+ui+"'"
        cr.execute(query)
        cr.execute("commit")
        print("record deleted")
    elif ch==4:
        query="select * from user"
        result=cr.execute(query)
        for i in result.fetchall():
            print(i)
cn.close()
