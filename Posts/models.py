from django.db import models

# Create your models here.


class Posts(models.Model):
    posts_name = models.CharField(max_length=30)
    posts_contents = models.CharField(max_length=30)
