from lib2to3.pgen2 import token
import random
import string

from django.conf import settings

from keycloak import KeycloakOpenID

KEYCLOAK_SERVER = settings.KEYCLOAK_SERVER
KEYCLOAK_CLIENT_ID = settings.KEYCLOAK_CLIENT_ID
KEYCLOAK_CLIENT_SECRET = settings.KEYCLOAK_CLIENT_SECRET
KEYCLOAK_REALM = settings.KEYCLOAK_REALM
KEYCLOAK_REDIRECT_URI = settings.KEYCLOAK_REDIRECT_URI

keycloak_openid = KeycloakOpenID(server_url=KEYCLOAK_SERVER,
                    client_id=KEYCLOAK_CLIENT_ID,
                    realm_name=KEYCLOAK_REALM,
                    client_secret_key=KEYCLOAK_CLIENT_SECRET)


def generate_keycloak_auth_url():
    auth_url = keycloak_openid.auth_url(
        redirect_uri=KEYCLOAK_REDIRECT_URI,
        scope="email",
        state="your_state_info")
    return auth_url


def get_token_from_code(code):
    token = keycloak_openid.token(
        grant_type='authorization_code',
        code=code,
        redirect_uri=KEYCLOAK_REDIRECT_URI)
    return token


def get_keycloak_user_info(token):
    """
    token: string (access token)

    Get user info from keycloak
    """
    user_info = keycloak_openid.userinfo(token)
    return user_info


def generate_random_string():
    return ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(10))
