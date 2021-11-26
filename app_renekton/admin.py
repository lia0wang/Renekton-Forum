from django.contrib import admin

# Register your models here.
# Register the topic with the admin site
from .models import Topic
from .models import Post

admin.site.register(Topic)
admin.site.register(Post)