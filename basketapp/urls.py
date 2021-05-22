from django.urls import path

from .views import basket


app_name = 'basketapp'

urlpatterns = [
    path('', basket, name='index'),
]
