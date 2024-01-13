from django.shortcuts import get_object_or_404
from rest_framework import viewsets, permissions, filters, generics
from rest_framework.pagination import LimitOffsetPagination

from posts.models import Post, Group, Follow, User
from .serializers import (
    PostSerializer, CommentSerializer, GroupSerializer, FollowSerializer)
from .permissions import IsAuthorOrReadOnlyPermission, FollowPermission


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = (IsAuthorOrReadOnlyPermission,)
    pagination_class = LimitOffsetPagination

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class CommentViewSet(viewsets.ModelViewSet):
    serializer_class = CommentSerializer
    permission_classes = (IsAuthorOrReadOnlyPermission,)

    def get_post(self, **kwargs):
        """Получаем пост с нужным id."""
        return get_object_or_404(Post, pk=self.kwargs.get('post_id'))

    def get_queryset(self):
        return self.get_post().comments.all()

    def perform_create(self, serializer):
        serializer.save(post=self.get_post(), author=self.request.user)


class GroupViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = (permissions.AllowAny,)


class FollowList(generics.ListCreateAPIView):
    queryset = Follow.objects.all()
    serializer_class = FollowSerializer
    permission_classes = (FollowPermission,)
    filter_backends = (filters.SearchFilter,)
    search_fields = ('following__username',)

    def perform_create(self, serializer):
        serializer.save(
            user=self.request.user,
            following=get_object_or_404(
                User, username=self.request.data.get('following'))
        )
