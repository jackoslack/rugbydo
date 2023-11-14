# pages/views.py
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.shortcuts import render

from .forms import NameForm

def show_settings(request):
    
    from django.conf import settings

    try:
        bdir = settings.BASE_DIR
    except:
        bdir = "Error"

    try:
        static_url = settings.STATIC_URL
    except:
        static_url = "Error"

    #try:
    #    static_root = settings.STATIC_ROOT
    #except:
    #    static_root = "Error"

    try:
        static_files_directory = settings.STATICFILES_DIRS
    except:
        static_files_directory = "Error"

    try:
        project_root = settings.PROJECT_ROOT
    except:
        project_root = "Error"

    return render(request, 'bdir.html', 
                  {'static_url': static_url}, 
                  {'static_files_directory': static_files_directory}, 
                  {'project_root': project_root},
                  {'bdir': bdir},
        )

def home_page_view(request):

    
    return render(request, 'home.html')

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
