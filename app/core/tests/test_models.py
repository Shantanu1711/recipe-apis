from django.test import TestCase
from django.contrib.auth import get_user_model


class ModelTests(TestCase):

    def test_create_user_with_email_succesful(self):
        """
        test creating a user with email address
        """

        email = 'test@example.com'
        password = 'testpass123'

        user = get_user_model().objects.create_user(email, password)
        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_new_user_email_normalize(self):

        sample_emails = [
            ['test1@Example.com', 'test1@example.com'],
            ['TEST2@Example.com', 'TEST2@example.com'],
            ['Test3@Example.Com', 'Test3@example.com'],
            ['test4@EXAMPLE.COM', 'test4@example.com'],
        ]
        for email, expected in sample_emails:
            user = get_user_model().objects.create_user(email, 'sample123')
            self.assertEqual(user.email, expected)

    def test_new_user_without_email_raises_valueerror(self):

        with self.assertRaises(ValueError):
            get_user_model().objects.create_user('', "sample123")

    def test_create_superuser(self):

        user = get_user_model().objects.create_superuser(
            'test2example.com',
            'test123'
        )
        self.assertTrue(user.is_staff)
        self.assertTrue(user.is_superuser)
