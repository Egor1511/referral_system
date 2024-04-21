import time

from rest_framework import status
from rest_framework import viewsets
from rest_framework.response import Response

from users.models import UserProfile
from users.serializers import PhoneNumberInputSerializer, \
    AuthCodeInputSerializer


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
                phone_numbers=phone_number)
            return Response({'message': 'Phone number verified'},
                            status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
