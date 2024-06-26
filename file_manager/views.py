from django.shortcuts import render, redirect

from django.contrib.auth.decorators import login_required

from django.contrib.auth import logout

import os
from dotenv import load_dotenv
load_dotenv() 

# view to return home page
def home_page (request) :
    print(os.getenv('PASS_EMAIL_SENDER'))
    return render(request, "landingPage/landingPageIndex.html")


@login_required(login_url="/")
def logoutPage (request) : 
    logout(request)

    return redirect("/")