from django import forms
from django.contrib.auth.models import User
from portals.models import Comment
class CommentForm(forms.ModelForm):
    class Meta:
        model=Comment
        fields=('name','email','body')

class ContactForm(forms.Form):
    name=forms.CharField(max_length=100)
    email=forms.EmailField()
    subject=forms.CharField(max_length=100)
    message=forms.CharField(max_length=1000)

class SignUpForm(forms.ModelForm):
    class Meta:
        model=User
        fields=['username','password','email','first_name','last_name']

class FeedBackForm(forms.Form):
    name=forms.CharField(max_length=100)
    email=forms.EmailField()
    subject=forms.CharField(max_length=100)
    message=forms.CharField(widget=forms.Textarea)

