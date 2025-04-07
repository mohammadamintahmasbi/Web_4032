from django.shortcuts import render
from rest_framework.generics import CreateAPIView, ListAPIView
from rest_framework.permissions import AllowAny

from .serializers import FormSerializer
from .models import Form
class SendForm(CreateAPIView):
    queryset = Form.objects.all()
    serializer_class = FormSerializer
    permission_classes = [AllowAny]
class GetForm(ListAPIView):
    queryset = Form.objects.all()
    serializer_class = FormSerializer
    permission_classes = [AllowAny]