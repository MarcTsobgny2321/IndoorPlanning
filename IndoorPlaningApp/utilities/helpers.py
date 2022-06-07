class MMessage :
    def __init__(self,type,message):
        if(type==1):
            self.type="success"
        if(type==2):
            self.type="error"
        self.message=message