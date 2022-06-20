"""IndoorPlaningApp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
import IndoorApp.views
import authentication.views
from django.conf import settings #add this
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls, name='admin'),
    path('home/', IndoorApp.views.home, name='home'),
    path('mapPage/', IndoorApp.views.mapPage, name='mapPage'),
    path('mapPage/getCelInfos', IndoorApp.views.GetCellInfo.as_view(), name="getCellInfos"),
    path('', IndoorApp.views.home, name='home'),
    path('currentLocation/', IndoorApp.views.CurrentLocation.as_view(), name='currentLocation'),
    path('login/',authentication.views.Login.as_view(), name='login'),
    path('logout/',authentication.views.logoout_user, name='logout'),
    path('stopNetwork/',IndoorApp.views.stopNetwork, name='stopNetwork'),
    path('indoorMapPlanner/',IndoorApp.views.IndoorMapPlanner.as_view(), name='indoorMapPlanner'),
    
    path('indoorMapPlanner/uploadMap',IndoorApp.views.uploadMap, name='uploadMap'),
    
    
    
    
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
