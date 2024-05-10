#constructor
#2.parameterized constructor
class ab:
    def __init__(self,x,y):
        self.a=x
        self.b=y
    def show(self):
        print(self.a,self.b)
        self.c=self.a+self.b
        print(self.c)
m=int(input("enter first no. "))
n=int(input("enter second no."))
st=ab(m,n)
st.show()
