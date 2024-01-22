# views.py
from django.shortcuts import render
from django.conf import settings
from PIL import Image, ImageDraw, ImageFont
import os

# def home(request):
#     return render(request, 'home.html') 

def home(request):
    if request.method == 'POST':
        # Process the form data
        image_file = request.FILES.get('image')
        text = request.POST.get('text')
