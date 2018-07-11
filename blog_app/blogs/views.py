from django.http import HttpResponse, Http404
from django.shortcuts import render, get_object_or_404
from .models import User, Post
from rest_framework import viewsets
from .serializers import UserSerializer, PostSerializer

def index(request):
  latest_posts_list = Post.objects.order_by('-pub_date')[:5]
  context = {
    'latest_posts_list': latest_posts_list
  }

  return render(request, 'blogs/index.html', context)

def detail(request, post_id):
  post = get_object_or_404(Post, pk=post_id)
  return render(request, 'blogs/detail.html', {'post': post})

def like(request, post_id):
  return HttpResponse("You're liking the post")


class UserViewSet(viewsets.ModelViewSet):
  """
  API endpoint that allows users to be viewed or edited.
  """
  queryset = User.objects.all().order_by('name')
  serializer_class = UserSerializer


class PostViewSet(viewsets.ModelViewSet):
  """
  API endpoint that allows posts to be viewed or edited.
  """
  queryset = Post.objects.all().order_by('-pub_date')
  serializer_class = PostSerializer
