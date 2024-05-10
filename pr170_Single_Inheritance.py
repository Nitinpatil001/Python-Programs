#1.single inheritance
class stud:
    def inpt(self):
        self.r=int(input("enter rollno"))
        self.n=input("enter name")
class mark(stud):
    def result(self):
        self.m=int(input("enter marathi "))
        self.h=int(input("enter hindi "))
        self.e=int(input("enter english "))
        self.t=self.m+self.h+self.e
        self.p=self.t*100/300
        print(self.r,self.n,self.m,self.h,self.e,self.t,self.p)
st=mark()
st.inpt()
st.result()
