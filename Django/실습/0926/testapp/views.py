from django.shortcuts import render
import random

# Create your views here.
def index(request, _number):
    if _number % 2 == 0:
        result = "짝수"
    if _number == 0:
        result = "0"
    else:
        result = "홀수"

    context = {"result": result, "number": _number}

    return render(request, "index.html", context)


def calculate(request, var1, var2):

    add = var1 + var2
    sub = var1 - var2
    mul = var1 * var2
    div = var1 // var2

    context = {
        "var1": var1,
        "var2": var2,
        "add": add,
        "sub": sub,
        "mul": mul,
        "div": div,
    }
    return render(request, "calculate.html", context)


def life(request):
    return render(request, "life.html")


def life_show(request):
    name = request.GET.get("name")
    animals = [
        "고양이",
        "강아지",
        "사자",
        "호랑이",
        "표범",
        "코뿔소",
        "하마",
        "악어",
        "곰",
        "소",
        "독수리",
        "닭",
        "메추라기",
        "두꺼비",
        "고라니",
        "당나귀",
    ]

    animal = random.choice(animals)

    context = {
        "name": name,
        "animal": animal,
    }

    return render(request, "life_show.html", context)


def lorem(request):
    return render(request, "lorem.html")


def lorem_show(request):
    cnt_para = int(request.GET.get("paragraphs"))
    cnt_words = int(request.GET.get("words"))

    lorems = [[] for _ in range(cnt_para)]
    ran_words = [
        "바나나",
        "짜장면",
        "사과",
        "바나나",
        "딸기",
    ]

    for i in range(len(lorems)):
        while len(lorems[i]) < cnt_words:
            word = random.choice(ran_words)
            lorems[i].append(word)

    context = {"lorems": lorems}
    return render(request, "lorem_show.html", context)
