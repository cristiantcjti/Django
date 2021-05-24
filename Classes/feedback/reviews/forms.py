
from .models import Review
from django import forms
from django.forms import models

# class ReviewForm(forms.Form): #We can create our form
#    user_name = forms.CharField(label="Your Name", max_length=100, error_messages={
#        "required": "Your name must not be empty!",
#        "max_length": "Please enter a shorter name!"
#    })
#    review_text = forms.CharField(label="Your Feedback", widget=forms.Textarea, max_length=200)
#    rating = forms.IntegerField(label="Your Rating", min_value=1, max_value=5)


# We can allow django to create a form based on a model.
class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        # in case we want to selec the fields we should pass a list ['user_name', 'rating']
        fields = "__all__"
        #exclude = ['user_name', 'rating']
        labels = {
            "user_name": "Your Name",
            "review_text": "Your Feedback",
            "reting": "Your Rating"
        }
        error_messages = {
            "user_neme": {
               "required": "Your name must not be empty!",
                "max_length": "Please enter a shorter name!"
            }
        }
