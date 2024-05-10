#passing arguments to class function
class ab:
    def add(self,x,y):
        self.m=x
        self.n=y
        self.z=self.m+self.n
        print(self.z)
a=int(input("enter first "))
b=int(input("enter second "))
st=ab()
st.add(a,b)
