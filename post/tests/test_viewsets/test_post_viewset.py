import json
from django.urls import reverse
from rest_framework.test import APIClient, APITestCase
from rest_framework.views import status
from rest_framework.authtoken.models import Token

from post.factories import UserFactory, PostFactory
from post.models.post import Post

class TestPostViewSet(APITestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = UserFactory()
        self.client.force_authenticate(user=self.user)  # Força a autenticação do usuário para os testes
        token = Token.objects.create(user=self.user)
        token.save

        self.post = PostFactory(
            user=self.user,
            content="Something test",
        )
    
    def test_get_all_posts(self):
        token = Token.objects.get(user__username=self.user.username)
        self.client.credentials(HTTP_AUTHORIZATION="Token " + token.key)
        
        # Incluindo o argumento 'version' na chamada reverse
        response = self.client.get(reverse("post-list", kwargs={'version': 'v1'}))
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        post_data = json.loads(response.content)
        results = post_data['results']

        # Ajuste para verificar corretamente se o conteúdo está presente na resposta
        self.assertTrue(any(post['content'] == self.post.content for post in results))

    def test_create_post(self):
        token = Token.objects.get(user__username=self.user.username)
        self.client.credentials(HTTP_AUTHORIZATION="Token " + token.key)
        data = json.dumps({
            "user": self.user.id,
            "content": "New post content"
        })

        # Incluindo o argumento 'version' na chamada reverse
        response = self.client.post(
            reverse("post-list", kwargs={'version': 'v1'}),
            data=data,
            content_type="application/json"
        )

        
        # import pdb; pdb.set_trace()

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        created_post = Post.objects.get(content="New post content")
        self.assertEqual(created_post.user.id, self.user.id)
        self.assertEqual(created_post.content, "New post content")