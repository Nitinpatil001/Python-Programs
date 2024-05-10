#1.single inheritance
class ab:
    def getd(self):
        self.a=int(input("enter first "))
        self.b=int(input("enter second "))
class pq(ab):
    def add(self):
        self.c=self.a+self.b
        print(self.c)
st=pq()
st.getd()
st.add()
