from django.shortcuts import render, redirect

# view to return home page
def home_page (request) :

    return render(request, "landingPage/index.html")