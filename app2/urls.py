from django.urls import path
from app2.views import *
app_name='sai'
urlpatterns=[
    path('eswar/',eswar,name='eswar'),
]