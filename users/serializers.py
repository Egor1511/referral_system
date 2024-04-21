from rest_framework import serializers


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
