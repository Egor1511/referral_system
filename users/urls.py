from rest_framework.routers import SimpleRouter

from users.views import SendPhoneNumberViewSet, SendAuthCodeViewSet

router_v1 = SimpleRouter()

router_v1.register(
    r'send_phone_number',
    SendPhoneNumberViewSet,
    basename='send_phone_number'
)
router_v1.register(
    r'send_auth_code',
    SendAuthCodeViewSet,
    basename='send_auth_code'
)

urlpatterns = router_v1.urls
