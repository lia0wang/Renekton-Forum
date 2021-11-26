from django.shortcuts import render
from .models import Topic

# Create your views here.
def index(request):
    '''Home page'''
    return render(request, 'app_renekton/index.html')

def topics(request):
    '''Topics page'''
    topics = Topic.objects.order_by('date_added')
    context = {'topics': topics}
    return render(request, 'app_renekton/topics.html', context)

def topic(request, topic_id):
    '''Show a single topic and all its posts.'''
    topic = Topic.objects.get(id=topic_id)
    # '-' sorts the results in reverse order to display the most recent post
    posts = topic.post_set.order_by('-date_added')
    context = {'topic': topic, 'posts': posts}
    return render(request, 'app_renekton/topic.html', context)
 