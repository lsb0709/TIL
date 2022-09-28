from django.shortcuts import render
from pjt0926.settings import BASE_DIR
from .models import Article

guestbook = []

# Create your views here.
def index(request):
    # DB에서 가져오기
    guestbook = Article.objects.all()

    return render(request, "articles/index.html", {"guestbook": guestbook})


def create(request):
    content = request.GET.get("content")
    # gueskbook.append(content)
    # DB에 저장
    Article.objects.create(content=content)

    return render(request, "articles/create.html", {"content": content})
