#class
class stud:
    def getd(self):
        self.r=int(input("enter rollno"))
        self.n=input("enter name")
        self.m=int(input("enter marathi "))
        self.h=int(input("enter hindi "))
        self.e=int(input("enter english "))
    def result(self):
        self.t=self.m+self.h+self.e
        self.p=self.t*100/300
        print(self.r,self.n,self.m,self.h,self.e,self.t,self.p)
st=stud()
st.getd()
st.result()
