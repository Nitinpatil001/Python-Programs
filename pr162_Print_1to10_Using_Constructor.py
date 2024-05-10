#constructor
#1.default constructor
#print 1 to 10 nos using constructor
class ab:
    def __init__(self):
        self.a=1
    def disp(self):        
        while self.a<=10:
            print(self.a)
            self.a=self.a+1
st=ab()
st.disp()
