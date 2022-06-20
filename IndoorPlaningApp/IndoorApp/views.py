from genericpath import exists
from re import L
from threading import local
from time import sleep
from django.shortcuts import redirect, render
# Create your views here.

from django.views.generic import View
from utilities.helpers import MMessage
import utilities.helpers as hp
import utilities.notes as ut
from django.templatetags.static import static
from django.contrib.auth.decorators import login_required
import pickle


from django.core.files.storage import FileSystemStorage


@login_required
def home(request):

    # dataset = ut.loadXlxsFile(static('sites.xlsx'))
    # coloms = ['Longitude', 'Latitude']
    # LatLng = ut.getColoms(dataset=dataset, coloms=coloms).values.tolist()

    return render(request, "IndoorApp/home.html", context={'msc': hp.getPickData(hp.MSC),
                                                           'cell': hp.getPickData(hp.TOS),
                                                           })


@login_required
def mapPage(request):

    # dataset = ut.loadXlxsFile(static('sites.xlsx'))
    # coloms = ['Longitude', 'Latitude']
    # LatLng = ut.getColoms(dataset=dataset, coloms=coloms).values.tolist()
    # head,datas=ut.init()

    return render(request, "IndoorApp/mapPage.html", context={'msc': hp.getPickData(hp.MSC),
                                                              'cell': hp.getPickData(hp.TOS),
                                                              })


class Cell:
    def __init__(self, lat, lng, description):
        self.lat = lat
        self.lng = lng
        self.description = description


x = 10

head = []
networkOp = ut.NetworkOperator("", "", "")
errors = []


class GetCellInfo(View):
    print("Debut appel classe GetCellInfo")
    template_name = 'IndoorApp/mapPage.html'

    # @login_required
    def get(self, request):
        global x
        x = 25
        log = []
        if('op' in request.GET and 'network' in request.GET):
            global head
            global networkOp
            global errors
            head, networkOp, errors = ut.init(
                operator=request.GET['op'], network=request.GET['network'])

            log.append(MMessage(
                1, f"Base de données  {networkOp.name} {networkOp.networkType} chargée avec succes"))

            return render(request, self.template_name, context={'logs': log,
                                                                'op': networkOp,
                                                                'msc': hp.getPickData(hp.MSC),
                                                                'cell': hp.getPickData(hp.TOS),
                                                                })
        return render(request, self.template_name, context={'msc': hp.getPickData(hp.MSC),
                                                            'cell': hp.getPickData(hp.TOS),
                                                            })

    # @login_required
    def post(self, request):

        latM = float(request.POST['latitude'])
        lngM = float(request.POST['longitude'])
        # op = request.POST['op']
        # net = request.POST['network']
        AsiteID = request.POST['siteID']
        # AsiteID = request.POST.get('site ID',False)
        # AsiteID = request.POST.get('cell ID',False)
        AcellID = request.POST['cellID']
        # head, networkOp,erros = ut.init(operator=op, network=net)

        # global errors
        # print(f'\n\n\n\n$$$ Le réseau choisit {} ')
        logs = []
        if not errors:
            if networkOp.networkType == '4G':
                cellTag = ut.getCellInfos2(
                    networkOp=networkOp, SiteID=AsiteID, CellID=AcellID)
            if networkOp.networkType == '3G':
                print("\n\n Je fouille en 3G \n\n")
                cellTag = ut.getCellInfos2(
                    networkOp=networkOp, SiteID=AsiteID, CellID=AcellID)
            if networkOp.networkType == '2G':
                cellTag = ut.getCellInfos2(
                    networkOp=networkOp, SiteID=AsiteID, CellID=AcellID)

            if 'cellTag' in locals() and not cellTag.empty:

                cell = cellTag.to_dict('records')[0]

                print(f"\n\n\n$$$$$Before save All {cell}\n\n\n$$$$$ ")

                hp.savePickleData(hp.TOS, cell)

                print(f"\n\n\n$$$$$ All {hp.getPickData(hp.TOS)}\n\n\n$$$$$ ")

                angle = 0
                Az = cellTag.Azimuth.values[0]
                # print(f'Azimuth : {Az}')

                if Az <= 180:
                    angle = (180 + Az) % 360
                elif (Az > 180) & (Az <= 360):
                    angle = (Az-180) % 360

                latT = float(cellTag.Latitude)
                lngT = float(cellTag.Longitude)
                az = float(cellTag.Azimuth)
                # print(
                #     f'Latitude : {latT} ; Longitude : {lngT} ; Angle d\'orientation : {angle}')
                des = ""
                # print(f'type de cellTag : {cellTag}')
                for val in cellTag:
                    #  print(i, ",", val,",",cellTag[val].values[0])
                    des = f'{des}  {val} : {cellTag[val].values[0]} |  '

                cellT = Cell(lat=latT, lng=lngT, description=des)
                # print(cellT.description)
                logs.append(MMessage(1, 'Site trouvé chargé avec succès'))

                mySavedConf = {}
                mySavedConf.update({"Operator": networkOp.name})
                mySavedConf.update({"networkType": networkOp.networkType})
                mySavedConf.update({"Targed Cell Identified": AsiteID})
                mySavedConf.update({"Targed Site Identified": AcellID})
                mySavedConf.update({"Received Power": "xxx Dbm"})
                mySavedConf.update({"Azimuth": angle})

                # outp=open("mySavedConf.pkl",'wb')
                # pickle.dump(hp.mySavedConf, outp, pickle.HIGHEST_PROTOCOL)
                # outp.close()

                hp.savePickleData(hp.MSC, mySavedConf)
                return render(request, self.template_name, context={
                    'op': networkOp,
                    'logs': logs,
                    'cellT': cellT,
                    'latM': latM,
                    'lngM': lngM,
                    'lat': latT,
                    'lng': lngT,
                    'Az': az,
                    'dataset': networkOp.dataset,
                    'head': head,
                    'cellTag': ut.toValues(cellTag),
                    'angle': angle,
                    'msc': hp.getPickData(hp.MSC),
                    'cell': hp.getPickData(hp.TOS),
                })

            else:
                print('Erreur : aucune donné trouvé')
                logs.append(MMessage(2, "Aucun site trouvé"))
                return render(request, self.template_name, context={'op': networkOp, 'logs': logs})

        else:
            print('Des érreurs survenuues lors du chatgement de la bd')
            errors.append(
                MMessage(2, 'Des érreurs survenuues lors du chatgement de la bd'))
            return render(request, self.template_name, context={'op': networkOp, 'logs': errors})

        # return render(request, self.template_name, context={'latM' : latM, 'lngM' : lngM,'lat' :latT, 'lng' : lngT,'Az':az,'dataset': networkOp.dataset,'head' : head,'cellTag' :ut.toValues(cellTag),'angle':angle})


