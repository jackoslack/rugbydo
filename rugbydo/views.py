# pages/views.py
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.shortcuts import render

from .forms import NameForm

def show_settings(request):
    
    from django.conf import settings

    bdir = settings.BASE_DIR
    static = settings.STATIC_URL
    auto_field = settings.DEFAULT_AUTO_FIELD

    return render(request, 'bdir.html', {'static': static})

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
