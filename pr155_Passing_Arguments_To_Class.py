#passing arguments to class function
class ab:
    def add(self,x,y):
        self.z=x+y
        print(self.z)
a=int(input("enter first "))
b=int(input("enter second "))
st=ab()
st.add(a,b)
