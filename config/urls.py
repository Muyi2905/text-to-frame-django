from django.contrib import admin
from django.urls import path, include
from myapp import frame_image

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('myapp.urls')),
    path('', frame_image, name='frame_image'),  # Include only if not in myapp.urls
]
