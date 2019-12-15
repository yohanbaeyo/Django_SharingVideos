from django.shortcuts import render, redirect
from .models import *

# Create your views here.
def index(request):
    qs = Video.objects.all()
    q = request.GET.get("q")
    if q:
        qs = qs.filter(title__icontains=q)
    return render(request, 'main/index.html', {'videoList': qs})
