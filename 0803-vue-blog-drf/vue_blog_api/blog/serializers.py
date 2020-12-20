from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from django.contrib.auth.hashers import make_password
from rest_framework import serializers
from .models import Blogs, Zones, Comments


class CommentsSerializer(serializers.HyperlinkedModelSerializer):
    # blog_comment = serializers.HyperlinkedRelatedField(many=True, view_name='blogs-detail', read_only=True)
    # user_comment = serializers.HyperlinkedRelatedField(many=True, view_name='blogs-detail', read_only=True)
    owner = serializers.ReadOnlyField(source='owner.username')  # 将 owner 设为只读字段
    # blog = serializers.ReadOnlyField(source='blog.id')

    class Meta:
        model = Comments
        fields = ['url', 'id', 'content', 'created', 'owner', 'blog']


class BlogSerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')  # 将 owner 设为只读字段
    blog_comment = serializers.HyperlinkedRelatedField(many=True, view_name='comments-detail', read_only=True)
    class Meta:
        model = Blogs
        fields = ['url', 'id', 'title', 'content', 'created', 'owner', 'tags', 'imgUrl', 'blog_comment']


class ZonesSerializer(serializers.HyperlinkedModelSerializer):
    
    class Meta:
        model = Zones
        fields = ['url', 'id', 'zone', 'created',]


class UserSerializer(serializers.HyperlinkedModelSerializer):
    # 序列化器可以覆盖属性
    blogs = serializers.HyperlinkedRelatedField(many=True, view_name='blogs-detail', read_only=True)
    user_comment = serializers.HyperlinkedRelatedField(many=True, view_name='comments-detail', read_only=True)

    password = serializers.CharField(style={'input_type':'password'})

    class Meta:
        model = User
        fields = ['url', 'id', 'username', 'password', 'email', 'blogs', 'user_comment']

    def create(self, validated_data):
        """
        重写create方法，创建用户时加密用户密码
        """
        if validated_data.get('password'):
            validated_data['password'] = make_password(validated_data['password'])

        user = get_user_model().objects.create(**validated_data)
        return user