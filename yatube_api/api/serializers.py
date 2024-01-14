from rest_framework import serializers
from rest_framework.relations import SlugRelatedField


from posts.models import Comment, Post, Group, Follow, User


class PostSerializer(serializers.ModelSerializer):
    author = SlugRelatedField(slug_field='username', read_only=True)

    class Meta:
        fields = '__all__'
        model = Post


class CommentSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(
        read_only=True, slug_field='username'
    )

    class Meta:
        fields = '__all__'
        model = Comment
        read_only_fields = ('post',)


class GroupSerializer(serializers.ModelSerializer):

    class Meta:
        fields = '__all__'
        model = Group


class FollowSerializer(serializers.ModelSerializer):
    user = serializers.SlugRelatedField(
        read_only=True, slug_field='username',
        default=serializers.CurrentUserDefault()
    )
    following = serializers.SlugRelatedField(
        slug_field='username', queryset=User.objects.all()
    )

    def validate(self, data):
        """Валидация уникальности (user, following)."""
        if Follow.objects.filter(
                user=self.context['request'].user,
                following=data.get('following')).exists():
            raise serializers.ValidationError(
                'Вы уже подписаны на этого автора.')
        return data

    def validate_following(self, value):
        """Запрет подписки на самого себя."""
        if value == self.context['request'].user:
            raise serializers.ValidationError(
                'Вы не можете быть подписаны на самого себя.')
        return value

    class Meta:
        fields = ('user', 'following')
        model = Follow
