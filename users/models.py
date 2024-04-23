from django.db import models


class UserProfile(models.Model):
    phone_number = models.CharField(
        max_length=15,
        unique=True,
    )
    invite_code = models.CharField(
        max_length=6,
        unique=True,
    )
    used_invite_code = models.CharField(
        max_length=6,
        blank=True,
        null=True,
    )
    invited_by = models.ForeignKey(
        'self',
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        related_name='invited_by_users',
    )

    class Meta:
        ordering = ('-id',)
        verbose_name = 'User Profile'
        verbose_name_plural = 'User Profiles'

    def __str__(self):
        """
        Returns a string representation of the UserProfile object.

        Returns:
            str: The phone numbers of the user.
        """
        return self.phone_numbers

    @staticmethod
    def get_invited_by(invite_code):
        try:
            return UserProfile.objects.get(invite_code=invite_code)
        except UserProfile.DoesNotExist:
            return None

    @staticmethod
    def get_list_of_invitees(obj):
        invitees = UserProfile.objects.select_related('invited_by').filter(
            invited_by=obj)
        return [invitee.phone_number for invitee in invitees]
