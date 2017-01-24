
from unittest import TestCase

import django_screenshots 
from django_screenshots import Builder


class TestBuilder(TestCase):
    def test_capture(self):
        b = django_screenshots.Builder('http://twitter.com')
        self.assertTrue(isinstance(b, Builder))
