from django.urls import path

from mainapp.views import gallery, upload_to_gallery


app_name = 'mainapp'

urlpatterns = [
    path('', gallery, name='index'),
    path('upload/', upload_to_gallery, name='upload_to_gallery')
]
