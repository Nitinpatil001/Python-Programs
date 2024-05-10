#5.2.hybrid inheritance
class emp:
    def getd(self):
        self.en=int(input("enter empno"))
        self.n=input("enter name ")
class dept(emp):
    def inpt(self):
        self.dname=input("enter deptname ")
class job(emp):
    def datint(self):
        self.desig=input("enter designation")
class pay(dept,job):
    def calc(self):
        self.b=int(input("enter payment "))
        self.da=self.b*.60
        self.hra=self.b*.10
        print(self.en,self.n,self.dname,self.desig,self.b,self.da,self.hra)
st=pay()
st.getd()
st.inpt()
st.datint()
st.calc()
