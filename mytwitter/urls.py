from django.urls import path
from .import views

urlpatterns = [
    path("", views.get_all_twitter, name='get_list_of_twitter'),
    path('<int:id>/edit_twitter/', views.edit_twitter, name='edit_twitter'),
    path('<int:id>/delete_twitter/', views.delete_twitter, name='delete_twitter'),  # Fixed typo
    path('create_at/', views.add_twitter, name='create_twitter'),
    path('register/', views.register, name='register'),
]
