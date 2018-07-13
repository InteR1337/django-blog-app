from .models import User, Post
from rest_framework import serializers

class PostSerializer(serializers.ModelSerializer):
  class Meta:
    model = Post
    fields = ('id', 'text', 'pub_date', 'likes', 'user')

class UserSerializer(serializers.ModelSerializer):
  posts = PostSerializer(many=True, required=False)

  class Meta:
    model = User
    fields = ('id', 'name', 'posts', 'is_admin')
