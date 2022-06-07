from email import message
from django.shortcuts import render,redirect

from django.views.generic import View
# Create your views here.
from django.contrib.auth import authenticate, login,logout


def logoout_user(request):
    logout(request)
    return redirect('login')
class Login(View):
    template_name = 'authentication/login.html'

    def get(self, request):
        return render(request, self.template_name)

    def post(self, request):
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        # Redirect to a success page.
        else:

            message='Identification echoué'
            return render(request, self.template_name,context={'message':message,'username':username, 'password':password})
    
    
        # return render(request, self.template_name,context={'message':message})

        # Return an 'invalid login' error message.
