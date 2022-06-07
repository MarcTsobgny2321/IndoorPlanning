from genericpath import exists
from re import L
from django.shortcuts import redirect, render
# Create your views here.

from django.views.generic import View
from utilities.helpers import MMessage
import utilities.notes as ut
from django.templatetags.static import static
from django.contrib.auth.decorators import login_required


@login_required
def home(request):

    # dataset = ut.loadXlxsFile(static('sites.xlsx'))
    # coloms = ['Longitude', 'Latitude']
    # LatLng = ut.getColoms(dataset=dataset, coloms=coloms).values.tolist()

    return render(request, "IndoorApp/home.html")

@login_required
def mapPage(request):

    # dataset = ut.loadXlxsFile(static('sites.xlsx'))
    # coloms = ['Longitude', 'Latitude']
    # LatLng = ut.getColoms(dataset=dataset, coloms=coloms).values.tolist()
    # head,datas=ut.init()

    return render(request, "IndoorApp/mapPage.html")


class Cell:
    def __init__(self, lat, lng, description):
        self.lat = lat
        self.lng = lng
        self.description = description

class GetCellInfo(View):
    template_name = 'IndoorApp/mapPage.html'
    # @login_required
    def get(self, request):
        return render(request, self.template_name, context={})
    # @login_required
    def post(self, request):

        latM = float(request.POST['latitude'])
        lngM = float(request.POST['longitude'])
        op = request.POST['op']
        net = request.POST['network']
        AsiteID = request.POST['siteID']
        # AsiteID = request.POST.get('site ID',False)
        # AsiteID = request.POST.get('cell ID',False)
        AcellID = request.POST['cellID']
        head, networkOp,erros = ut.init(operator=op, network=net)
        print(f"\n\n\n\n\n\n $$$$ type de erros :{type(erros)} \n\n\n\n\n\n $$$$")    
        if not erros:
            
            if networkOp.networkType == '4G':
                cellTag = ut.getCellInfos2(
                    networkOp=networkOp, SiteID=AsiteID, CellID=AcellID)
            if networkOp.networkType == '3G':
                cellTag = ut.getCellInfos2(
                    networkOp=networkOp, SiteID=AsiteID, CellID=AcellID)
            if networkOp.networkType == '2G':
                cellTag = ut.getCellInfos2(
                    networkOp=networkOp, SiteID=AsiteID, CellID=AcellID)
            print(cellTag)

            if not cellTag.empty:
                angle = 0
                Az = cellTag.Azimuth.values[0]
                print(f'Azimuth : {Az}')

                if Az <= 180:
                    angle = (180 + Az) % 360
                elif (Az > 180) & (Az <= 360):
                    angle = (Az-180) % 360

                latT = float(cellTag.Latitude)
                lngT = float(cellTag.Longitude)
                az = float(cellTag.Azimuth)
                print(
                    f'Latitude : {latT} ; Longitude : {lngT} ; Angle d\'orientation : {angle}')
                des = ""
                print(f'type de cellTag : {cellTag}')
                for val in cellTag:
                    #  print(i, ",", val,",",cellTag[val].values[0])
                    des = f'{des}  {val} : {cellTag[val].values[0]} |  '

                cellT = Cell(lat=latT, lng=lngT, description=des)
                print(cellT.description)          
                erros.append(MMessage(1,'Fichier chargé avec succès'))
                return render(request, self.template_name, context={'erros':erros,'cellT': cellT, 'latM': latM, 'lngM': lngM, 'lat': latT, 'lng': lngT, 'Az': az, 'dataset': networkOp.dataset, 'head': head, 'cellTag': ut.toValues(cellTag), 'angle': angle})
      
            else:
                print('Erreur : aucune donné trouvé')
                erros.append(MMessage(2,"Aucun site trouvé"))
                return render(request, self.template_name, context={'erros': erros})
                
        else :
            print('Des érreurs survenuues lors du chatgement de la bd')
            return render(request, self.template_name, context={'erros': erros})
            

        # return render(request, self.template_name, context={'latM' : latM, 'lngM' : lngM,'lat' :latT, 'lng' : lngT,'Az':az,'dataset': networkOp.dataset,'head' : head,'cellTag' :ut.toValues(cellTag),'angle':angle})

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
