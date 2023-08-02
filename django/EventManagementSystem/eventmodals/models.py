 
from django.contrib.auth.models import User 
from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()




class User(AbstractUser):
    
    pass

    def __str__(self):
        return str(self.id)


class Event(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    date = models.DateField()
    time = models.TimeField()
    location = models.ManyToManyField('Venue', related_name='events')
    capacity = models.PositiveIntegerField()
    categories = models.ManyToManyField('Category', related_name='events')
    creator = models.ForeignKey('User', on_delete=models.CASCADE,default=0)
    def __str__(self):
        return str(self.title)

class Registration(models.Model):
    event = models.ForeignKey('Event', on_delete=models.PROTECT)
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    registration_date = models.DateTimeField(auto_now_add=True)
    username=models.CharField(max_length=100,default="none")
    email=models.CharField(max_length=30,default="none")
    is_payed = models.BooleanField(default=False)
    

    def __str__(self):
        return str(self.id)


class Venue(models.Model):
    capacity = models.PositiveIntegerField()
    name = models.CharField(max_length=200,default="HVG")
    availability = models.TextField()
    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


User._meta.get_field('groups').remote_field.related_name = 'eventmodals_user_groups'
User._meta.get_field('groups').remote_field.related_query_name = 'eventmodals_user_groups'
User._meta.get_field('user_permissions').remote_field.related_name = 'eventmodals_user_permissions'
User._meta.get_field('user_permissions').remote_field.related_query_name = 'eventmodals_user_permissions'
