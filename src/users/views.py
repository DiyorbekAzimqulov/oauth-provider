from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from oauth2_provider.views.generic import ProtectedResourceView
from django.http import HttpResponse

# Create your views here.

class ApiEndpoint(ProtectedResourceView):
    def get(self, request, *args, **kwargs):
        return HttpResponse('Hello, OAuth2!')

def index(request):
    return render(request, 'index.html')

@login_required
def protected(request):
    return render(request, 'protected.html')