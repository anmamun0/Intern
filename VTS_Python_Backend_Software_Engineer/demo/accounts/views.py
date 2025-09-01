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
    return HttpResponse(f"hello this is test")