# pages/views.py
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.shortcuts import render

from .forms import NameForm

def show_settings(request):
    
    from django.conf import settings
    my_settings = []
    for set in settings:
        my_settings.append(set)

    #bdir = settings.BASE_DIR
    bdir = my_settings

    return render(request, 'bdir.html', {'bdir': bdir})

def home_page_view(request):

    return HttpResponse("Hello, Freddo!")

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
