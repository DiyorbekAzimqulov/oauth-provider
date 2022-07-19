from django.urls import path

from .views import auth_keycloak_callback

urlpatterns = [
    path('callback', auth_keycloak_callback, name='auth_keycloak_callback'),
]