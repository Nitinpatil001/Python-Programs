#constructor
#1.default constructor
#print factorial of given no. using constructor
class ab:
    def __init__(self):
        self.a=1
        self.c=1
    def fact(self):
        self.n=int(input("enter no."))
        while self.a<=self.n:
            self.c=self.c*self.a
            self.a=self.a+1
        print("factorial=",self.c)
        

st=ab()
st.fact()
