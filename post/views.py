from django.shortcuts import render, redirect
from django.contrib.auth.admin import User
from django.contrib.auth.decorators import login_required
from .models import Post, Comment
from friends.models import Friend, Request
from .forms import NewPostAdd, NewComment
from django.db.models import Q


# Create your views here.

@login_required
def index(request):
    userLogged = request.user
    friends = Friend.objects.filter(user1=userLogged).values_list('user2', flat=True)
    posts = Post.objects.filter(Q(author__in=friends) | Q(author=userLogged)).order_by('-date_posted')
    for post in posts:
        post.comments = Comment.objects.filter(post=post).order_by('date_posted')
    context = {
        'posts': posts,
        'comment_form': NewComment(),
        'form': NewPostAdd()
    }
    return render(request, 'post/index.html', context)


@login_required
def newPost(request):
    if request.method == 'GET':
        form = NewPostAdd()
        return render(request, 'post/newPost.html', {'form': form})
    elif request.method == 'POST':
        post = Post()
        post.title = request.POST['title']
        post.content = request.POST['content']
        post.author = request.user
        post.save()
        return redirect('post-index')


@login_required
def addComment(request, id):
    post = Post.objects.get(pk=id)
    if request.method == 'GET':
        comment = NewComment()
        context = {
            'post': post,
            'comment': comment
        }
        return render(request, 'post/addComment.html', context)

    elif request.method == 'POST':
        comment = Comment()
        comment.author = request.user
        comment.description = request.POST['description']
        comment.post = post
        comment.save()
        return redirect('post-index')


@login_required
def about(request, id):
    post = Post.objects.get(pk=id)
    comments = Comment.objects.filter(post=post)
    context = {
        'post': post,
        'comments': comments,
        'comment': NewComment()
    }
    return render(request, 'post/about.html', context)
