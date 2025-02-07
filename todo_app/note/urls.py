from django.urls import path
from note import views


urlpatterns = [
    path('', views.IndexPage.as_view(), name='index'),
    path('add_note/', views.AddNotePage.as_view(), name='add_note'),
]
