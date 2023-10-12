# pages/views.py
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.shortcuts import render

from .forms import NameForm

def show_settings(request):
    from django.conf import settings
    bdir = settings.BASE_DIR
    return HttpResponse(bdir)

def home_page_view(request):

    return HttpResponse("Hello, Freddo!")


def get_name(request):
    # if this is a POST request we need to process the form data
    """
    if request.method == "POST":
        # create a form instance and populate it with data from the request:
        form = NameForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return HttpResponseRedirect("/thanks/")

    # if a GET (or any other method) we'll create a blank form
    else:
        form = NameForm()
"""
    form = NameForm()
    return render(request, "name.html", {"form": form})
