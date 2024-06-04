from django.shortcuts import render

# view to return home page
def home_page (request) :

    # return home page
    return render(request, "landingPage.html")