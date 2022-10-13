from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm
from django.contrib.auth import get_user_model
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth import update_session_auth_hash
# from django.contrib.auth.forms import UserCreationForm
from .forms import CustomUserCreationForm, CustomUserChangeForm

# Create your views here.
def signup(request):
    # POST 요청 처리
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save() #ModelForm의 save 메서드의 리턴값은 해당 모델의 인스턴스다!
            # 회원가입 후 자동으로 로그인 
            auth_login(request, user) # 로그인 
            return redirect('movies:index')

    else:
        form = CustomUserCreationForm()
    context = {
        'form': form
    }
    return render(request, 'accounts/signup.html', context)

def profile(request, pk):
    # 유저정보를 받아오는 쿼리셋
    user = get_user_model().objects.get(pk=pk)
    context = {
        'user': user,
    }
    return render(request, 'accounts/profile.html', context)

def login(request):
    if request.method == 'POST':
        # AuthenticationForm은 ModelForm이 아님!
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            # 세션 저장
            # login 함수는 request, user 객체를 인자로 받음
            # user 객체는 어디? form에서 인증된 유저 정보를 받을 수 있다
            auth_login(request, form.get_user())
            # if request.GET.get('next'):
            return redirect(request.GET.get('next') or 'movies:index')
            # else:
            #     return redirect('movies:index')
    else:
        form = AuthenticationForm()
    context = {
        'form':form
    }
    return render(request, 'accounts/login.html', context)

def logout(request):
    auth_logout(request)
    return redirect('movies:index')

def update(request):
    if request.method == 'POST':
        form = CustomUserChangeForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('accounts:profile', request.user.pk)
    else:
        form = CustomUserChangeForm(instance=request.user)
    context = {
        'form': form,
    }
    return render(request, 'accounts/update.html', context)

def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            return redirect('movies:index')
    else:
        form = PasswordChangeForm(request.user)
    context = {
        'form':form,
    }
    return render(request, 'accounts/change_password.html', context)

def delete(request):
    request.user.delete()
    auth_logout(request)
    return redirect('movies:index')