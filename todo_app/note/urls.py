from django.urls import path
from note import views


urlpatterns = [
    path('', views.index, name='index'),
]
