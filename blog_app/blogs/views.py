from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse

from .permissions import IsAdmin
from .models import User, Post
from .serializers import UserSerializer, PostSerializer
from rest_framework import generics, permissions

@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'posts': reverse('post-list', request=request, format=format),
    })

class UserList(generics.ListCreateAPIView):
  queryset = User.objects.all()
  serializer_class = UserSerializer

  def get(self, request, *args, **kwargs):
    return self.list(request, *args, **kwargs)

  def post(self, request, *args, **kwargs):
    return self.create(request, *args, **kwargs)


class UserDetail(generics.RetrieveUpdateDestroyAPIView):
  queryset = User.objects.all()
  serializer_class = UserSerializer

  def get(self, request, *args, **kwargs):
    return self.retrieve(request, *args, **kwargs)

  def put(self, request, *args, **kwargs):
    return self.update(request, *args, **kwargs)

  def delete(self, request, *args, **kwargs):
    return self.destroy(request, *args, **kwargs)


class PostList(generics.ListCreateAPIView):
  queryset = Post.objects.all()
  serializer_class = PostSerializer
  permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

  def get(self, request, *args, **kwargs):
    return self.list(request, *args, **kwargs)

  def post(self, request, *args, **kwargs):
    return self.create(request, *args, **kwargs)


class PostDetail(generics.RetrieveUpdateDestroyAPIView):
  queryset = Post.objects.all()
  serializer_class = PostSerializer
  permission_classes = (IsAdmin,)

  def get(self, request, *args, **kwargs):
    return self.retrieve(request, *args, **kwargs)

  def put(self, request, *args, **kwargs):
    return self.update(request, *args, **kwargs)

  def delete(self, request, *args, **kwargs):
    return self.destroy(request, *args, **kwargs)
