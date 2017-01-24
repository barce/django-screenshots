from __future__ import unicode_literals

from django.apps import AppConfig


class ScreenshotsConfig(AppConfig):
    name = 'screenshots'

    def ready(self):
        import screenshots.profiles.signals
