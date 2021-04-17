from django.urls import path

from shopapp.views import product, by_category


app_name = 'shopapp'

urlpatterns = [
    path('', product, name='index'),
    path('<int:category_id>/', by_category),
]
