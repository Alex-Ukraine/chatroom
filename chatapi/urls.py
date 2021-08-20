from rest_framework import routers
from .api import MessageViewSetList, MessageViewSetSingle

router = routers.DefaultRouter()
router.register('api/list', MessageViewSetList, 'apilist')
router.register('api/single', MessageViewSetSingle, 'apisingle')


urlpatterns = router.urls