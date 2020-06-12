from django import forms
from django.core import validators


class FormName(forms.Form):
    name = forms.CharField()
    email = forms.EmailField()
    text = forms.CharField(widget=forms.Textarea)
    verify_email= forms.EmailField(label="Enter the Email Again")
    botcatcher = forms.CharField(required=False,widget=forms.HiddenInput)

    def clean(self):
        all_clean_data=super().clean()
        email=all_clean_data['email']
        vemail=all_clean_data['verify_email']
        if email!=vemail:
            raise forms.ValidationError('Email doesnot matches!')



    """def clean_botcatcher(self):
        botcatcher = self.cleaned_data['botcatcher']
        if len(botcatcher)>0:
            raise forms.ValidationError("GOT CATCH")

        return botcatcher"""
