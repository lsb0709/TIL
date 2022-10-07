from email import contentmanager
from django.shortcuts import render, redirect
from .models import Movie

# main page 이동 메소드
def index(reqeust):
    movies = Movie.objects.order_by("-hearted", "-created_at")
    context = {
        "movies": movies,
    }
    return render(reqeust, "review/index.html", context)


def new(reqeust):
    return render(reqeust, "review/new.html")


# detail.html로 이동 메소드
def detail(request, pk_):
    # 여기서 객체를 생성 => context
    target = Movie.objects.get(id=pk_)

    context = {"target": target}

    return render(request, "review/detail.html", context)


# 생성 메소드
def create(reqeust):
    obj = reqeust.GET
    Movie.objects.create(
        title=obj.get("title"),
        content=obj.get("content"),
        created_at=obj.get("created_at"),
        updated_at=obj.get("updated_at"),
    )
    return redirect("movieapp:index")


# 삭제 메소드
def delete(request, pk_):
    target = Movie.objects.get(id=pk_)
    target.delete()

    return redirect("movieapp:index")


# 업데이트 관련 메소드
def update(request, pk_):
    target = Movie.objects.get(id=pk_)
    # 내용 채울 예정
    target.title = request.POST.get("title")
    target.content = request.POST.get("content")
    target.save()
    return redirect("movieapp:index")


def edit(request, pk_):
    target = Movie.objects.get(id=pk_)
    context = {
        "target": target,
    }
    return render(request, "review/edit.html", context)


def heart(request, pk_):
    target = Movie.objects.get(id=pk_)

    if target.hearted:
        target.hearted = False
    else:
        target.hearted = True

    target.save()
    return redirect("movieapp:index")
