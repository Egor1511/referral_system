from django.db.models.signals import pre_save
from django.dispatch import receiver

from users.models import UserProfile
from users.services import generate_invite_code


@receiver(pre_save, sender=UserProfile)
def pre_save_user_profile(sender, instance, **kwargs):
    """
    Signal receiver to generate invite code before saving UserProfile.
    """
    if not instance.invite_code:
        instance.invite_code = generate_invite_code()
