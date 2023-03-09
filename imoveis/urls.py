from django.contrib import admin
from django.urls import path
import include
from imoveis.views import ImoveisView

urlpatterns = [
    path('', ImoveisView.as_view(), name='imoveis'),

]