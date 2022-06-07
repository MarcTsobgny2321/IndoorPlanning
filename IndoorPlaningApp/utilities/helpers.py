

class MMessage :
    def __init__(self,type,message):
        if(type==1):
            self.type="success"
        if(type==2):
            self.type="error"
        self.message=message
        
        


class Test :
    x=10
    def test(self):
     global x
     x=25



# t=Test()
# print(t.x)
# t.test()
# print(t.x)