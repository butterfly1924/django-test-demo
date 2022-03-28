from django.http import HttpResponse


def home(request):
    """View function for home page"""
    return HttpResponse('Home page for github action+argocd demo')