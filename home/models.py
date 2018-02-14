from django.db import models

class Room(models.Model):
    """model for each room listing"""
    # add roommate preferences in the future
    host_name = models.CharField(max_length=50)
    address = models.CharField(max_length=100)
    property_name = models.CharField(max_length=30, default="")
    description = models.TextField(default="No Description")
    cost = models.PositiveIntegerField(default=0)
    visists = models.PositiveIntegerField(default=0)
    number_of_rooms = models.PositiveSmallIntegerField()
    last_updated = models.DateTimeField('last updated') # ToDo: Fix the timezone issue

    def __str__(self):
        return self.property_name
