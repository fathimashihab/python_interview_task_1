from django.urls import path
from . import views

urlpatterns = [
    path('images/', views.image_list, name='image_list'),
    path('upload/', views.upload_image, name='upload_image'),
]