from django.db import models


class mail_track(models.Model):
    sender_email = models.EmailField()
    receiver_email = models.EmailField()
    counter = models.IntegerField(default=0)
    is_opened = models.BooleanField(default=False)
