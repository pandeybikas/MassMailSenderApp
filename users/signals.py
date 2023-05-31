from django.db.models .signals import post_save
from django.dispatch import receiver
from .models import Profile
from django.contrib.auth.models import User

@receiver(post_save, sender=User)
def create_profile(sender, created, instance, **Kwargs):
    if created:
        Profile.objects.create(user=instance)
