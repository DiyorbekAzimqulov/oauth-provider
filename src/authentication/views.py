from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import login
from django.contrib.auth import get_user_model


from .utils import get_token_from_code, get_keycloak_user_info, generate_random_string
# Create your views here.

def auth_keycloak_callback(request):
    data = request.GET
    code = data.get('code')
    token = get_token_from_code(code)
    user_info = get_keycloak_user_info(token['access_token'])
    first_name = user_info.get('given_name', '')
    last_name = user_info.get('family_name', '')
    email = user_info.get('email', '')
    username = user_info.get('preferred_username', '')
    user = get_user_model().objects.filter(username=username).first()
    if not user:
        user = get_user_model().objects.create_user(
            username=username,
            email=email,
            first_name=first_name,
            last_name=last_name,
            password=generate_random_string()
        )
    login(request, user)

    print("auth_keycloak_callback", request.GET)
    return HttpResponse('Hello, you are logged in!')
