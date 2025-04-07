from django.shortcuts import render
from rest_framework.generics import CreateAPIView, ListAPIView
# Create your views here.

class SendForm(CreateAPIView):
    pass

class GetForm(ListAPIView):
    pass
