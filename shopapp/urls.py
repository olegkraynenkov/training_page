from django.urls import path

from shopapp.views import product


app_name = 'shopapp'

urlpatterns = [
    path('', product, name='index'),
]
