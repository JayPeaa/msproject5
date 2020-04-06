from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


class Profile(models.Model):
    """ Profile DB model linked to Djangos inbuilt user model
    with a 1-2-1 relationship """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    user_street_address_1 = models.CharField(max_length=60, blank=False)
    user_street_address_2 = models.CharField(max_length=60, blank=False)
    user_city = models.CharField(max_length=40, blank=False)
    user_county = models.CharField(max_length=40, blank=False)
    user_country = models.CharField(max_length=40, blank=False)
    user_postcode = models.CharField(max_length=20, blank=False)
    user_phone_number = models.CharField(max_length=20, blank=False)

    def __str__(self):
        return self.user.username


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    """Signals allow decoupled applications to be notified when
    actions occur used here to create profile when a new user is created"""
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    """Signals allow decoupled applications to be notified when
    actions occur used here to save profile when a new user is created"""
    instance.profile.save()
