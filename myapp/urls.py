from django.urls import path
from .views import create_image_text, output_frame

urlpatterns = [
    path('create/', create_image_text, name='create_image_text'),
    path('output/<int:pk>/', output_frame, name='output_frame'),
]
