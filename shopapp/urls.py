from django.urls import path, include

from shopapp.views import product, by_category


app_name = 'shopapp'

urlpatterns = [
    path('', product, name='index'),
    path('<int:category_id>/', by_category, name='by_category'),
    path('basket/', include('basketapp.urls', namespace='basket')),
]
