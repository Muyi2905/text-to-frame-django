
from django.contrib import admin
from django.urls import path, include
from .views import frame_image



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('myapp.urls')),
     path('frame/', frame_image, name='frame_image'),
  
    
]


