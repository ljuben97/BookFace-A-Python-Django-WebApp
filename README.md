# BookFace - A Django Python Project 

This project was made in python in the Django framework to resemble the FaceBook website and systems. The project has 3 main apps built in it:

* **Users**
* **Friends**
* **Post**

## Users App

The user app contains a Register and Login system that's already built in by Django with an email field also added. It contains a register page and login page:

### The Register Page:
![alt text](https://raw.githubusercontent.com/ljuben97/BookFace-A-Python-Django-WebApp/master/screens/Register.png)

### The Log In Page:

![](https://raw.githubusercontent.com/ljuben97/BookFace-A-Python-Django-WebApp/master/screens/Login.png)

When a user is created it automatically generates a profile for the user and a profile page dedicated to the User

### The Profile Page:

![](https://raw.githubusercontent.com/ljuben97/BookFace-A-Python-Django-WebApp/master/screens/profile.png)

## Friends App

When the user profile is created the user can add friends. This can be done by going to the profile page on the friend it wants to add and click on the **Add Friend** button. 

After that a friend request will be sent to the user and the user can either accept or decline the request. The user who sent the request can also unsend the friend request or unfriend users who he is already friends with. 

The **/friends** page displays the users who the logged in user is friends with along with the friend requests he has sent and the friend requests he has received

### The Friends Page:

![](https://raw.githubusercontent.com/ljuben97/BookFace-A-Python-Django-WebApp/master/screens/Friends.png)

## Post App

The post app gives the user the ability to post a thread that consists of a:

* **Title**
* **Description**

The user can post a thread an also receive all the other Threads posted only by the users he is friends with along with all the comments of every thread. 

The user also has the ability to post a comment on a thread

### The Post Page:

![](https://raw.githubusercontent.com/ljuben97/BookFace-A-Python-Django-WebApp/master/screens/Post.png)

## Sample Code

Bellow is a sample code of the Friends Views. I hope you all like this project. In the future I plan to add a fully functional likes system and also polish up the CSS a little bit to make it look more modern and clean. 

### Friends Views Code:

```
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .models import Friend, Request
from users.models import Profile
from django.db.models import Q


# Create your views here.

@login_required
def index(request):
    user = request.user
    friends = Friend.objects.filter(user1=user).values_list('user2', flat=True)
    friendsProfiles = Profile.objects.filter(user__in=friends)
    requests = Request.objects.filter(requested_by=user).values_list('requested_to', flat=True)
    requestsProfiles = Profile.objects.filter(user__in=requests)
    requestedFrom = Request.objects.filter(requested_to=user).values_list('requested_by', flat=True)
    requestedFromProfiles = Profile.objects.filter(user__in=requestedFrom)
    context = {
        'friends': friendsProfiles,
        'requests': requestsProfiles,
        'requestedFrom': requestedFromProfiles
    }
    return render(request, 'friends/index.html', context)


@login_required
def handle_friend_request(request):
    if request.method == 'POST':
        user = request.user
        userRequesting = User.objects.get(pk=request.POST['requesting'])
        friendRequest = Request.objects.filter(Q(requested_by=userRequesting) & Q(requested_to=user))
        if friendRequest.count() > 0:
            if request.POST['selected'] == 'accept':
                friendRequest.delete()

                friends1 = Friend()
                friends1.user1 = user
                friends1.user2 = userRequesting
                friends1.save()

                friends2 = Friend()
                friends2.user2 = user
                friends2.user1 = userRequesting
                friends2.save()

            elif request.POST['selected'] == 'decline':
                friendRequest.delete()

    return redirect('friends-index')


@login_required
def send_friend_request(request):
    user = request.user
    if request.method == 'POST':
        userRequested = User.objects.get(pk=request.POST['requestedTo'])
        friendRequest = Request.objects.filter((Q(requested_by=user) & Q(requested_to=userRequested)) | (
                Q(requested_by=userRequested) & Q(requested_to=user)))
        if friendRequest.count() == 0:
            friendRequest = Request()
            friendRequest.requested_by = user
            friendRequest.requested_to = userRequested
            friendRequest.save()
    return redirect('friends-index')


@login_required
def delete_friend_request(request):
    userLogged = request.user
    if request.method == 'POST':
        userRequested = User.objects.get(pk=request.POST['requestedTo'])
        friendRequest = Request.objects.filter(Q(requested_by=userLogged) & Q(requested_to=userRequested))
        if friendRequest.count() > 0:
            friendRequest.delete()

    return redirect('friends-index')


@login_required
def unfriend(request):
    userLogged = request.user
    if request.method == 'POST':
        userRequested = User.objects.get(pk=request.POST['requestedTo'])
        friends1 = Friend.objects.filter(Q(user1=userLogged) & Q(user2=userRequested))
        friends2 = Friend.objects.filter(Q(user2=userLogged) & Q(user1=userRequested))

        if friends1.count() > 0 and friends2.count() > 0:
            friends1.delete()
            friends2.delete()

    return redirect('friends-index')
```

