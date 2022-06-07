from tracemalloc import stop
from typing import List
import pandas as pd
import utilities.helpers as hp

def loadXlxsFile(path):

    datas = pd.read_excel(path)

    return datas


def getColoms(dataset, coloms):
    return dataset[coloms]


def chooseDB(operator, network):
    pass


class NetworkOperator:
    def __init__(self, name, networkType, dataset):
        self.name = name
        self.networkType = networkType
        self.dataset = dataset
        
    def delete(self):
        del self


def init(operator, network):
    # Pandas comparaison
    # https://towardsdatascience.com/using-logical-comparisons-with-pandas-dataframes-3520eb73ae63
    head=[]
    networkOp=NetworkOperator("","","")
    erros=[]
    # dataset=loadXlxsFile('/home/marc/DEV/IndoorPlaning/IndoorPlaningApp/utilities/sites.xlsx')
    try:
        print(f'\n ******  Chargement de la base données ' +
              operator+'_'+network+'.xlsx\n*****')
        dataset = loadXlxsFile(
            '/home/marc/Documents/Database OCM/'+operator+'_'+network+'.xlsx')
        print('\n ******Chargé avec succes\n ******')

        # You do your operations here
    except NameError:
        # If there is ExceptionI, then execute this block.
        print("Fichier inexistant")
        # erros.append("Fichier inexistant")
        erros.append(hp.MMessage(2,"Fichier inexistant"))
    except Exception:
        # If there is ExceptionII, then execute this block.
        print("Des erreurs sont survenues lors du chargement") 
        # erros.append(("Erreur de chargement"))
        erros.append(hp.MMessage(2,"Des erreurs sont survenues lors du chargement"))
        
    else:
        #  If there is no exception then execute this block.
        # coloms=['Longitude','Latitude','SiteCode','Azimuth']

        head = dataset.columns
        networkOp = NetworkOperator(
        name=operator, networkType=network, dataset=dataset)
    # print(networkOp.dataset)
    # stop

    # print(dataset.head(5))
    # LatLng=getColoms(dataset=dataset,coloms=coloms).head(20).values.tolist()
    # return (head.tolist(),dataset.values.tolist())


    # return (head, dataset)
    return (head, networkOp,erros)


def getCellInfos2(networkOp, SiteID, CellID):
    # print(f'**********\ntpupe :{type(int(SiteID))}')
    if networkOp.name == 'OrangeCM':
        if networkOp.networkType == '4G':
            str = f'{SiteID}_{CellID}'
            res = networkOp.dataset[networkOp.dataset['LNBTS _Cell ID'] == str]
        elif networkOp.networkType == '3G':
            #   dataset[(dataset['RNCID'] == 307) & (dataset['CellID'] == 30345)]
            res = networkOp.dataset[(networkOp.dataset['RNCID'] == int(
                SiteID)) & (networkOp.dataset['CellID'] == int(CellID))]
        elif networkOp.networkType == '2G':
            res = networkOp.dataset[networkOp.dataset['CI'] == int(CellID)]

    return res


def toListM(dataset):
    return dataset.tolist()


def toValues(dataset):
    return dataset.values.tolist()
# h,d=init('OrangeCM','4G')

# cell =getCellInfos(d,50688,2)
# print(cell.Longitude)

