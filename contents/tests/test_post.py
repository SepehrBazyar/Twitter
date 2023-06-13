from django.test import TestCase
from .models import Post

# Create your tests here.
class PostTestCase(TestCase):
    def setUp(self) -> None:
        self.post = Post.objects.create()
        return super().setUp()
    
    def test_true_like(self):
        self.assertTrue(self.post.is_liked_by_user(user))
