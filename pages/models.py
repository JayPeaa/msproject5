from django.db import models


class Subscribe(models.Model):
    """ document here """
    subscriber = models.EmailField(max_length=254, null=False, blank=False, default='')