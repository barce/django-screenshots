from django.db.models.signals import post_save
from django.db.models.signals import pre_save
from screenshots.models import Screenshot
from django.dispatch import receiver
from screenshots.tasks import create_screenshot
import django_rq

@receiver(pre_save, sender=Screenshot)
def set_screenshot_attributes(sender, instance, **kwargs):
    print("pre_save hook")
    print(instance.set_filename())
    print("exist pre_save")

@receiver(post_save, sender=Screenshot)
def create_screenshot_job(sender, instance, **kwargs):
    print("post_save hook")
    print("+++")
    print(instance.url)
    print(instance.status)
    print("+++")
    if instance.status == '':
        print("instance.status is none")
        queue = django_rq.get_queue('screenshots')
        result = queue.enqueue(create_screenshot, instance.url)
