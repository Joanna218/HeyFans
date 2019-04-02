from django.contrib import admin
from .models import Posts, PostsItem

# 需要後台管理Posts的文章，告訴Django要admin管理我的Posts，因此需要註冊


@admin.register(PostsItem)
class PostsItemAdmin(admin.ModelAdmin):
    list_display = ('post_name', 'post_contents',
                    'post_like_cout', 'post_id')


# 為了讓在store新增商店時就可以在下方一併新增菜單
class PostsItemInline(admin.TabularInline):
    model = PostsItem
    extra = 1


@admin.register(Posts)
class PostsAdmin(admin.ModelAdmin):
    # 顯示資料的欄位，名稱需一模一樣
    list_display = ['post_name', 'post_name_id', 'post_note']
    inlines = [PostsItemInline]
