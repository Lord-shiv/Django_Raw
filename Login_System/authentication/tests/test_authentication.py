from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User


class BaseTest(TestCase):
    def setUp(self):
        self.register_url = reverse("register")
        self.login_url = reverse("login")
        self.user = {
            "email": "testemail@gmail.com",
            "username": "username",
            "password": "password",
            "password2": "password",
            "name": "fullname",
        }
        self.user_short_password = {
            "email": "testemail@gmail.com",
            "username": "username",
            "password": "tes",
            "password2": "tes",
            "name": "fullname",
        }
        self.user_unmatching_password = {
            "email": "testemail@gmail.com",
            "username": "username",
            "password": "testtest",
            "password2": "testto",
            "name": "fullname",
        }
        self.user_invalid_email = {
            "email": "test.com",
            "username": "username",
            "password": "testtest",
            "password2": "testto",
            "name": "fullname",
        }

        return super().setUp()


class RegisterTest(BaseTest):
    def test_can_view_page_correctly(self):
        response = self.client.get(self.register_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "auth/register.html")

    def test_can_register_user(self):
        response = self.client.post(self.register_url, self.user, format="text/html")
        self.assertEqual(response.status_code, 302)

    def test_cant_register_user_with_short_password(self):
        response = self.client.post(
            self.register_url, self.user_short_password, format="text/html"
        )
        self.assertEqual(response.status_code, 400)

    def test_cant_register_user_with_unmatching_passwords(self):
        response = self.client.post(
            self.register_url, self.user_unmatching_password, format="text/html"
        )
        self.assertEqual(response.status_code, 400)

    def test_cant_register_user_with_invalid_email(self):
        response = self.client.post(
            self.register_url, self.user_invalid_email, format="text/html"
        )
        self.assertEqual(response.status_code, 400)

    def test_cant_register_user_with_taken_email(self):
        self.client.post(self.register_url, self.user, format="text/html")
        response = self.client.post(self.register_url, self.user, format="text/html")
        self.assertEqual(response.status_code, 400)


class LoginTest(BaseTest):
    def test_can_access_page(self):
        response = self.client.get(self.login_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "auth/login.html")

    def test_login_success(self):
        self.client.post(self.register_url, self.user, format="text/html")
        user = User.objects.filter(email=self.user["email"]).first()
        user.is_active = True
        user.save()
        response = self.client.post(self.login_url, self.user, format="text/html")
        self.assertEqual(response.status_code, 302)

    def test_cant_login_with_unverified_email(self):
        self.client.post(self.register_url, self.user, format="text/html")
        response = self.client.post(self.login_url, self.user, format="text/html")
        self.assertEqual(response.status_code, 401)

    def test_cant_login_with_no_username(self):
        response = self.client.post(
            self.login_url, {"password": "passwped", "username": ""}, format="text/html"
        )
        self.assertEqual(response.status_code, 401)

    def test_cant_login_with_no_password(self):
        response = self.client.post(
            self.login_url, {"username": "passwped", "password": ""}, format="text/html"
        )
        self.assertEqual(response.status_code, 401)
