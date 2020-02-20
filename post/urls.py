from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='post-index'),
    path('<int:id>/', views.about, name='post-about'),
    path('addComment/<int:id>', views.addComment, name='add-comment'),
    path('newPost/', views.newPost, name='new-post')
]
