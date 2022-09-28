from django.shortcuts import render

from pjt0926.settings import BASE_DIR

# Create your views here.
def index(request):

    return render(request, "practices/index.html")


def ping(request):

    return render(request, "practices/ping.html")


def pong(request):
    # 방법 1
    # name = request.GET.get('ball')
    # context = {
    #     'name': name,
    # }

    # return render(request, "pong.html", context)

    # return 값에 바로 넣는 방법
    return render(request, "practices/pong.html", {"name": request.GET.get("ball")})
