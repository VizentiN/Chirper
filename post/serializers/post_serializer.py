from rest_framework import serializers
from django.contrib.auth.models import User
from post.models import Post

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['id', 'user', 'content', 'created_at', 'updated_at']

    def create(self, validated_data):
        user = self.context['request'].user
        if not user or not user.is_authenticated:
            raise serializers.ValidationError("User must be authenticated to create a post.")

        validated_data.pop('user', None)

        post = Post.objects.create(user=user, **validated_data)
        return post