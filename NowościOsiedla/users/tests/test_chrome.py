from django.test import SimpleTestCase
from selenium import webdriver
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from django.urls import reverse, resolve

import time

from osiedle_app.views import about
from users.forms import UserRegisterForm
from users.views import loginPage, logoutUser, registerPage


class TestU_Singin_login(StaticLiveServerTestCase):
    def setUp(self):
        self.browser = webdriver.Chrome('users/tests/chromedriver.exe')

    def tearDown(self):
        self.browser.close()

    def test_project_buton_ink_text_sing_in(self):
        self.browser.get(self.live_server_url)

        add_url_register = self.live_server_url + reverse('register')
        self.browser.find_element_by_link_text('Sign Up').click()
        self.assertEquals(self.browser.current_url, add_url_register)
        time.sleep(3)

    def test_project_buton_ink_text_log_in(self):
        self.browser.get(self.live_server_url)

        add_url_login = self.live_server_url + reverse('login')
        self.browser.find_element_by_link_text('Log In').click()
        self.assertEquals(self.browser.current_url, add_url_login)
        time.sleep(3)

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