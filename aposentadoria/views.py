from django.shortcuts import render
from rest_framework import viewsets
from aposentadoria.models import *
from aposentadoria.serializer import *
# Create your views here.
class TrabalhoViewSet(viewsets.ModelViewSet):
    queryset = Trabalho.objects.all()
    serializer_class = TrabalhoSerializer
