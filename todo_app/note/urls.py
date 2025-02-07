from django.urls import path
from note import views


urlpatterns = [
    path('', views.IndexPage.as_view(), name='index'),
]
