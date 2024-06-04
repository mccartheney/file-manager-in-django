from django.shortcuts import render
from users import forms

def home_page (request) :
    return render(request, "landingPage.html")