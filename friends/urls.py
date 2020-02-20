from django.urls import path
from . import views

urlpatterns = [
    path('/', views.index, name='friends-index'),
    path('/requesting/', views.handle_friend_request, name='handle-friend-request'),
    path('/sendRequest/', views.send_friend_request, name='send-friend-request'),
    path('/removeRequest/', views.delete_friend_request, name='delete-friend-request'),
    path('/unfriend/', views.unfriend, name='unfriend')
]
