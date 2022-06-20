from django.urls import path

from .views import posts

app_name = 'posts'
urlpatterns = [
    path('', posts.index, name='index'),
    path('create/', posts.create, name='create'),
    path('<int:pk>/update/', posts.update, name='update'),
    path('<int:pk>/delete/', posts.delete, name='delete'),
]
