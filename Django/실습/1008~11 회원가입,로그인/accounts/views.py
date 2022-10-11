from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model
# from django.contrib.auth.forms import UserCreationForm
from .forms import CustomUserCreationForm

# Create your views here.
def signup(request):
    # POST 요청 처리
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
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