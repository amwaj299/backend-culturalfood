# Create your tests here.
from django.test import TestCase
from django.contrib.auth.models import User
from main_app.models import Dish, Tag, Location


class ModelsTest(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(username='amwaj', password='12345')
        self.loc1 = Location.objects.create(name='Saudi Arabia')
        self.loc2 = Location.objects.create(name='Japan')
        self.tag1 = Tag.objects.create(name='Spicy')
        self.tag2 = Tag.objects.create(name='Seafood')

        self.dish1 = Dish.objects.create(
            name='Kabsa',
            description='Traditional Saudi rice with meat',
            photo='http://example.com/kabsa.jpg',
            origin=self.loc1,
            user=self.user
        )

        self.dish2 = Dish.objects.create(
            name='Sushi',
            description='Rice and fish rolls',
            photo='http://example.com/sushi.jpg',
            origin=self.loc2,
            user=self.user
        )

        self.dish1.tags.set([self.tag1])
        self.dish2.tags.set([self.tag2])

    def test_user_create(self):
        self.assertEqual(str(self.user), 'amwaj')

    def test_location_create(self):
        self.assertEqual(str(self.loc1), 'Saudi Arabia')
        self.assertEqual(str(self.loc2), 'Japan')

    def test_tag_create(self):
        self.assertEqual(str(self.tag1), 'Spicy')
        self.assertEqual(str(self.tag2), 'Seafood')

    def test_dish_create(self):
        self.assertEqual(str(self.dish1), 'Kabsa')
        self.assertEqual(str(self.dish2), 'Sushi')

    def test_dish_user_relationship(self):
        self.assertEqual(self.dish1.user.username, 'amwaj')
        self.assertEqual(self.dish2.user.username, 'amwaj')

    def test_dish_location_relationship(self):
        self.assertEqual(self.dish1.origin.name, 'Saudi Arabia')
        self.assertEqual(self.dish2.origin.name, 'Japan')

    def test_dish_tags_relationship(self):
        self.assertEqual(self.dish1.tags.count(), 1)
        self.assertEqual(self.dish2.tags.count(), 1)
        self.assertIn(self.tag1, self.dish1.tags.all())
        self.assertIn(self.tag2, self.dish2.tags.all())

    def test_deleting_user_cascades_to_dishes(self):
        self.user.delete()
        self.assertEqual(Dish.objects.count(), 0)


    def test_deleting_location_cascades_to_dishes(self):
        loc_id = self.loc1.id
        self.loc1.delete()
        self.assertEqual(Dish.objects.filter(origin_id=loc_id).count(), 0)



