from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver
from Lamersroom.models import Profile, Post
from django.contrib.auth import get_user_model


@receiver(post_save, sender=get_user_model())
def auto_profile_add(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)