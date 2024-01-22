
from django.shortcuts import render
from PIL import Image, ImageFont, ImageDraw


def home(request):
    return render(request, 'home.html')  
