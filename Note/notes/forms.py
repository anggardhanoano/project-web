from django import forms
from django.forms import ModelForm
from notes.models import *


class CreateForm(forms.ModelForm) :
    
    title = forms.CharField(label = "",widget=forms.TextInput(
        attrs = {
                "id" : "title",
                "class" : "form-control",
                "placeholder" : "Note Title",            
                }
    ))

    class Meta:
        model = NoteModel
        fields = ("title", "content") 

