from django.db import models

# Create your models here.

class Topic(models.Model):
    name = models.CharField(max_length=256,unique=True)
    timestamp=models.DateTimeField(auto_now_add=True)


class Bloglist(models.Model):

    name = models.CharField(max_length=256,unique=True)
    timestamp=models.DateTimeField(auto_now_add=True)
    desc = models.TextField(default="sample")
    likes= models.IntegerField()
    markdown=models.TextField()
    topic = models.ForeignKey('first_app.Topic',on_delete=models.CASCADE)
    image = models.CharField(max_length=256)
