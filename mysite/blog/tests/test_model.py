from django.test import TestCase
from ..models import Post
from django.contrib.auth.models import User


class PostTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        Post.objects.create(title='ola', author=User, body='testando', tags='Musica')

    def test_title_name_label(self):
        title = Post.objects.get(id=1)
        field_label = title._meta.get_field('title').verbose_name
        self.assertEquals(field_label, 'title')




