from django.db import models
class Event(models.Model):
    event_title=models.CharField(max_length=120)
    event_location=models.CharField(max_length=60)
    date=models.CharField(max_length=120)

    def __str__(self):
        return self.event_title
class Eventdetail(models.Model):
    name = models.CharField(max_length=120)
    email = models.EmailField(max_length=200)
    phone = models.CharField(max_length=150)
    event=models.ForeignKey('Event',on_delete=models.CASCADE) #CASCADE is to delete all related data to delete

