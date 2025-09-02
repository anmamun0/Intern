from django.shortcuts import render
from django.http import (
            HttpResponse,
            HttpResponseBadRequest,
            HttpResponseGone,
            HttpResponseNotAllowed,
            HttpResponseRedirect,
            HttpResponseServerError,
            HttpResponseForbidden,
            HttpResponseNotFound,
                         )
# Create your views here.
def my_view(request):
    print(request.method)      # GET, POST
    print(request.path)        # /home/
    print(request.GET)         # Query parameters
    
    print(request.POST)        # Form data
    print(request.COOKIES)     # Cookies
    print(request.headers)     # HTTP headers
    return HttpResponse("Check console for request info")