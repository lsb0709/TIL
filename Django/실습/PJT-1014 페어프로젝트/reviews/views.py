from django.shortcuts import render, redirect
from .forms import ReviewForm
from .models import Review
from django.contrib.auth.decorators import login_required


@login_required
def create(request):
    if request.method == "POST":
        review_form = ReviewForm(request.POST)
        if review_form.is_valid():
            review_form.save()
            return redirect("reviews:index")
    else:
        review_form = ReviewForm()
    context = {
        "review_form": review_form,
    }

    return render(request, "reviews/create.html", context)


def index(request):
    reviews = Review.objects.order_by("-pk")
    context = {
        "reviews": reviews,
    }
    return render(request, "reviews/index.html", context)


def detail(request, review_pk):
    review = Review.objects.get(pk=review_pk)

    context = {
        "review": review,
    }
    return render(request, "reviews/detail.html", context)


@login_required
def update(request, pk):
    review = Review.objects.get(pk=pk)
    if request.method == "POST":
        review_form = ReviewForm(request.POST, instance=review)
        if review_form.is_valid():
            review_form.save()
            return redirect("reviews:detail", review.pk)
    else:
        review_form = ReviewForm(instance=review)
    context = {
        "review_form": review_form,
    }

    return render(request, "reviews/update.html", context)


@login_required
def delete(request, pk):
    Review.objects.get(pk=pk).delete()
    return redirect("reviews:index")
