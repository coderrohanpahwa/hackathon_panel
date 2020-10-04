from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm,UsernameField
from .models import Contact,Scoreboard,Answer
class SignUpForm(UserCreationForm):
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control'}),label="Enter Password")
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control'}),label="Re-Enter Password")

    class Meta:
        model=User
        fields=['first_name','email','username','password1','password2']
        labels={'first_name':'Enter name',

                'username':'Enter username',
                'email':'Enter email',
                'password1':'Enter password',
                'password2':' Re-Enter password',

                }
        widgets={
            'first_name':forms.TextInput(attrs={'class': 'form-control'}),

            'email':forms.EmailInput(attrs={'class': 'form-control'}),
            'username':forms.TextInput(attrs={'class': 'form-control'})
        }

class ContactForm(forms.ModelForm):
    class Meta:
        model=Contact
        fields=['name','email','query']
        labels={'name':'Enter name','email':'Enter email','query':'Enter query'}
        widgets={
            'name':forms.TextInput(attrs={'class':'form-control'}),
            'email':forms.EmailInput(attrs={'class':'form-control'}),
            'query':forms.Textarea(attrs={'class':'form-control'}),
        }
class ScoreboardForm(forms.ModelForm):
    class Meta:
        model=Scoreboard
        fields=['name','username','score','answer']
class AnswerForm(forms.ModelForm):
    class Meta:
        model=Answer
        fields=['name','username','answer']