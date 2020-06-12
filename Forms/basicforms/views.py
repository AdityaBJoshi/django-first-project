from django.shortcuts import render
from . import forms

# Create your views here.
def index(request):
    return render(request,'index.html')

def forms_name_view(request):
    form = forms.FormName()
    if request.method == "post":
        form = forms.FormName(request.post)
        if form.is_valid():
            print('validationsucessful')
            print('Name:' +form.cleaned_data['name'])
            print('email:' +form.cleaned_data['email'])
            print('text:' +form.cleaned_data['text'])

    return render(request,'forms.html',{'form':form})
