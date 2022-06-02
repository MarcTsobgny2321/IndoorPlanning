from django.shortcuts import redirect, render
# Create your views here.

from django.views.generic import View
import utilities.notes as ut
from django.templatetags.static import static


def home(request):

    # dataset = ut.loadXlxsFile(static('sites.xlsx'))
    # coloms = ['Longitude', 'Latitude']
    # LatLng = ut.getColoms(dataset=dataset, coloms=coloms).values.tolist()

    return render(request, "IndoorApp/home.html")


def mapPage(request):

    # dataset = ut.loadXlxsFile(static('sites.xlsx'))
    # coloms = ['Longitude', 'Latitude']
    # LatLng = ut.getColoms(dataset=dataset, coloms=coloms).values.tolist()
    # head,datas=ut.init()

    return render(request, "IndoorApp/mapPage.html")

class GetCellInfo(View):
    template_name = 'IndoorApp/mapPage.html'

    def get(self, request):
        return render(request, self.template_name, context={})

    def post(self, request):

        lat = request.POST['latitude']
        lng = request.POST['longitude']
        op = request.POST['op']
        net = request.POST['network']
        AsiteID = request.POST['siteID']
        # AsiteID = request.POST.get('site ID',False)
        # AsiteID = request.POST.get('cell ID',False)
        AcellID = request.POST['cellID']
        head, networkOp = ut.init(operator=op, network=net)
        
        if networkOp.networkType=='4G':
            cellTag = ut.getCellInfos2(networkOp=networkOp, SiteID=AsiteID, CellID=AcellID)
        if networkOp.networkType=='3G':
            cellTag = ut.getCellInfos2(networkOp=networkOp, SiteID=AsiteID, CellID=AcellID)
        if networkOp.networkType=='2G':
            cellTag = ut.getCellInfos(dataset=networkOp.dataset, eNB=AsiteID, CID=AcellID)
        print(cellTag)
        pass
        
        angle=0
        Az=cellTag.Azimuth.values[0]
        print(f'Azimuth : {Az}')
        
        if Az <= 180 :
            angle=(180 + Az)%360
        elif (Az >180) & (Az<=360):
            angle=(Az-180)%360
        
        lat=float(cellTag.Latitude)
        lng=float(cellTag.Longitude)
        az=float(cellTag.Azimuth)
        print(f'Latitude : {lat} ; Longitude : {lng} ; Angle d\'orientation : {angle}')
        return render(request, self.template_name, context={'lat' :lat, 'lng' : lng,'Az':az,'dataset': networkOp.dataset,'head' : head,'cellTag' :ut.toValues(cellTag),'angle':angle})


class CurrentLocation(View):
    template_name = 'IndoorApp/home.html'

    def get(self, request):
        message = request.GET['currentLoc']
        print(f'la position entrée : {message}')
        return render(request, self.template_name, context={'message': message})

    def post(self, request):
        message = 'Identifiants invalides.'
        return render(request, self.template_name, context={'message': message})
