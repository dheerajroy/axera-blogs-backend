from rest_framework.routers import SimpleRouter
from .views import TopicViewset

router = SimpleRouter()
router.register('', TopicViewset)

urlpatterns = router.get_urls()
