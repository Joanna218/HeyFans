from django.db import models

# Create your models here.

# 發文者


class Posts(models.Model):

    post_name = models.CharField(max_length=30, default="no name")
    post_name_id = models.IntegerField()
    post_note = models.CharField(max_length=30, default="no note")

    def __str__(self):
        return self.post_name

    # 每一個發文者 總共的發文內容


class PostsItem(models.Model):

    post = models.ForeignKey(
        to=Posts, related_name='postitem_set', on_delete=models.CASCADE
    )
    post_name = models.CharField(max_length=30, default="no name")
    post_contents = models.CharField(max_length=200, default="no contents")
    post_like_cout = models.IntegerField()

    def __str__(self):
        return self.post_name

    # 一個發文者 會有很多的發文內容
    # 每一個發文內容 只屬於一個發文者
