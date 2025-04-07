from django.urls import path
from .views import SendForm, GetForm

urlpatterns = [
    path(r'send', SendForm.as_view(), name='send-form'),
    path(r'get', GetForm.as_view(), name='get-form')
]
