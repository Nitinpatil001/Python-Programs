#demonstrate the constructor and destructor
class ab:
    def __init__(self):
        print("in constructor")
    def __del__(self):
        print("in destructor")
st=ab()
pq=ab()
