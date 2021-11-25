from django.contrib import admin

# Register your models here.
# Register the topic with the admin site
from .models import Topic
admin.site.register(Topic)