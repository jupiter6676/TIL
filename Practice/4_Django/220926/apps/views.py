from multiprocessing import context
from django.shortcuts import render
import random

# Create your views here.
def index(request):
    return render(request, "index.html")


# 홀짝
def is_odd_even(request, number):
    res = "홀수" if number % 2 == 1 else "짝수"

    context = {
        "number": number,
        "result": res,
    }

    return render(request, "is_odd_even.html", context)


# 사칙연산
def calculate(request, num1, num2):
    add = num1 + num2
    sub = num1 - num2
    mul = num1 * num2
    div = num1 // num2

    context = {
        "num1": num1,
        "num2": num2,
        "add": add,
        "sub": sub,
        "mul": mul,
        "div": div,
    }

    return render(request, "calculate.html", context)


# 전생
def past_life(request):
    return render(request, "past_life.html")


def past_life_result(request):
    job = random.choice(["황제", "귀족", "평민", "말", "돼지", "돌"])
    name = request.GET.get("user-name")

    context = {
        "job": job,
        "name": name,
    }

    return render(request, "past_life_result.html", context)


def lorem(request):
    return render(request, "lorem.html")


def lorem_result(request):
    num_para = int(request.GET.get("para"))
    num_word = int(request.GET.get("word"))

    words = ["오이", "당근", "양파", "감자", "토마토", "김치"]
    paras = list()

    for _ in range(num_para):
        paras.append(random.choices(words, k=num_word))

    context = {
        "paras": paras,
    }

    print(paras)

    return render(request, "lorem_result.html", context)
