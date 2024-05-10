#default value argumet class function
class ab:
    def add(self,x=10,y=20):
        self.m=x
        self.n=y
        self.z=self.m+self.n
        print(self.z)
a=int(input("enter first "))
b=int(input("enter second "))
st=ab()
st.add()
st.add(a,b)
st.add(a)
