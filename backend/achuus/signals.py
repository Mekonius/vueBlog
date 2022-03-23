from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from .models import AchuuProfile


@receiver(post_save, sender=User)
def create_profile(instance, created, **kwargs):
    if created:
        profile = AchuuProfile(user=instance)
        profile.save(["user"])
