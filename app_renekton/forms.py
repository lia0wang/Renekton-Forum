from django import forms
from .models import Topic
class TopicForm(forms.ModelForm):
    class Meta:
        model = Topic
        fields = ['topic_name']
        labels = {'topic_name': ''}