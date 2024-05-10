#returning value thru  class function
class ab:
    def add(self,x,y):
        self.m=x
        self.n=y
        self.z=self.m+self.n
        return self.z
a=int(input("enter first "))
b=int(input("enter second "))
st=ab()
c=st.add(a,b)
print(c)
