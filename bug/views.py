from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("Welcome to Bug Application! This is built for the WikiMedia Outreachy Contribution by Oyindamola Olatunji.")

