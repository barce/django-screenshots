from __future__ import unicode_literals
from django.db import models
import hashlib
import urllib.parse
# Create your models here.
class Screenshot(models.Model):
    id = models.AutoField("ID", primary_key=True)
    url = models.CharField(max_length=255)
    image_url = models.CharField(max_length=255)
    filename = models.CharField(max_length=255)
    status = models.CharField(max_length=255)

    def set_filename(self):
        m = hashlib.md5()
        m.update(self.url.encode('utf-8'))
        self.filename = m.hexdigest() + '.png'
        return self.filename
