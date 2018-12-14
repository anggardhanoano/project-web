from django.contrib.auth.decorators import login_required
from django.urls import path
from notes.views import *


app_name = "notes"

urlpatterns = [
    path("", login_required(NoteCreateView.as_view()), name = "create"),
    path("list", login_required(NoteListView.as_view()), name = "list"),
    path("<int:pk>/", login_required(NoteDetailView.as_view()), name = "detail"),
    path("update/<int:pk>/", login_required(NoteUpdateView.as_view()), name = "update"),
    path("delete/<int:pk>/", login_required(NoteDeleteView.as_view()), name = "delete"),

]