from django.db import models
from django.db.models.fields import TimeField
from django.db.models.fields.related import ForeignKey

class Topic(models.Model):
    """A topic the user is learning about."""
    # use CharField when you want to store a small amount of text
    topic_name = models.CharField(max_length=200)

    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """Return a string representation of the model."""
        return self.topic_name

class Entry(models.Model):
    """Something learned about a topic"""
    # the topic attribute is a foreign key instance
    # this is the code that connect each entry to a topic
    # key -> connect each piece of data
    # casacading delete -> on_delete=modles.CASCADE
    topic = ForeignKey(Topic, on_delete=models.CASCADE)
    # size of individual limit 
    text = models.TextField()
    # present the entries in order, place a timestamp next to each entry
    date_added = TimeField(auto_now_add=True)

    class Meta:
        # hold extra info to hold a model

        # 'verbose_name_plural' is an attribute of class Meta
        # use 'entries' instead of 'entrys' when the entry > 1
        verbose_name_plural = 'entries'
    
    def __str__(self):
        '''Return a str representation of the model.'''
        # only the first 50 words will be shown also an ellipsis to
        # show the text of the entry is not completely displayed
        if len(self.text) > 50:
            return f"{self.text[0:50]}..."
        return self.text