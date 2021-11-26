from django.shortcuts import render, redirect
from .models import Topic
from .forms import PostForm, TopicForm

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
 
def new_topic(request):
    """Add a new topic."""
    if request.method != 'POST':
        # No data submitted; create a blank form.
        form = TopicForm()
    else:
        # POST data submitted; process data.
        form = TopicForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('app_renekton:topics')
    # Display a blank or invalid form.
    context = {'form': form}
    return render(request, 'app_renekton/new_topic.html', context)

def new_post(request, topic_id):
    """Add a new post for a particular topic."""
    topic = Topic.objects.get(id=topic_id)
    if request.method != 'POST':
        # No data submitted; create a blank form.
        form = PostForm()
    else:
        # POST data submitted; process data.
        form = PostForm(data=request.POST)
        if form.is_valid():
            new_post = form.save(commit=False)
            new_post.topic = topic
            new_post.save()
            return redirect('app_renekton:topic', topic_id=topic_id)
    # Display a blank or invalid form.
    context = {'topic': topic, 'form': form}
    return render(request, 'app_renekton/new_post.html', context)