from django.shortcuts import render, redirect
from .forms import ImageTextForm

def create_image_text(request):
    if request.method == 'POST':
        form = ImageTextForm(request.POST, request.FILES)
        if form.is_valid():
            image_text = form.save()
            return redirect('output_frame', pk=image_text.pk)
    else:
        form = ImageTextForm()

    return render(request, 'imagetext/create_image_text.html', {'form': form})

def output_frame(request, pk):
    image_text = ImageText.objects.get(pk=pk)
    return render(request, 'imagetext/output_frame.html', {'image_text': image_text})
