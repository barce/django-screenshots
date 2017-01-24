from django.test import TestCase
from screenshots.models import Screenshot
from subprocess import call
import subprocess
from time import sleep

# TODO: separate s3 buckets into environment buckets: dev, test, prod

# Create your tests here.
class ScreenshotTestCase(TestCase):
    def setUp(self):
        Screenshot.objects.create(url="http://www.cnn.com", image_url="")
        Screenshot.objects.create(url="http://www.espn.com", image_url="")

    def test_screenshot_has_md5_filename(self):
        """Screenshots """
        cnn = Screenshot.objects.get(url="http://www.cnn.com")
        espn = Screenshot.objects.get(url="http://www.espn.com")
        self.assertEqual(cnn.set_filename(), 'c50252f4f24784b5d368926df781ede9.png')
        self.assertEqual(espn.set_filename(), '502c1e280b68524231c2a17a0f1e4187.png')
