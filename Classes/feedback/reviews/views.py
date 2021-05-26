from django.http import HttpResponseRedirect, request
from django.shortcuts import render
from django.views import View
from django.views.generic.base import TemplateView
from django.views.generic import ListView, DetailView
from django.views.generic.edit import FormView, CreateView
from .forms import ReviewForm
from .models import Review
from reviews import forms



# Create your views here.


# Using CreateView class to fetch and save a form
class ReviewView(CreateView):
    model = Review
    template_name = "reviews/review.html"
    form_class = ReviewForm
    success_url = "/thank-you"

# Using FormView class to fetch and save a form
#class ReviewView(FormView):
#    form_class = ReviewForm
#    template_name = "reviews/review.html"
#    success_url = "/thank-you"

#    def form_valid(self, form):
#        form.save()
#        return super().form_valid(form)

# Using View class to fetch and save a form
#class ReviewView(View):
    #When we use class, django already knows which method call based on the request.
#    def get(self, request):
#        form = ReviewForm()

#        return render(request, "reviews/review.html", {
#            "form": form
#        })

#    def post(self, request):
#        form = ReviewForm(request.POST)

#        if form.is_valid():
#            form.save()
#            return HttpResponseRedirect("/thank-you")

#        return render(request, "reviews/review.html", {
#            "form": form
#        })

#########################################
# Using a more specific class, TemplateView
class ThankyouView(TemplateView):
    template_name = "reviews/thank_you.html"

    def get_context_data(self, **kwargs):  
        context = super().get_context_data(**kwargs)
        context["message"] = "This works"
        return context
    
# Using View heritage
#class ThankyouView(View):
#    def get(self, request):
#        return render(request, "reviews/thank_you.html")    

#########################################
class ReviewListView(ListView):
    template_name = "reviews/review_list.html"
    model=Review
    # The rendered name to use in the template is object_list, but we can replace it.
    context_object_name = "reviews"

    # If we need to filter the fetch result.
    #def get_queryset(self):
    #    base_query = super().get_queryset()
    #    data = base_query.filter(rating__gt=5)
    #    return data

# Using TemplateView to fetch a list
#class ReviewListView(TemplateView):
#    template_name = "reviews/review_list.html"

#    def get_context_data(self, **kwargs):
#        context = super().get_context_data(**kwargs)
#        reviews = Review.objects.all()
#        context["reviews"] = reviews
#        return context

#########################################

class SingleReviewView(DetailView):
    template_name = "reviews/single_review.html"
    model = Review 

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        loaded_review = self.object
        request = self.request
        favorite_id = request.session.get("favorite_review")
        context["is_favorite"] = favorite_id == str(loaded_review.id)
        return context

# Using TemplateView to fetch a detailed
#class SingleReviewView(TemplateView):
#    template_name = "reviews/single_review.html"

#    def get_context_data(self, **kwargs):
#        context = super().get_context_data(**kwargs)
#        review_id = kwargs["id"]
#        select_review = Review.objects.get(pk=review_id)
#        context["review"] = select_review
#        return context    

#########################################

class AddFavoriteView(View):
    def post(self, request):
        review_id = request.POST["review_id"]
        request.session["favorite_review"] = review_id
        return HttpResponseRedirect("/reviews/" + review_id)

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


