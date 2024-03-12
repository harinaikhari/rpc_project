# rps_app/forms.py

from django import forms

class ChoiceForm(forms.Form):
    choices = [('rock', 'Rock'), ('paper', 'Paper'), ('scissors', 'Scissors')]
    user_choice = forms.ChoiceField(choices=choices)
