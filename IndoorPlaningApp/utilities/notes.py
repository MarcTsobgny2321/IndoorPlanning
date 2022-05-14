import pandas as pd

def loadXlxsFile(path):
    
    datas =pd.read_excel(path)  
  
    return datas
    
    
def getColoms(dataset,coloms):
    return dataset[coloms]
 
 

def init():   
        
    dataset=loadXlxsFile('/home/marc/DEV/IndoorPlaning/IndoorPlaningApp/utilities/sites.xlsx')
    coloms=['Longitude','Latitude','CI']
    LatLng=getColoms(dataset=dataset,coloms=coloms).head(30).values.tolist()
    return LatLng   


