from django.shortcuts import render
from rest_framework.generics import ListAPIView,ListCreateAPIView,RetrieveAPIView,RetrieveUpdateAPIView,RetrieveUpdateDestroyAPIView

from rest_framework.generics import ListAPIView
from .serializers import  CryptoSerializer
from .models import Crypto
class CryptoListView(ListCreateAPIView):
    queryset=Crypto.objects.all()
    serializer_class=CryptoSerializer

class CryptoDetailView(RetrieveUpdateDestroyAPIView):
    queryset=Crypto.objects.all()
    serializer_class=CryptoSerializer