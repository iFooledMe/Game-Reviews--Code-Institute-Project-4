from django import forms
from django.db import models
from django.forms import ModelForm
from .models import UserCommentsScore


class NewCommentForm(forms.ModelForm):
    class Meta:
        model = UserCommentsScore
        label = False
        fields = ['comment', 'user_score']
        widgets = {
            'comment': forms.Textarea(
                attrs={'class': 'form-control mt-2',
                       'placeholder': 'Write your comment (max 300 characters)'
                       }
            ),
            'user_score': forms.NumberInput(
                attrs={'class': 'form-control',
                       }
            ),
        }
        labels = {
            'comment': '',
            'user_score': 'Your score 1-10(best) - In the field below',
        }


class EditCommentForm(forms.ModelForm):
    class Meta:
        model = UserCommentsScore
        label = False
        fields = ['comment', 'user_score']
        widgets = {
            'comment': forms.Textarea(
                attrs={'class': 'form-control mt-2',

                       }
            ),
            'user_score': forms.NumberInput(
                attrs={'class': 'form-control',

                       }
            ),
        }
        labels = {
            'comment': '',
            'user_score': 'Your score 1-10(best) - In the field below',
        }
