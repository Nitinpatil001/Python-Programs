#class
class ab:
    def assign(self):
        self.a=10
        self.b=20
    def disp(self):
        print(self.a,self.b)#it displays error because b is not class member
        
st=ab()
st.assign()
st.disp()
