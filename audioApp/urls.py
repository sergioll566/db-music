from django.contrib import admin
from django.urls import path,include
from . import views
from . api_views import AudioView
urlpatterns = [
    path('', views.homepage,name='home_audio'),
    path('registrar/', views.registrar,name='registrar'),
    path("audios/",AudioView.as_view(),name='audios'),

]
