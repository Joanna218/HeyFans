from django.urls import path
from . import views

urlpatterns = [
    path('', views.posts_list, name='posts_list'),
    # path('<int:pk>/', views.store_detail, name='store_detail'),
    # path('new/', views.store_create, name="store_create"),
    # path('<int:pk>/update/', views.store_update, name="store_update"),
]
