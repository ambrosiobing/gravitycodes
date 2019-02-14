from django.shortcuts import render
from django.http import HttpRequest, HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt

# Create your views here.

@csrf_exempt
def home(request):
    """Renders the home page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'gravcode/index.html',
        {
            'title':'',
            'message':'',
        }
    )

@csrf_exempt
def about(request):
    """Renders the about page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'gravcode/about.html',
    )

@csrf_exempt
def team(request):
    """Renders the team page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'gravcode/team.html',
    )

@csrf_exempt
def services(request):
    """Renders the services page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'gravcode/services.html',
    )

@csrf_exempt
def contact(request):
    """Renders the contact page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'gravcode/contact.html',
    )
