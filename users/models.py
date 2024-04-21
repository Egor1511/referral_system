from django.db import models
from rest_framework.exceptions import ValidationError

from users.services import generate_invite_code


class UserProfile(models.Model):
    phone_numbers = models.CharField(
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

    def save(self, *args, **kwargs):
        """
        Saves the UserProfile object.
        Args:
            *args: Variable length argument list.
            **kwargs: Arbitrary keyword arguments.
        Returns:
            None
        """
        if not self.invite_code:
            self.invite_code = generate_invite_code()
        super().save(*args, **kwargs)

    def clean(self):
        """
        Validation for self-invite cases.

        Raises:
            ValidationError: Self-invite cases are not allowed.
        """
        if self.invited_by == self:
            raise ValidationError("You cannot invite yourself.")