def stopNetwork(request):

    # dataset = ut.loadXlxsFile(static('sites.xlsx'))
    # coloms = ['Longitude', 'Latitude']
    # LatLng = ut.getColoms(dataset=dataset, coloms=coloms).values.tolist()
    # head,datas=ut.init()
    # del networkOp
    if 'networkOp' in globals():
        global networkOp
        del networkOp
    return redirect('getCellInfos')


class CurrentLocation(View):
    template_name = 'IndoorApp/home.html'

    @login_required
    def get(self, request):
        message = request.GET['currentLoc']
        print(f'la position entrée : {message}')
        return render(request, self.template_name, context={'message': message})

    @login_required
    def post(self, request):
        message = 'Identifiants invalides.'
        return render(request, self.template_name, context={'message': message})


class IndoorMapPlanner(View):
    template_name = 'IndoorApp/indoorMapPlanner.html'

    def get(self, request):
        print('Appel de IndoorMapPlanner')
        return render(request, self.template_name, context={
            'msc': hp.getPickData(hp.MSC),
            'cell': hp.getPickData(hp.TOS),
            'image_url': hp.url_map_imape,
        })

    def post(self, request):
        pass


def uploadMap(request):
    template_name = 'IndoorApp/indoorMapPlanner.html'

    if request.method == 'POST' and request.FILES['imageMap']:
        upload = request.FILES['imageMap']
        print(f'\n\n\n ******Mon fichier : : : : {upload} ***\n\n')
        fss = FileSystemStorage()
        file = fss.save(upload.name, upload)
        image_url = fss.url(file)
        
        hp.url_map_imape = image_url
        return render(request, template_name, context={'image_url': hp.url_map_imape,
                                                       'msc': hp.getPickData(hp.MSC),
                                                       'cell': hp.getPickData(hp.TOS)
                                                       })
    return render(request, template_name, context={
        'image_url': hp.url_map_imape,
                  'msc': hp.getPickData(hp.MSC),
                  'cell': hp.getPickData(hp.TOS)})


class CellM:

    def __init__(self, Latitude, Longitude):
        self.Latitude = Latitude
        self.Longitude = Longitude
