from django.shortcuts import redirect, render
# Create your views here.

from django.views.generic import View
import utilities.notes as ut
from django.templatetags.static import static
def home(request):


    # dataset = ut.loadXlxsFile(static('sites.xlsx'))
    # coloms = ['Longitude', 'Latitude']
    # LatLng = ut.getColoms(dataset=dataset, coloms=coloms).values.tolist()
    LatLng=ut.init()

    return render(request, "IndoorApp/home.html", context={'LatLng': LatLng})


class CurrentLocation(View):
    template_name = 'IndoorApp/home.html'

    def get(self, request):
        message = request.GET['currentLoc']
        print(f'la position entrée : {message}')
        return render(request, self.template_name, context={'message': message})

    def post(self, request):

        message = 'Identifiants invalides.'
        return render(request, self.template_name, context={'message': message})
