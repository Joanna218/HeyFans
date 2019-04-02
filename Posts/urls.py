from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('posts_list', views.posts_list, name='posts_list'),
    path('posts_list/<int:pk>/', views.posts_detail, name='posts_detail'),
    # path('<int:pk>/', views.store_detail, name='store_detail'),
    # path('new/', views.store_create, name="store_create"),
    # path('<int:pk>/update/', views.store_update, name="store_update"),
]

# paht() 要給name是可以給這給路徑一個名稱，之後連結直接給它名稱即可
