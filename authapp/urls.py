from django.urls import path

from authapp.views import login


app_name = 'authapp'

urlpatterns = [
    path('', login, name='login'),
]
