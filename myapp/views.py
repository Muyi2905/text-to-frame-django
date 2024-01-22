# views.py
from django.shortcuts import render
from django.conf import settings
from PIL import Image, ImageDraw, ImageFont
import os

def home(request):
    return render(request, 'home.html') 

def home(request):
    if request.method == 'POST':
        # Process the form data
        image_file = request.FILES.get('image')
        text = request.POST.get('text')

        framed_image_path = os.path.join(settings.MEDIA_ROOT, 'framed_images', 'framed_image.jpg')
        framed_image.save(framed_image_path)
        
        framed_image_url = os.path.join(settings.MEDIA_URL, 'framed_images', 'framed_image.jpg')
        return render(request, 'myapp/home.html', {'framed_image_url': framed_image_url})