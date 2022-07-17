from django.urls import path

from .views import index, protected


app_name = 'users'
urlpatterns = [
    path('', index, name='index'),
    path('protected/', protected, name='protected'),
]