from django.shortcuts import render, redirect
from .models import Topic, Post
from .forms import PostForm, TopicForm
from django.contrib.auth.decorators import login_required
from django.http import Http404

# Create your views here.
def index(request):
    '''Home page'''
    return render(request, 'app_renekton/index.html')

# @login_required is to check if the user is logged in
# python will run the code inside login_required before topics
@login_required
def topics(request):
    '''Topics page'''
    topics = Topic.objects.order_by('date_added')

    # topics are only visualable to the owners of them
    # topics = Topic.objects.filter(owner=request.user).order_by('date_added')

    context = {'topics': topics}
    return render(request, 'app_renekton/topics.html', context)

@login_required
def topic(request, topic_id):
    '''Show a single topic and all its posts.'''
    topic = Topic.objects.get(id=topic_id)

    # if the user is not the owner of the topic, he cannot access the topic
    # if topic.owner != request.user:
    #     raise Http404

    # '-' sorts the results in reverse order to display the most recent post
    posts = topic.post_set.order_by('-date_added')
    context = {'topic': topic, 'posts': posts}
    return render(request, 'app_renekton/topic.html', context)
 
@login_required
def new_topic(request):
    """Add a new topic."""
    if request.method != 'POST':
        # No data submitted; create a blank form.
        form = TopicForm()
    else:
        # POST data submitted; process data.
        form = TopicForm(data=request.POST)
        if form.is_valid():
            # form.save()

            new_topic = form.save(commit=False)
            # set the new topic’s owner attribute to the user who created it 
            new_topic.owner = request.user
            new_topic.save()
            return redirect('app_renekton:topics')

    # Display a blank or invalid form.
    context = {'form': form}
    return render(request, 'app_renekton/new_topic.html', context)

@login_required
def new_post(request, topic_id):
    """Add a new post for a particular topic."""
    topic = Topic.objects.get(id=topic_id)
    # if topic.owner != request.user:
    #     raise Http404

    if request.method != 'POST':
        # No data submitted; create a blank form.
        form = PostForm()
    else:
        # POST data submitted; process data.
        form = PostForm(data=request.POST)
        if form.is_valid():
            new_post = form.save(commit=False)
            new_post.topic = topic

            # set the owner of the new added post to the user who create the post
            new_post.owner = request.user
            new_post.save()
            return redirect('app_renekton:topic', topic_id=topic_id)

    # Display a blank or invalid form.
    context = {'topic': topic, 'form': form}
    return render(request, 'app_renekton/new_post.html', context)

@login_required
def edit_post(request, post_id):
    '''Edit the current post'''
    post = Post.objects.get(id=post_id)
    topic = post.topic

    # a user cannot edit the post if he is not the owner of the post
    if post.owner != request.user:
        raise Http404

    if request.method != 'POST':
        # So the user will see their exist info of the current post so they can edit it
        form = PostForm(instance=post)
    else:
        # process POST data
        form = PostForm(instance=post, data=request.POST)
        if form.is_valid():
            form.save()
            # redirect to the topic page, where the user should see the updated version of the entry they edited
            return redirect('app_renekton:topic', topic_id=topic.id)
    
    # if the no data submitted or the form is invalid, render the page using the edit_post html template
    context = {'post': post, 'topic': topic, 'form': form}
    return render(request, 'app_renekton/edit_post.html', context)
