from django.db import models

# In app/models.py

from django.db import models

class Event(models.Model):
    event_name = models.CharField(max_length=100)
    event_place = models.CharField(max_length=100)
    event_date = models.DateField()
    event_description = models.TextField()
    event_coordinator = models.CharField(max_length=100)
    # date = models.DateTimeField(auto_now_add=True, default='')

    def __str__(self):
        return self.event_name

