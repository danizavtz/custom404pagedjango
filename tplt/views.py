from django.shortcuts import render
from django.http import HttpResponseNotFound
from django.http import HttpResponse
import datetime


def default(request):
    now = datetime.datetime.now()
    html = "<html><body>It is now %s.</body></html>" % now
    return HttpResponse(html)

# Create your views here.
def custom_404_view(request, exception=None):
    return HttpResponseNotFound("<h1>!Page not found!</h1>")