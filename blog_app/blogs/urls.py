from django.urls import path
from django.conf.urls import url, include
from rest_framework import routers

from . import views

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'posts', views.PostViewSet)

app_name = 'blogs'
urlpatterns = [
  path('', views.index, name='index'),
  path('<int:post_id>/', views.detail, name='detail'),
  path('<int:post_id>/like/', views.like, name='like'),
  path('api/v1/', include(router.urls)),
]
