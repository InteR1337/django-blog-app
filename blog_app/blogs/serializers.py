from .models import User, Post
from rest_framework import serializers

class UserSerializer(serializers.HyperlinkedModelSerializer):
  class Meta:
    model = User
    fields = ('id', 'name')

class PostSerializer(serializers.HyperlinkedModelSerializer):
  user = UserSerializer(required=True)

  class Meta:
    model = Post
    fields = ('text', 'pub_date', 'likes', 'user')
