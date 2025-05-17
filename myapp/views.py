from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from .models import MyModel

# Create your views here.
def show_models(request: HttpRequest) -> HttpResponse:
    all_models = MyModel.objects.all()
    context = {'models': all_models, 'title': 'My Models'}
    return render(request, 'index.html', context)
