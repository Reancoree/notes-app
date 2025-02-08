from django.urls import path
from note import views

urlpatterns = [
    path('', views.IndexPage.as_view(), name='index'),
    path('trash/', views.TrashNotePage.as_view(), name='trash'),
    path('add_note/', views.AddNotePage.as_view(), name='add_note'),
    path('change_note/<int:pk>', views.UpdateNotePage.as_view(), name='change_note'),
    path('delete_note/<int:pk>', views.DeleteNotePage.as_view(), name='delete_note'),

]
