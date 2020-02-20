from django.forms import Form
from django import forms


class NewComment(Form):
    description = forms.CharField(label='', widget=forms.TextInput(attrs={'placeholder': 'Write a comment...'}), )


class NewPostAdd(Form):
    title = forms.CharField(label='', max_length=100, widget=forms.TextInput(attrs={'placeholder': 'Post title'}))
    content = forms.CharField(label='', widget=forms.Textarea(attrs={'placeholder': 'Post description', 'rows': 2}))
