from rest_framework import routers
from .api import MessageViewSetList, MessageViewSetSingle

router = routers.DefaultRouter()
router.register('api/list', MessageViewSetList, 'messages')
router.register('api/single', MessageViewSetSingle, 'messages')


urlpatterns = router.urls