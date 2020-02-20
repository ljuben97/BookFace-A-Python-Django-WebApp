from django.shortcuts import render, redirect
from .forms import UserRegisterForm
from django.contrib.auth.decorators import login_required
from .models import Profile
from friends.models import Friend, Request
from django.contrib.auth.admin import User
from django.db.models import Q


# Create your views here.


def create(request):
    if request.method == 'GET':
        form = UserRegisterForm()
        context = {
            'form': form
        }
        return render(request, 'user/register.html', context)

    elif request.method == 'POST':

        form = UserRegisterForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('post-index')
        else:
            print(form.errors)


def profile(request, id):
    user = User.objects.get(pk=id)
    profileUser = Profile.objects.get(user=user)
    fr = 2
    if request.user.is_authenticated:
        userLogged = request.user
        friends = Friend.objects.filter(Q(user1=userLogged) & Q(user2=user))
        requestTo = Request.objects.filter(Q(requested_by=userLogged) & Q(requested_to=user))
        requestFrom = Request.objects.filter(Q(requested_by=user) & Q(requested_to=userLogged))
        if friends.count() > 0:
            fr = 0
        elif requestTo.count() > 0:
            fr = 1
        elif requestFrom.count() > 0:
            fr = -1
        else:
            fr = -2
    context = {
        'profile': profileUser,
        'fr': fr
    }
    return render(request, 'user/profile.html', context)
