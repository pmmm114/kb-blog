from django.db import models
# timezone
from django.utils import timezone
#ekeditor
from ckeditor.fields import RichTextField
# Auth user model
from django.contrib.auth.models import AbstractUser
from django.conf import settings

class User(AbstractUser):
    pass

class Post(models.Model):
    post_num = models.AutoField(primary_key=True)
    post_title = models.CharField(max_length=100)
    post_content = RichTextField(config_name='post_ckeditor')
    post_date = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )