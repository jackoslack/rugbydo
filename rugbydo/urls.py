"""
URL configuration for rugbydo project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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

from .views import *

#from .views import home_page_view

#from .views import get_name

#from .views import about

#from .views import players

#from .views import show_settings

urlpatterns = [
    path('admin/', admin.site.urls),
    #
    path("about", about, name="about"),
    path("", home_page_view, name="home"),
    path("bdir", show_settings, name="bdir"),
    path("name", get_name, name="name"),
    path("players/<str:gender>", players, name="players"),
    path("players/", players, name="players"),
    path("points/", points, name="points"),
    path("points/<str:gender>", points, name="points"),
    path("mlist", mlist, name="mlist"),
    path("photologue", photologue, name="photologue"),
    path("photologue/gallery", photologue, name="photologue"),
    
    
    
]

# Use static() to add url mapping to serve static files during development (only)
from django.conf import settings
from django.conf.urls.static import static

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)