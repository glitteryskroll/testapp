from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request, 'testapp/test.html', {'name':request.GET['name'], 'message':request.GET['message']})
