from django.test import TestCase
from django.contrib.auth import get_user_model

User = get_user_model()

# Create your tests here.
class ModelTests(TestCase):
    def test_create_user_with_email_and_password_success(self):
        """Test if the user was created with an email and password"""
        email = "mahmoud@test.com"
        password = "testing1234"

        user = User.objects.create_user(email=email, password=password)
        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_normalize_email(self):
        """Test if the email is normalized i.e in all lowercase"""
        email = "mahmoud@TEST.com"
        password = "testing1234"

        user = User.objects.create_user(email=email.lower(), password=password)
        self.assertEquals(user.email, email.lower())

    def test_new_user_without_email_exception(self):
        with self.assertRaises(ValueError):
            email = "mahmoud@test.com"
            password = "testing1234"

            user = User.objects.create_user(email=None, password=password)

    def test_create_superuser(self):
        email = "mahmoud@test.com"
        password = "testing1234"

        user = User.objects.create_superuser(email=email, password=password)
        self.assertTrue(user.is_staff)
        self.assertTrue(user.is_superuser)

    def test_create_superuser_without_password(self):
        with self.assertRaises(ValueError):
            email = "mahmoud@test.com"
            user = User.objects.create_superuser(email=email, password=None)
        