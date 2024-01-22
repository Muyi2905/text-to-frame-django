
from django.urls import path
from .views import frame_image

urlpatterns = [
    path('frame/', frame_image, name='frame_image'),
    # Add other URL patterns as needed
]
