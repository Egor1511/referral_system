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
