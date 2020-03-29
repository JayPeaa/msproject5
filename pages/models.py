from django.db import models


class Subscriber(models.Model):
    """ document here """
    email = models.EmailField(max_length=254, null=False, blank=False, default='')
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email