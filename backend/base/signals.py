from django.db.models.signals import pre_save
from django.contrib.auth.models import User

# to use name value for username and email


def updateUser(sender, instance, **kwargs):
    print('Signal Triggered')
    user = instance
    if user.email != '':
        user.username = user.email


pre_save.connect(updateUser, sender=User)
