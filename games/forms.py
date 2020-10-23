from django import forms
from django.db import models
from django.forms import ModelForm
from . models import GenreTag, ThemeTag, MiscTag
GAME_SORT_CHOICES = [
    ('Order by date (Asc)', 'Order by...'),
    ('Order by date (Asc)', 'Sort by date (Asc)'),
    ('Order by date (Desc)', 'Sort by date (Desc)'),
    ('Order by score (Asc)', 'Sort by score (Asc)'),
    ('Order by score (Desc)', 'Sort by score (Desc)'),
]

GAME_TIME_CHOICES = [
    ('Show all time', 'Show by release date...'),
    ('Show all time', 'Show all time'),
    ('Show last week', 'Show last week'),
    ('Show last month', 'Show last month'),
    ('Show last 3 months', 'Show last 3 months'),
    ('Show last 6 months', 'Show last 6 months'),
    ('Show last year', 'Show last year'),
]

GAME_VIEW_CHOISES = [
    ('Show default', 'Show default list...'),
    ('Show compact list', 'Show compact list'),
    ('Show expanded list', 'Show expanded list'),
]

GENRE_TAGS = [tuple((tag.id, tag.long_name))
              for tag in GenreTag.objects.all()]


class GameSortShowForms(forms.Form):
    sort = forms.MultipleChoiceField(
        label=False,
        widget=forms.Select(
            attrs={
                'class': 'form-control-sm w-100 SortShowForm-auto-submit',
            }
        ),
        choices=GAME_SORT_CHOICES, initial='3',
    )

    time = forms.MultipleChoiceField(
        label=False,
        widget=forms.Select(
            attrs={'class': 'form-control-sm w-100 SortShowForm-auto-submit'}
        ),
        choices=GAME_TIME_CHOICES,
    )

    # The form Works fine but removed for this version of the application 
    # since there is not enough time to add the functions for it
    '''
    view = forms.MultipleChoiceField(
        label=False,
        widget=forms.Select(
            attrs={'class': 'form-control-sm w-100 SortShowForm-auto-submit'}
        ),
        choices=GAME_VIEW_CHOISES,
    )
    '''


class GameFilterGenreForm(forms.Form):
    genre_filter = forms.MultipleChoiceField(
        label=True,
        widget=forms.CheckboxSelectMultiple(
            attrs={'class': 'genre-filter-checkbox z-index-20'}
        ),
        choices=GENRE_TAGS,
    )

    def as_plain(self):
        # Returns this form rendered as HTML <tr>s -- excluding the <table></table>
        return self._html_output(
            normal_row='%(label)s%(errors)s%(field)s%(help_text)s',
            error_row='%s',
            row_ender='',
            help_text_html='<br /><span class="helptext">%s</span>',
            errors_on_separate_row=False)
