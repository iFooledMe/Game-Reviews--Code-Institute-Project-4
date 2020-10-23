from django import forms
from django.db import models
from django.forms import ModelForm
from .models import UserCommentsScore
from django.contrib.auth.models import User


USER_SCORE_CHOICES = [
    ('0', 'No score'),
    ('1', '1'),
    ('2', '2'),
    ('3', '3'),
    ('4', '4'),
    ('5', '5'),
    ('6', '6'),
    ('7', '7'),
    ('8', '8'),
    ('9', '9'),
    ('10', '10'),
]

class NewCommentForm(forms.ModelForm):
    class Meta:
        model = UserCommentsScore
        label = False
        fields = ['comment', 'user_score']
        widgets = {
            'comment': forms.Textarea(
                attrs={'class': 'form-control mt-2'}
            ),
            'user_score': forms.Select(
                choices=USER_SCORE_CHOICES,
                attrs={'class': 'form-control'}
            ),   
        }
        labels = {
            'comment': '',
            'user_score': 'Your score 1-10(best)',
        }
            
class EditCommentForm(forms.ModelForm):
    class Meta:
        model = UserCommentsScore
        label = False
        fields = ['comment', 'user_score']
        widgets = {
            'comment': forms.Textarea(
                attrs={'class': 'form-control mt-2'}
            ),
            'user_score': forms.Select(
                choices=USER_SCORE_CHOICES,
                attrs={'class': 'form-control'}
            ),   
        }
        labels = {
            'comment': '',
            'user_score': 'Your score 1-10(best) - In the field below',
        }


class EditUserForm(forms.ModelForm):
    class Meta:
        model = User
        label = True
        fields = ['first_name', 'last_name', 'email', 'username']
        widgets = {
            'first_name': forms.TextInput(
                attrs={'class': 'form-control mb-3',

                       }
            ),
            'last_name': forms.TextInput(
                attrs={'class': 'form-control mb-3',

                       }
            ),
            'email': forms.TextInput(
                attrs={'class': 'form-control mb-3',

                       }
            ),
            'username': forms.TextInput(
                attrs={'class': 'form-control ',

                       }
            ),
        }
        labels = {
            'first_name': 'Last name',
            'last_name': 'First name',
        }
