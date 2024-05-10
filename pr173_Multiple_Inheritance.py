#3.multiple inheritance
class ab:
    def getd(self):
        self.a=int(input("enter first "))
class pq:
    def inpt(self):
        self.b=int(input("enter second "))
class xy(ab,pq):
    def calc(self):
        self.c=self.a+self.b
        print(self.c)
st=xy()
st.getd()
st.inpt()
st.calc()
