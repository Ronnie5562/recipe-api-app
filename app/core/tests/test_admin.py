"""
Test for the django admin modi
"""
from django.test import TestCase, Client
from django.contrib.auth import get_user_model
from django.urls import reverse


class AdmiSiteTests(TestCase):

    def setUp(self):
        print('Starting Admin site test ...')
        self.client = Client()
        self.admin_user = get_user_model().objects.create_superuser(
            email='admin@example.com',
            password='admin123'
        )

        self.client.force_login(self.admin_user)

        self.user = get_user_model().objects.create_user(
            email = 'test@example.com',
            password = 'test123',
            name = 'Test user'
        )

    def test_user_list(self):
        """ Test that users are listed on user page"""
        url = reverse('admin:core_user_changelist')
        response = self.client.get(url)

        self.assertContains(response, self.user.name)
        self.assertContains(response, self.user.email)

    def test_admin_user_change_page_works(self):
        """Test that the user edit page works"""
        url = reverse("admin:core_user_change", args=[self.user.id])
        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)

    def test_create_user_page(self):
        """Test that the create user page works"""
        url = reverse("admin:core_user_add")
        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)