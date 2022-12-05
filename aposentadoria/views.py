from django.shortcuts import render, redirect
from rest_framework import viewsets
from aposentadoria.models import *
from aposentadoria.serializer import *
# Create your views here.
class TrabalhoViewSet(viewsets.ModelViewSet):
    queryset = Trabalho.objects.all()
    serializer_class = TrabalhoSerializer



def index(request):
        
    return render(request, 'index.html')