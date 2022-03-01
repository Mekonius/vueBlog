from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from achuus.models import Achuu_Profile


@receiver(post_save, sender=User)
def create_profile(instance, created, **kwargs):
    if created:
        profile = Achuu_Profile(user=instance)
        profile.save(["user"])
