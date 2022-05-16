import pandas as pd

def loadXlxsFile(path):
    
    datas =pd.read_excel(path)  
  
    return datas
    
    
def getColoms(dataset,coloms):
    return dataset[coloms]
 
 

def init():   
        
    # dataset=loadXlxsFile('/home/marc/DEV/IndoorPlaning/IndoorPlaningApp/utilities/sites.xlsx')
    dataset=loadXlxsFile('/home/marc/Documents/Database OCM/test.xlsx')
    coloms=['Longitude','Latitude','SiteCode','Azimuth']
    LatLng=getColoms(dataset=dataset,coloms=coloms).head(10).values.tolist()
    print(LatLng)
    return LatLng   

