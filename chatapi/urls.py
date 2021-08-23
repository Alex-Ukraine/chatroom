from rest_framework import routers
from .api import MessageViewSetList, MessageViewSetSingle

router = routers.DefaultRouter()
router.register('api/list', MessageViewSetList, 'api-list')
router.register('api/single', MessageViewSetSingle, 'api-single')


urlpatterns = router.urls