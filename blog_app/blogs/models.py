import datetime

from django.db import models
from django.utils import timezone

class User(models.Model):
  name = models.CharField(max_length=30)

  def __str__(self):
    return self.name

class Post(models.Model):
  user = models.ForeignKey(User, on_delete=models.CASCADE)
  text = models.CharField(max_length=500)
  pub_date = models.DateTimeField('date posted')
  likes = models.IntegerField(default=0)

  def was_published_recently(self):
    return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

  def __str__(self):
    return self.text
