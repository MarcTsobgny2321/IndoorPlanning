from django.shortcuts import redirect, render
# Create your views here.

def home(request):
    return render(request,"IndoorApp/home.html")




from django.views.generic import View


class CurrentLocation(View):
    template_name = 'IndoorApp/home.html'

    def get(self, request):
        message = request.GET['currentLoc']
        print(f'la position entrée : {message}')
        return render(request, self.template_name, context={ 'message': message})
        
    def post(self, request):
       
        message = 'Identifiants invalides.'
        return render(request, self.template_name, context={'message': message})