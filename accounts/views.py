from django.shortcuts import render

# Create your views here.
def people(request, user_id) :
    return render(request, 'accounts/people.html')

def login(request) :
    return render(request, 'accounts/login.html')
    
def logout(request) :
    pass

def signup(request) :
    return render(request, 'accounts/signup.html')    

def update(request) :
    return render(request, 'accounts/update.html')
    
