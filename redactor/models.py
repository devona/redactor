from django.db import models
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField

class Post(models.Model):
    title = models.CharField(max_length=100)
    content = RichTextUploadingField()