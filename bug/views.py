from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("Welcome to Bug Application! This is built for the Wikimedia Outreachy Contribution by Oyindamola Olatunji.")

