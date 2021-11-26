from django import forms
from .models import Topic, Post

class TopicForm(forms.ModelForm):
    class Meta:
        model = Topic
        fields = ['topic_name']
        labels = {'topic_name': ''}

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['text']
        labels = {'text': 'Post:'}
        widgets = {'text': forms.Textarea(attrs={'cols': 80})}