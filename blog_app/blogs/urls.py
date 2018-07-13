from django.conf.urls import include, url
from . import views
from rest_framework.urlpatterns import format_suffix_patterns

app_name = 'blogs-api'
urlpatterns = [
  url(r'^users/$', views.UserList.as_view(), name='user-list'),
  url(r'^posts/$', views.PostList.as_view(), name='post-list'),
  url(r'^users/(?P<pk>[0-9]+)/$', views.UserDetail.as_view()),
  url(r'^posts/(?P<pk>[0-9]+)/$', views.PostDetail.as_view()),
  url(r'^', include('rest_framework.urls')),
]

urlpatterns = format_suffix_patterns(urlpatterns)