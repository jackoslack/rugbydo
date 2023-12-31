# pages/views.py
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.shortcuts import render

from .forms import NameForm

def about(request):
     
    return render(request, 'about.html')
    

def show_settings(request):
    
    from django.conf import settings

    staticfiles_dirs = settings.STATICFILES_DIRS
    static_url = settings.STATIC_URL
    project_root = settings.PROJECT_ROOT
    static_root = settings.STATIC_ROOT


    return render(request, 'bdir.html', 
                  {'static_root': static_root, 
                   'staticfiles_dirs': staticfiles_dirs, 
                   'static_url': static_url,
                   'project_root': project_root},
        )

def home_page_view(request):
  
    return render(request, 'home.html')

def photologue(request):

    title = "Photo Gallery"
  
    return render(request, 'gallery.html',{ "title" : title})

def players(request, gender="None"):

    if gender == "M":
        gender = "Mens"
    elif gender == "F":
        gender = "Womens"
    else:
        gender = ""
    
    title = "Player Stats"
    
    return render(request, 'players.html', {"title" : title , "gender" : gender})


def points(request, gender="None"):

    if gender == "M":
        gender = "Mens"
    elif gender == "F":
        gender = "Womens"
    else:
        gender = ""
    
    title = "Player Career Points"
    
    return render(request, 'points.html', {"title" : title , "gender" : gender})

def mlist(request):

    title = "Match List"
  
    return render(request, 'matches.html', { "title": title })

def reps(request):

    title = "Reps"
  
    return render(request, 'home.html', { "title": title })

def get_name(request):

    if request.method == 'POST':
        name = request.POST.get('name')
        return render(request, 'name.html', {'name': name})
    else:
        return render(request, 'name.html')
    

"""
def get_name(request):
    # if this is a POST request we need to process the form data
    
    return render(request, "name.html")
"""
