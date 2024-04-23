from rest_framework import serializers

from users.models import UserProfile


class PhoneNumberInputSerializer(serializers.Serializer):
    phone_number = serializers.CharField(
        max_length=15,
    )


class AuthCodeInputSerializer(serializers.Serializer):
    auth_code = serializers.CharField(
        max_length=4,
        min_length=4,
    )

    def validate_auth_code(self, value):
        """
        Custom validator to check if the auth code is exactly 4 digits.
        """

        if len(value) != 4 and not value.isdigit():
            raise serializers.ValidationError("Invalid auth code.")
        return value


class ProfileSerializer(serializers.ModelSerializer):
    list_of_invitees = serializers.SerializerMethodField()

    class Meta:
        model = UserProfile
        fields = (
            'phone_number', 'invite_code', 'used_invite_code',
            'list_of_invitees')

    def get_list_of_invitees(self, obj) -> list:
        """
        Get a list of phone numbers of users
        who were invited by the given object.
        Args:
            obj (UserProfile): The UserProfile object
            to get the list of invitees for.
        Returns:
            list: A list of phone numbers of the invitees.
        """
        context = obj.get_list_of_invitees(obj)
        return context
