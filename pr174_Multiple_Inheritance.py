#3.multiple inheritance
class emp:
    def getd(self):
        self.en=int(input("enter empno "))
        self.n=input("enter name ")
class dept:
    def inpt(self):
        self.dn=input("enter deptname ")
class pay(emp,dept):
    def calc(self):
        self.b=int(input("enter payment "))
        self.da=self.b*.60
        self.hra=self.b*.10
        print(self.en,self.n,self.dn,self.b,self.da,self.hra)
st=pay()
st.getd()
st.inpt()
st.calc()
