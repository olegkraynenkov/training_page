from django.urls import path

from mainapp.views import gallery


app_name = 'mainapp'

urlpatterns = [
    path('', gallery, name='index'),
]
