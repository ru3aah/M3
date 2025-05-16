from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from models import MyModel


def show_models(request: HttpRequest) -> HttpResponse:
    all_models = MyModel.objects.all()
    return render(request, 'myapp/index.html')

# Create your views here.
