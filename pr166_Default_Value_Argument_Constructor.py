#constructor
#3.default value argument constructor
class ab:
    def __init__(self,x=10,y=20):
        self.a=x
        self.b=y
    def show(self):
        print(self.a,self.b)
m=int(input("enter first no. "))
n=int(input("enter second no."))
st=ab()
st.show()
pq=ab(m,n)
pq.show()
xy=ab(m)
xy.show()
