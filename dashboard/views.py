from django.shortcuts import render, redirect

# view to homepage to dashboard
def home_dashboard (request) :
    if request.user.is_authenticated : # if user is logged

        # render home page
        return render (request, "dashboard/index.html")
    else : # if user is not logged
        
        # redirect to login page
        return redirect ("user/login")