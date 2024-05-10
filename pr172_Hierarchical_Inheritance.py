#2.hierarchical inheritance
class stud:
    def inpt(self):
        self.r=int(input("enter rollno"))
        self.n=input("enter name")
class be(stud):
    def result(self):
        self.c=int(input("enter marks of c "))
        self.j=int(input("enter marks of java "))
        self.d=int(input("enter marks of dbms "))
        self.t=self.c+self.j+self.d
        self.p=self.t*100/300
        print(self.r,self.n,self.c,self.j,self.d,self.t,self.p)
class dbm(stud):
    def result(self):
        self.e=int(input("enter marks of eco "))
        self.a=int(input("enter marks of acc "))
        self.h=int(input("enter marks of hrm "))
        self.t=self.e+self.a+self.h
        self.p=self.t*100/300
        print(self.r,self.n,self.e,self.a,self.h,self.t,self.p)
st=be()
st.inpt()
st.result()
xy=dbm()
xy.inpt()
xy.result()
    
