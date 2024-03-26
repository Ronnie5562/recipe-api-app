"""
Test for models
"""

from decimal import Decimal

from django.test import TestCase
from django.contrib.auth import get_user_model

from core import models


def create_user(email="test@example.com", password="test123"):
    """Helper function to create a user"""
    return get_user_model().objects.create_user(email, password)


class ModelTests(TestCase):

    # USER MODEL TESTS

    def test_create_user_with_email_successful(self):
        """
        Test creating a new user with an email is successful
        """
        email = 'test@example.com'
        password = 'testpass123'

        user = get_user_model().objects.create_user(
            email=email,
            password=password
        )

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_new_user_email_normalized(self):
        """
        Test the email for a new user is normalized
        """
        sample_emails = [
            ["test1@EXAMPLE.com", "test1@example.com"],
            ["test2@EXAmPLe.com", "test2@example.com"],
            ["TEST3@EXAMPLE.com", "TEST3@example.com"],
            ["Test4@EXAMPLE.com", "Test4@example.com"],
            ["test5@eXAMPLE.COM", "test5@example.com"],
        ]

        for email, normalized_email in sample_emails:
            user = get_user_model().objects.create_user(email, 'testuser')
            self.assertEqual(user.email, normalized_email)

    def test_new_user_without_email_raises_error(self):
        """
        Test that creating a user without an email raises a ValueError
        """
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user('', 'test123')

    def test_create_superuser(self):
        """
        Test that creating a super user is successful
        """
        user = get_user_model().objects.create_superuser(
            'test@example.com', 'test123'
        )
        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)

    # RECIPE MODEL TESTS

    def test_recipe_str(self):
        """
        Test the recipe string representation
        """
        user = get_user_model().objects.create_user(
            name="Test User",
            email="test@example.com",
            password="test123"
        )
        recipe = models.Recipe.objects.create(
            user=user,
            title='Steak and mushroom sauce',
            time_minutes=20,
            price=Decimal('5.00'),
            description='Great recipe for steak and mushroom sauce'
        )

        self.assertEqual(str(recipe), recipe.title)

    def test_create_tag(self):
        """Test Creating a tag is succeeful"""
        user = create_user()
        tag = models.Tag.objects.create(user=user, name='Vegan')

        self.assertEqual(str(tag), tag.name)
