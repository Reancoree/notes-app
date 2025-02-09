from django.urls import path

from user import views

app_name = 'user'

urlpatterns = [
    path('profile/', views.profile_view, name='profile'),
    path('accounts/regiser/', views.RegisterView.as_view(), name='register')
]
