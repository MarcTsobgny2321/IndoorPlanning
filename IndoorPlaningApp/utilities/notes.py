from tracemalloc import stop
import pandas as pd

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


def init(operator, network):
    # Pandas comparaison
    # https://towardsdatascience.com/using-logical-comparisons-with-pandas-dataframes-3520eb73ae63

    # dataset=loadXlxsFile('/home/marc/DEV/IndoorPlaning/IndoorPlaningApp/utilities/sites.xlsx')
    print(f'\n ******  Chargement de la base données ' + operator+'_'+network+'.xlsx\n*****')
    dataset = loadXlxsFile('/home/marc/Documents/Database OCM/'+operator+'_'+network+'.xlsx')
    print('\n ******Chargé avec succes\n ******')
    # coloms=['Longitude','Latitude','SiteCode','Azimuth']

    head = dataset.columns
    networkOp=NetworkOperator(name=operator,networkType=network,dataset=dataset)
    # print(networkOp.dataset)
    # stop
    
    # print(dataset.head(5))
    # LatLng=getColoms(dataset=dataset,coloms=coloms).head(20).values.tolist()
    # return (head.tolist(),dataset.values.tolist())

    # return (head, dataset)
    return (head,networkOp)


def getCellInfos(dataset, eNB, CID):
    str = f'{eNB}_{CID}'
    res = dataset[dataset['LNBTS _Cell ID'] == str]
    return res



def getCellInfos2(networkOp, SiteID, CellID):
    # print(f'**********\ntpupe :{type(int(SiteID))}')
    if networkOp.name=='OrangeCM':
      if networkOp.networkType=='4G':
        str = f'{SiteID}_{CellID}'
        res = networkOp.dataset[networkOp.dataset['LNBTS _Cell ID'] == str]
      elif networkOp.networkType=='3G':
        #   dataset[(dataset['RNCID'] == 307) & (dataset['CellID'] == 30345)]
        res = networkOp.dataset[(networkOp.dataset['RNCID'] == int(SiteID)) & (networkOp.dataset['CellID'] == int(CellID))]
      elif networkOp.networkType=='2G':
        str = f'{SiteID}_{CellID}'
        res = networkOp.dataset[networkOp.dataset['LNBTS _Cell ID'] == str]
    
    return res

def toListM(dataset):
    return dataset.tolist()


def toValues(dataset):
    return dataset.values.tolist()
# h,d=init('OrangeCM','4G')

# cell =getCellInfos(d,50688,2)
# print(cell.Longitude)
