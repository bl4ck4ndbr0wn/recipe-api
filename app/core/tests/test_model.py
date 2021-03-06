from django.test import TestCase
from django.contrib.auth import get_user_model

from core import models

def sample_user(email='test@gmail.com', password='testPass'):
    """Create a sample user"""
    return get_user_model().objects.create_user(email, password)


class ModelTests(TestCase):

    def test_create_user_with_email_successful(self):
        """Test create a new user with an email is successfull"""
        email = "test@gmail.com"
        password = "Testpass123"
        user = get_user_model().objects.create_user(
            email=email,
            password=password
            )

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_new_user_email_nomalized(self):
        """Test the email for a new user is normalized"""
        email = "test@GMAIL.COM"
        user = get_user_model().objects.create_user(email, "test123")

        self.assertEqual(user.email, email.lower())

    def test_new_user_invalid_email(self):
        """Test creating user with no email raises error"""
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(None, "test123")

    def test_create_new_supperuser(self):
        """Test creating a new supperuser:"""
        user = get_user_model().objects.create_superuser(
            "test@gmail.com",
            "test123"
            )

        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)

    def test_tag_str(self):
        """Test the tag string representation"""
        tag = models.Tag.objects.create(
            user=sample_user(),
            name='Vegan'
        )

        self.assertEqual(str(tag), tag.name)

    def test_ingredients_str(self):
        """Test the ingredient string reprentation"""
        ingredient = models.Ingredient.objects.create(
            user=sample_user(),
            name='Cucamber'
        )

        self.assertEqual(str(ingredient), ingredient.name)

    def test_recipe_str(self):
        """test the recipy string representation"""
        recipe = models.Recipe.objects.create(
            user=sample_user(),
            title='Stake and mushroom source',
            time_minutes=5,
            price=5.00
        )

        self.assertEqual(str(recipe), recipe.title)
