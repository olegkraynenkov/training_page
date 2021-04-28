from django.urls import path

from authapp.views import auth


app_name = 'authapp'

urlpatterns = [
    path('', auth, name='login'),
]
