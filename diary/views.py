from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from .models import Diary, DiaryFile


# ================= AUTH =================

def login_view(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('diary_home')
        else:
            messages.error(request, "Invalid username or password")

    return render(request, 'diary/login.html')


def register_view(request):
    if request.method == "POST":
        username = request.POST.get('username')
        email = request.POST.get('email')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')

        if password1 != password2:
            messages.error(request, "Passwords do not match")
            return redirect('register')

        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already exists")
            return redirect('register')

        if User.objects.filter(email=email).exists():
            messages.error(request, "Email already exists")
            return redirect('register')

        User.objects.create_user(
            username=username,
            email=email,
            password=password1
        )
        messages.success(request, "Account created successfully. Please login.")
        return redirect('login')

    return render(request, 'diary/register.html')


def forgot_password_view(request):
    if request.method == "POST":
               return redirect('login')

    return render(request, 'diary/forgot_password.html')


def logout_view(request):
    logout(request)
    return redirect('login')


# ================= DIARY =================

@login_required
def diary_home(request):
    diaries = Diary.objects.filter(user=request.user).order_by('-created_at')
    return render(request, 'diary/diary_home.html', {'diaries': diaries})


@login_required
def diary_create(request):
    if request.method == "POST":
        title = request.POST.get('title')
        content = request.POST.get('content')
        files = request.FILES.getlist('files')

        diary = Diary.objects.create(
            user=request.user,
            title=title,
            content=content
        )

        for f in files:
            DiaryFile.objects.create(diary=diary, file=f)

        return redirect('diary_home')

    return render(request, 'diary/diary_create.html')


@login_required
def diary_detail(request, diary_id):
    diary = get_object_or_404(Diary, id=diary_id, user=request.user)
    return render(request, 'diary/diary_detail.html', {'diary': diary})


@login_required
def diary_edit(request, diary_id):
    diary = get_object_or_404(Diary, id=diary_id, user=request.user)

    if request.method == "POST":
        diary.title = request.POST.get('title')
        diary.content = request.POST.get('content')
        diary.save()
        return redirect('diary_home')

    return render(request, 'diary/diary_create.html', {'diary': diary})


@login_required
def diary_delete(request, diary_id):
    diary = get_object_or_404(Diary, id=diary_id, user=request.user)
    diary.delete()
    return redirect('diary_home')
