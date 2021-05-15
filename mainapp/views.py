from django.shortcuts import render
from .models import Picture

from .forms import PictureForm


def index(request):
    return render(request, 'mainapp/index.html')

def gallery(request):
    picture = Picture.objects.all()
    content = {'picture': picture}
    return render(request, 'mainapp/gallery.html', content)


def upload_to_gallery(request):

    if request.method == 'POST':
        form = PictureForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            img_obj = form.instance
            return  render(request, 'mainapp/upload_to_gallery.html', {'form': form, 'img_obj': img_obj})
    else:
        form = PictureForm()
    return render(request, 'mainapp/upload_to_gallery.html', {'form': form})

