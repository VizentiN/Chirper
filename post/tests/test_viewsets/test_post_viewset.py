import json
from django.urls import reverse
from rest_framework.test import APIClient, APITestCase
from rest_framework.views import status

from post.factories import UserFactory, PostFactory
from post.models.post import Post

class TestPostViewSet(APITestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = UserFactory()
        self.client.force_authenticate(user=self.user)  # Força a autenticação do usuário para os testes

        self.post = PostFactory(
            user=self.user,
            content="Something test",
        )
    
    def test_get_all_posts(self):
        response = self.client.get(reverse("post-list"))  # Ajustado para corresponder às suas rotas
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        post_data = json.loads(response.content)

        # Ajuste para verificar corretamente se o conteúdo está presente na resposta
        self.assertTrue(any(post['content'] == self.post.content for post in post_data))

    def test_create_post(self):
        data = json.dumps({
            "content": "New post content"
        })

        response = self.client.post(
            reverse("post-list"),
            data=data,
            content_type="application/json"
        )

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        created_post = Post.objects.get(content="New post content")
        self.assertEqual(created_post.content, "New post content")