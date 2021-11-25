from django.db import models

class Topic(models.Model):
    """A topic the user is learning about."""
    # use CharField when you want to store a small amount of text
    topic_name = models.CharField(max_length=200)

    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """Return a string representation of the model."""
        return self.topic_name

