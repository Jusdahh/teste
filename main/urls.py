from django.contrib import admin
from django.urls import path
import include
from main.views import HomeView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),

]


