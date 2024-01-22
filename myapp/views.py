# views.py
from django.shortcuts import render
from .forms import ImageFramingForm
from PIL import Image, ImageDraw, ImageFont
from django.conf import settings
import os

def frame_image(request):
    if request.method == 'POST':
        form = ImageFramingForm(request.POST, request.FILES)
        if form.is_valid():
            image = form.cleaned_data['image']
            text = form.cleaned_data['text']

            # Process the image and add text
            framed_image = process_image(image, text)

            # Save the framed image to a temporary location
            temp_image_path = os.path.join(settings.MEDIA_ROOT, 'temp_framed_image.png')
            framed_image.save(temp_image_path)

            # Pass the temporary image path to the template
            return render(request, 'your_template.html', {'framed_image_url': temp_image_path})
    else:
        form = ImageFramingForm()

    return render(request, 'your_template.html', {'form': form})

def process_image(image, text):
    # Open the image using PIL
    img = Image.open(image)

    # Add text to the image
    draw = ImageDraw.Draw(img)
    font = ImageFont.load_default()  # You can customize the font and size
    draw.text((10, 10), text, font=font, fill=(255, 255, 255))  # Adjust the position as needed

    return img
