import time

from rest_framework import status
from rest_framework import viewsets
from rest_framework.mixins import UpdateModelMixin, RetrieveModelMixin
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet

from users.models import UserProfile
from users.serializers import PhoneNumberInputSerializer, \
    AuthCodeInputSerializer, ProfileSerializer


class SendPhoneNumberViewSet(viewsets.ViewSet):
    serializer_class = PhoneNumberInputSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            phone_number = serializer.validated_data.get('phone_number')
            request.session['phone_number'] = phone_number

            time.sleep(2)
            return Response({'message': 'Auth code sent'},
                            status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class SendAuthCodeViewSet(viewsets.ViewSet):
    serializer_class = AuthCodeInputSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            phone_number = request.session['phone_number']
            user, _ = UserProfile.objects.get_or_create(
                phone_number=phone_number)
            return Response({'message': 'Phone number verified'},
                            status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ProfileViewSet(GenericViewSet, RetrieveModelMixin, UpdateModelMixin):
    serializer_class = ProfileSerializer
    queryset = UserProfile.objects.all()

    def partial_update(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data,
                                         partial=True)
        serializer.is_valid(raise_exception=True)

        used_invite_code = serializer.validated_data.get('used_invite_code')
        invited_by = instance.get_invited_by(used_invite_code)

        if instance.invite_code == used_invite_code:
            return Response({"error": "You cannot use your own invite code"},
                            status=status.HTTP_400_BAD_REQUEST)

        if invited_by is None:
            return Response({"error": "Object does not exist"},
                            status=status.HTTP_404_NOT_FOUND)

        instance.used_invite_code = used_invite_code
        instance.invited_by = invited_by
        instance.save()

        return Response(serializer.data, status=status.HTTP_200_OK)
