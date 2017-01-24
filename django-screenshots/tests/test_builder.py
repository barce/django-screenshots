
from unittest import TestCase

import automatedscreenshots
from automatedscreenshots import Builder


class TestBuilder(TestCase):
    def test_capture(self):
        b = automatedscreenshots.Builder('http://twitter.com')
        self.assertTrue(isinstance(b, Builder))
