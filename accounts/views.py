from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import AuthenticationForm
from .forms import CustomLoginForm ,CustomUserCreationForm, CustomUserChangeForm
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth import get_user_model

# Create your views here.
def people(request, user_id) :
    people = get_object_or_404(get_user_model(),id=user_id)
    content = {
        'people' : people,
    }
    return render(request, 'accounts/people.html', content)

def login(request) :
    if request.method == 'POST' :
        form = CustomLoginForm(request, request.POST)
        if form.is_valid() :
            auth_login(request, form.get_user())
            # login_required에 의해 들어온 로그인 처리
            return redirect(request.GET.get('next') or 'notes:list')
    
    form = CustomLoginForm()
    content = {
        'form' : form,
    }
    return render(request, 'accounts/login.html', content)
    
def logout(request) :
    auth_logout(request)
    return redirect('notes:list')

def signup(request) :
    if request.method == 'POST' :
        form = CustomUserCreationForm(request.POST)
        if form.is_valid() :
            form.save()
            # 회원가입 완료시, 자동로그인
            auth_login(request, form.instance)
            return redirect('notes:list')
    form = CustomUserCreationForm()
    content = {
        'form' : form,
    }
    return render(request, 'accounts/signup.html', content)    

def update(request) :
    if request.method == 'POST' :
        form = CustomUserChangeForm(request.POST, instance=request.user)
        if form.is_valid() :
            user = form.save()
            return redirect('accounts:people', user.id)            
    form = CustomUserChangeForm()
    content = {
        'form' : form,
    }
    return render(request, 'accounts/update.html', content)
    
