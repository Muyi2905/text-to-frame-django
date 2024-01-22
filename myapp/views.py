# views.py
from django.shortcuts import render
from django.conf import settings
from PIL import Image, ImageDraw, ImageFont
import os

def home(request):
    # framed_image_url = None 
    
    if request.method == 'POST':


        image_file = request.FILES.get('image')
        text = request.POST.get('text')

        # Generate the framed image
        framed_image = generate_framed_image(image_file, text)

        # Save the framed image
        framed_image_path = os.path.join(settings.MEDIA_ROOT, 'framed_images', 'framed_image.jpg')
        framed_image.save(framed_image_path)

        # Pass the framed image URL to the template
        framed_image_url = os.path.join(settings.MEDIA_URL, 'framed_images', 'framed_image.jpg')

    return render(request, 'home.html', {'framed_image_url': framed_image_url})

def generate_framed_image(image_file, text):
    # Open the uploaded image using Pillow
    image = Image.open(image_file)

    # # Create a drawing object
    # draw = ImageDraw.Draw(image)

    # # Set font and size (you might need to adjust the font path)
    # font_path = os.path.join(settings.BASE_DIR, 'path_to_your_font.ttf')
    # font_size = 30
    # font = ImageFont.truetype(font_path, font_size)

    # # Get image dimensions
    # image_width, image_height = image.size

    # # Calculate text position (centered)
    # text_width, text_height = draw.textsize(text, font)
    # text_position = ((image_width - text_width) // 2, (image_height - text_height) // 2)

    # # Draw the text on the image
    # draw.text(text_position, text, font=font, fill='white')

    # return image
