from django.shortcuts import render, get_object_or_404
from django.views.generic import CreateView,UpdateView,DeleteView,DetailView,ListView,TemplateView
from notes.models import *
from notes.forms import *
from django.urls import reverse_lazy
from django.contrib.auth  import get_user_model
# Create your views here.



class HomeIndex(TemplateView) :
    
    template_name = "home.html"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        self.author = self.request.user
        context["note_list"] = NoteModel.objects.filter(author = self.author)[:5]
        return context
    

    
class NoteUpdateView(UpdateView) :

    form_class = CreateForm
    model = NoteModel
    template_name = "update.html"


class NoteCreateView(CreateView) :
    
    model = NoteModel
    form_class = CreateForm
    template_name = "note.html"
    
    
    
    def form_valid(self, form) :
        form.instance.author = self.request.user        # to input author field with username
        return super().form_valid(form)


class NoteListView(ListView) :
    template_name = "list.html"
    context_object_name = "note_list"

    def get_queryset(self) :
        self.author = self.request.user
        return NoteModel.objects.filter(author = self.author)

class NoteDetailView(DetailView) :

    model = NoteModel
    context_object_name = "detail_note"
    template_name = "detail.html"




class NoteDeleteView(DeleteView) :
    
    model = NoteModel
    success_url = reverse_lazy("notes:list")
    template_name = "delete.html"
