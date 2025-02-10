from django.urls import path

from note import views

urlpatterns = [
    path('', views.IndexPage.as_view(), name='index'),
    path('trash/', views.TrashNotePage.as_view(), name='trash'),
    path('add_note/', views.AddNotePage.as_view(), name='add_note'),
    path('change_note/<int:pk>/', views.UpdateNotePage.as_view(), name='change_note'),
    path('delete_note/<int:pk>/', views.DeleteNotePage.as_view(), name='delete_note'),
    path('category/', views.CategoryPage.as_view(), name='category'),
    path('category/add/', views.AddCategoryPage.as_view(), name='add_category'),
    path('category/<slug:slug>/', views.UpdateCategoryPage.as_view(), name='category_slug'),
    path('category/delete/<slug:slug>/', views.DeleteCategoryPage.as_view(), name='delete_category'),
]
