from django.shortcuts import render

def login_view (request) :
    return render (request, "users/loginPage.html")

def register_view (request) :
    

    return render (request, "users/registerPage.html")