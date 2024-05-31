from rest_framework.viewsets import ModelViewSet

from post.models import Post
from post.serializers import PostSerializer

class PostViewSet(ModelViewSet):
    serializer_class = PostSerializer

    def get_queryset(self):
        return Post.objects.all().order_by('-created_at')