from django.shortcuts import render, redirect

# view to return home page
def home_page (request) :
    # if user is not logged
    if request.user.is_authenticated == False :
        pass

    return render(request, "landingPage/landingPage.html")