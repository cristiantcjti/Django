from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views import View
from .forms import ReviewForm

# Create your views here.


class ReviewView(View):
    #When we use class, django already knows which method call based on the request.
    def get(self, request):
        form = ReviewForm()

        return render(request, "reviews/reviews.html", {
            "form": form
        })

    def post(self, request):
        form = ReviewForm(request.POST)

        if form.is_valid():
            form.save
            return HttpResponseRedirect("/thank-you")

        return render(request, "reviews/reviews.html", {
            "form": form
        })


def thank_you(request):
    return render(request, "reviews/thank_you.html")

"""
#Using functions

def review(request):
    if request.method == "POST":
        # To create an update
        #        existing_data = Review.objects.get(pk=)
        #        form = ReviewForm(request.POST, instance=existing_data)
        form = ReviewForm(request.POST)

        if form.is_valid():
            # To valid and save when we create the form with Modelform
            form.save
            return HttpResponseRedirect("/thank-you")
# To valid and save when we creat the form without Modelform
#            review = Review(
#                user_name=form.cleaned_data['user_name'],
#                review_text=form.cleaned_data['review_text'],
#                rating=form.cleaned_data['rating'])
#            review.save()
#            return HttpResponseRedirect("/thank-you")

    else:
        form = ReviewForm()

    return render(request, "reviews/reviews.html", {
        "form": form
    })
"""


