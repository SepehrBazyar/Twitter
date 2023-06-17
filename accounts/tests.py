from django.test import TestCase
from .models import User, Relation

# Create your tests here.
class UserTestCase(TestCase):

    def setUp(self) -> None:
        self.john = User.objects.create(username='john', password='foobar', age=10)
        self.alex = User.objects.create(username='alex', password='foobar', age=20)
        self.mary = User.objects.create(username='mary', password='foobar', age=30)

    def test_followings_count(self):
        Relation.objects.create(from_user=self.john, to_user=self.alex)
        Relation.objects.create(from_user=self.john, to_user=self.mary)
        self.assertEqual(self.john.followings_count, 2)

    def test_followers_count(self):
        Relation.objects.create(to_user=self.john, from_user=self.alex)
        Relation.objects.create(to_user=self.john, from_user=self.mary)
        self.assertEqual(self.john.followers_count, 2)
