from django.contrib.auth.models import User
from rest_framework import generics, permissions
from rest_framework import viewsets

from blog.models import Blogs, Zones, Comments
from blog.serializers import BlogSerializer, UserSerializer, ZonesSerializer, CommentsSerializer
from .permissions import IsOwnerOrReadOnly


class CommentsViewSet(viewsets.ModelViewSet):
    """
    只读操作、登录用户编辑
    """
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]

    queryset = Comments.objects.all()
    serializer_class = CommentsSerializer

    # 向serializer的create()方法传递一个附加的'owner'字段
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class ZonesViewSet(viewsets.ModelViewSet):
    """
    只提供只读操作
    """
    queryset = Zones.objects.all()
    serializer_class = ZonesSerializer


class UserViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides 'list' and 'retrieve' actions.

    user视图集的注释
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer

    # 用户权限
    def get_permissions(self):
        print('self.action', self.action)
        if self.action == 'list':
            return [permissions.IsAuthenticated()]
        return []


class BlogsViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides 'list' ,'create', 'retrieve', 'update' and 'destory' actions.

    
    """
    queryset = Blogs.objects.all()
    serializer_class = BlogSerializer

    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]
    # 只有通过验证的用户才能访问。只有创建者才允许修改
    # permission_classes = [permissions.IsAuthenticated, IsOwnerOrReadOnly]
    # 不登录是也可浏览
    # permission_classes = [permissions.IsAuthenticatedOrReadOnly,]

    # 向serializer的create()方法传递一个附加的'owner'字段
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    def get_serializer_context(self):
        # print('id', dir(self.request))
        # print('id1', self.request)
        # id = self.request.id
        return {
            'request': self.request,
            'format': self.format_kwarg,
            'view': self
        }