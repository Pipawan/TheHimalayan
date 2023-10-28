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
        labels={'username':'Username','password':'Password','email':'Email','first_name':'First name','last_name':'Last Name'}

        widgets={
            'username':forms.TextInput(attrs={'class':'form-control','placeholder':'Username'}),
            'password':forms.TextInput(attrs={'class':'form-control','placeholder':''}),
            'email':forms.TextInput(attrs={'class':'form-control','placeholder':'Email'}),
            'first_name':forms.TextInput(attrs={'class':'form-control','placeholder':'First Name'}),
            'last_name':forms.TextInput(attrs={'class':'form-control','placeholder':'Last Name'}),
        }

class FeedBackForm(forms.Form):
    name=forms.CharField(max_length=100)
    email=forms.EmailField()
    subject=forms.CharField(max_length=100)
    message=forms.CharField(widget=forms.Textarea)

