#2.hierarchical inheritance
class ab:
    def getd(self):
        self.a=int(input("enter first "))
        self.b=int(input("enter second "))
class pq(ab):
    def add(self):
        self.c=self.a+self.b
        print(self.c)
class xy(ab):
    def mul(self):
        self.d=self.a*self.b
        print(self.d)
st=pq()
st.getd()
st.add()
mn=xy()
mn.getd()
mn.mul()
