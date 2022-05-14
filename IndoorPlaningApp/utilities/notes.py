import pandas as pd

def loadXlxsFile(path):
    
    datas =pd.read_excel(path)  
  
    return datas
    
    
def getColoms(dataset,coloms):
    return dataset[coloms]
 
 

def init():   
        
    dataset=loadXlxsFile('/home/marc/DEV/IndoorPlaning/IndoorPlaningApp/utilities/sites.xlsx')
    coloms=['Longitude','Latitude']
    LatLng=getColoms(dataset=dataset,coloms=coloms).head().values.tolist()
    return LatLng   


