from selenium import webdriver
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from django.urls import reverse
import time

class TestProject(StaticLiveServerTestCase):
    def setUp(self):
        self.browser = webdriver.Chrome('tests/chromedriver.exe')

    def tearDown(self):
        self.browser.close()

    def test(self):
        self.browser.get(self.live_server_url)
        time.sleep(20)