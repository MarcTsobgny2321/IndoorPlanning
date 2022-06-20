

import os
import pickle


class MMessage:
    def __init__(self, type, message):
        if(type == 1):
            self.type = "success"
        if(type == 2):
            self.type = "error"
        self.message = message


class Test:
    x = 10

    def test(self):
     global x
     x = 25


# t=Test()
# print(t.x)
# t.test()
# print(t.x)


# class OutdoorConfig :
#     def __init(self,azimuth,)


# class Company(object):
#     def __init__(self, name, value):
#         self.name = name
#         self.value = value

# with open('company_data.pkl', 'wb') as outp:
#     company1 = Company('banana', 40)
#     pickle.dump(company1, outp, pickle.HIGHEST_PROTOCOL)

#     company2 = Company('spam', 42)
#     pickle.dump(company2, outp, pickle.HIGHEST_PROTOCOL)

# del company1
# del company2

# with open('company_data.pkl', 'rb') as inp:
#     company1 = pickle.load(inp)
#     print(company1.name)  # -> banana
#     print(company1.value)  # -> 40

#     company2 = pickle.load(inp)
#     print(company2.name) # -> spam
#     print(company2.value)  # -> 42

MSC = "mySavedConf.pkl"
TOS = "tagedOutdoorSite.pkl"

url_map_imape="/media/maps/defaultMap.jpg"

def savePickleData(filename, toSave):
    if os.path.exists(filename):
      os.remove(filename)
    # import time
    # time.sleep(10) 

    outp=open(filename,'wb')
    pickle.dump(toSave, outp, pickle.HIGHEST_PROTOCOL)
    outp.close()

# Containt  outdoor properties for projects
def getPickData(filename):
    if os.path.exists(filename):
        inp=open(filename,'rb')
        return pickle.load(inp)
    


# mySavedConf=getPickData(MSC)

# tagedOutdoorSite=getPickData(TOS)