from django.urls import path
from django.contrib.auth import views as views_auth
from . import views
from django.conf.urls.static import static
from django.conf import settings
from django.contrib import admin


urlpatterns = [
    path('create/', views.create, name='user-create'),
    path('login/', views_auth.LoginView.as_view(template_name='user/login.html'), name='login'),
    path('logout/', views_auth.LogoutView.as_view(template_name='user/logout.html'), name='logout'),
    path('profile/<int:id>/', views.profile, name='user-profile')
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
