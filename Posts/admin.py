from django.contrib import admin
from .models import Posts

# 需要後台管理Posts的文章，告訴Django要admin管理我的Posts，因此需要註冊
@admin.register(Posts)
class PostsAdmin(admin.ModelAdmin):
    # 顯示資料的欄位，名稱需一模一樣
    # list_display = ['posts_name', 'posts_contents']
    pass
