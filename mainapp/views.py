from django.shortcuts import render

from .forms import PictureForm


def index(request):
    return render(request, 'mainapp/index.html')

def gallery(request):
    return render(request, 'mainapp/gallery.html')


def upload_to_gallery(request):
    title = 'Upload page'
    image_form = PictureForm()

    content = {'title': title, 'image_form': image_form}
    if request.method == 'POST':
        form = PictureForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            img_obj = form.instance
            content = {'title': title, 'img_obj': img_obj}
            return  render(request, 'mainapp/upload_to_gallery.html', content)

    return render(request, 'mainapp/upload_to_gallery.html', content)

