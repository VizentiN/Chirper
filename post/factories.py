import factory
from django.contrib.auth.models import User
from .models import Post

class UserFactory(factory.django.DjangoModelFactory):
    username = factory.Faker('pystr')
    email = factory.Faker('pystr')

    class Meta:
        model = User

class PostFactory(factory.django.DjangoModelFactory):
    user = factory.SubFactory(UserFactory)
    content = factory.Faker('text', max_nb_chars=280)
    created_at = factory.Faker('past_datetime', start_date="-30d")  # Posts from the last 30 days
    updated_at = factory.LazyAttribute(lambda obj: obj.created_at)

    class Meta:
        model = Post