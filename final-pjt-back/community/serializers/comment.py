from rest_framework import serializers
from django.contrib.auth import get_user_model
from ..models import Comment

User = get_user_model()

# CUD => validation
# R => Data serializing
class CommentSerializer(serializers.ModelSerializer):
    
    class UserSerializer(serializers.ModelSerializer):
        class Meta:
            model = User
            fields = ('pk', 'username')

    user = UserSerializer(read_only=True)
    
    like_users = UserSerializer(read_only=True, many=True)
    # like_comment_count = serializers.IntegerField()

    class Meta:
        model = Comment
        fields = ('pk', 'user', 'content', 'review', 'like_users')
        read_only_fields = ('review', )