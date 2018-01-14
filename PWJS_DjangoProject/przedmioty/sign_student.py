from django import forms

class SignStudentForm(forms.Form):
    name = forms.CharField(max_length=40)