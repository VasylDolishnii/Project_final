from django.urls import reverse, resolve
from django.test import SimpleTestCase

from osiedle_app.views import about
from users.views import loginPage, registerPage, logoutUser


class TestUrls(SimpleTestCase):
    def test_login_url_resolved(self):
        url = reverse('login')
        self.assertEquals(resolve(url).func, loginPage)

    def test_register_url_resolved(self):
        url = reverse('register')
        self.assertEquals(resolve(url).func, registerPage)

    def test_logout_url_resolved(self):
        url = reverse('logout')
        self.assertEquals(resolve(url).func, logoutUser)

    def test_about_url_resolved(self):
        url = reverse('about')
        self.assertEquals(resolve(url).func, about)
