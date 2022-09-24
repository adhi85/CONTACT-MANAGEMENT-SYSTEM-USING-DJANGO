from asyncio.windows_events import NULL
from email.headerregistry import Address
from pyexpat import model
from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class ContactDetails(models.Model):

    fname = models.CharField(max_length=200)
    lname = models.CharField(max_length=200)
    gender = models.CharField(max_length=50)
    age = models.PositiveIntegerField()
    address = models.TextField()
    phone = models.CharField(max_length=10)
    religion = models.CharField(max_length=50)
    nation = models.CharField(max_length=50)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    added_by=models.CharField(max_length=100,default=NULL)

    photo = models.ImageField(null=True, default="avatar.svg")

    class Meta:
        ordering = ['-updated', 'created']

    def __str__(self):
        return self.fname