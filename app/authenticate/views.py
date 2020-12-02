from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout

from .forms import NameForm

def home(request):
    return render(request,'authenticate/home.html', {})

def login_user(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('thanks')
            # Redirect to a success page.
            ...
        else:
            return redirect('login')
    # Return an 'invalid login' error message.
    else:
        return render(request, 'authenticate/login.html', {})

def get_name(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = NameForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return HttpResponseRedirect('/thanks/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = NameForm()

    return render(request, 'authenticate/name.html', {'form': form})

def thanks(request):
    return render(request,'authenticate/thanks.html', {})




