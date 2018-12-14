from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.contrib.auth  import get_user_model
from django.contrib.auth.models import AbstractUser
from ckeditor_uploader.fields import RichTextUploadingField
# Create your models here.




class NoteModel(models.Model) :
    author = models.ForeignKey(get_user_model(), related_name = "authors", on_delete=models.CASCADE )
    title = models.CharField(max_length = 150)
    content = RichTextUploadingField()
    date = models.DateTimeField(auto_now = True)

    def get_absolute_url(self):
        return reverse('home')

    def __str__(self) :
        return "{} {}".format(self.title, self.content)




